# ==============================================================================
# Project Name: Job Fit Evaluator API Runner (Two-Stage + Key Pool Version)
# Author: Scott Malin, CISSP
#
# Version: 1.8.9
# Updated: 2026-10-17
#
# CHANGELOG:
#   - v1.8.9 (2026-10-17): Implemented robust pre-flight checks validating Python
#     version, required pip packages, and folder write permissions with exact fix
#     commands. Added detailed, LLM-friendly section-by-section troubleshooting docs.
#   - v1.8.8 (2026-10-16): Two-stage evaluation pipeline: local Ollama triage
#     followed by Gemini deep evaluation using a multi-key pool rotation.
#
# PURPOSE FOR EXTERNAL LLM / TROUBLESHOOTING ASSISTANTS:
#   This script automates job search evaluations. 
#   - STAGE 1: Quick local filter using Ollama (llama3.1:latest).
#   - STAGE 2: Deep evaluation using Google Gemini API with key rotation and daily caps.
#   - OUTPUTS: JSON reports per job, an HTML dashboard, and an email summary.
#   - COMMON ISSUES: Missing API keys, network/timeout issues with Ollama or Gemini, 
#     or missing pip dependencies. Refer to the pre-flight check outputs for fixes.
# ==============================================================================

import os
import sys
import time
import json
import re
import argparse
import smtplib
import importlib.util
import html
import datetime

from datetime import datetime, date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from urllib.parse import urlparse
from pathlib import Path


# ==============================================================================
# Pre-Flight Prerequisites Check
# ==============================================================================
# LLM Troubleshooting Note: If this block fails, it stops execution immediately 
# and prints the exact command needed to fix your environment. Do not bypass this.
def run_preflight_checks():
    # 1. Validate Python Version (Requires Python 3.8+)
    if sys.version_info < (3, 8):
        print("=" * 65)
        print(f"[!] ERROR: Python 3.8 or higher is required. Found: {sys.version.split()[0]}")
        print("[!] Fix Command: Download and install Python from https://www.python.org/")
        print("=" * 65)
        sys.exit(1)

    # 2. Validate Required Pip Packages
    required_modules = ["openai", "playwright"]
    missing_deps = [m for m in required_modules if importlib.util.find_spec(m) is None]
    if missing_deps:
        print("=" * 65)
        print(f"[!] ERROR: Missing required Python packages: {', '.join(missing_deps)}")
        print(f"[!] Fix Command: pip install {' '.join(missing_deps)}")
        print("=" * 65)
        sys.exit(1)

    # 3. Validate Folder Write Permissions
    test_dirs = [
        os.getenv("EVALUATOR_COMPANIES_DIR", "./companies"),
        os.getenv("EVALUATOR_OUTPUT_DIR", "./output")
    ]
    for d in test_dirs:
        try:
            path_obj = Path(d)
            path_obj.mkdir(parents=True, exist_ok=True)
            test_file = path_obj / ".permissions_test"
            test_file.write_text("test", encoding="utf-8")
            test_file.unlink(missing_ok=True)
        except Exception as e:
            print("=" * 65)
            print(f"[!] ERROR: Lacks write permissions or invalid path for directory: {d}")
            print(f"[!] Details: {e}")
            print(f"[!] Fix Command: Check folder permissions or update environment variables.")
            print("=" * 65)
            sys.exit(1)

# Execute pre-flight validation right away
run_preflight_checks()

from openai import OpenAI


# ==============================================================================
# User-Configurable Settings and Thresholds
# ==============================================================================
# LLM Troubleshooting Note: Modify these constants or use environment variables 
# if your API keys, model names, or directory paths change.

GEMINI_API_KEYS = [
    os.getenv("GEMINI_API_KEY", ""),
    os.getenv("GEMINI_API_KEY_2", "")
]

MAX_TOTAL_DAILY_CALLS = 20

GEMINI_BASE_URL = os.getenv(
    "EVALUATOR_BASE_URL",
    "https://generativelanguage.googleapis.com/v1beta/openai/"
)

GEMINI_MODEL = os.getenv(
    "EVALUATOR_MODEL",
    "gemini-2.5-flash"
)

OLLAMA_LOCAL_ENDPOINT = "http://localhost:11434/v1"
OLLAMA_LOCAL_MODEL = "llama3.1:latest"
LOCAL_REQUEST_TIMEOUT = 120.0
STAGE1_MAX_DESC_CHARS = 1000

USAGE_FILE = os.path.join(
    os.getenv("EVALUATOR_OUTPUT_DIR", "./output"),
    "api_usage_pool.json"
)

try:
    REQUEST_TIMEOUT_SECONDS = max(1.0, float(os.getenv("EVALUATOR_REQUEST_TIMEOUT", "60")))
except ValueError:
    REQUEST_TIMEOUT_SECONDS = 60.0

try:
    COOLDOWN_SECONDS = max(0.0, float(os.getenv("EVALUATOR_COOLDOWN_SECONDS", "1")))
except ValueError:
    COOLDOWN_SECONDS = 1.0

try:
    MAX_DESCRIPTION_CHARS = max(500, int(os.getenv("EVALUATOR_MAX_DESCRIPTION_CHARS", "8000")))
except ValueError:
    MAX_DESCRIPTION_CHARS = 8000

STRONG_FIT_THRESHOLD = 80
MODERATE_FIT_THRESHOLD = 60
STAGE1_SCORE_THRESHOLD = 60

CATEGORY_WEIGHTS = {
    "responsibilities_score": 0.30,
    "required_qualifications_score": 0.30,
    "skills_technologies_education_score": 0.25,
    "preferred_qualifications_score": 0.15,
}

COMPANIES_DIR = os.getenv("EVALUATOR_COMPANIES_DIR", "./companies")
EVALUATION_DIR = os.getenv("EVALUATOR_OUTPUT_DIR", "./output")
RESUME_PATH = os.getenv("EVALUATOR_RESUME_PATH", "./resume.md")
PROMPT_PATH = os.getenv("EVALUATOR_PROMPT_PATH", "./prompts/Universal Job Fit Evaluation Prompt - API Call.md")
LITE_PROMPT_PATH = os.getenv("EVALUATOR_LITE_PROMPT_PATH", "./prompts/Lite Job Fit Evaluation Prompt - API Call.md")

SMTP_SERVER = os.getenv("EVALUATOR_SMTP_SERVER", "smtp.gmail.com")
try:
    SMTP_PORT = int(os.getenv("EVALUATOR_SMTP_PORT", "587"))
except ValueError:
    SMTP_PORT = 587

MAIL_FROM = os.getenv("EVALUATOR_MAIL_FROM", "")
MAIL_TO = os.getenv("EVALUATOR_MAIL_TO", "")
APP_PASSWORD = os.getenv("EVALUATOR_APP_PASSWORD", "")

_DEFAULT_EXCLUDED_TITLE_TERMS = ("recruiter", "administrative business partner", "sales engineer", "intern")


# ==============================================================================
# Command-Line Arguments & Exclusions
# ==============================================================================
# LLM Troubleshooting Note: Handles CLI arguments (--company, --force, --dry-run) 
# and filters out unwanted job titles based on keywords.

def parse_arguments():
    parser = argparse.ArgumentParser(description="Job Fit Evaluator API Runner (v1.8.9)")
    parser.add_argument("--company", type=str, default=None, help="Process specific company file.")
    parser.add_argument("--force", action="store_true", help="Re-evaluate postings regardless of state.")
    parser.add_argument("--dry-run", action="store_true", help="Show eligible postings without calling models.")
    return parser.parse_args()


_env_exclusions = os.getenv("EVALUATOR_EXCLUDED_TITLE_TERMS")
EXCLUDED_TITLE_TERMS = _DEFAULT_EXCLUDED_TITLE_TERMS if _env_exclusions is None else tuple(t.strip().lower() for t in _env_exclusions.split(",") if t.strip())

def get_title_exclusion_reason(title):
    norm = normalize_text(title).lower()
    for term in EXCLUDED_TITLE_TERMS:
        if term in norm:
            return f"Title matched exclusion term: {term}"
    return None


# ==============================================================================
# Output Directories and State
# ==============================================================================
# LLM Troubleshooting Note: Sets up output folders and initializes the local Ollama client.

os.makedirs(EVALUATION_DIR, exist_ok=True)
TODAY_STR = datetime.now().strftime("%Y-%m-%d")
OUTPUT_DIR = os.path.join(EVALUATION_DIR, f"evaluation_reports_{TODAY_STR}")
os.makedirs(OUTPUT_DIR, exist_ok=True)
STATE_FILE = os.path.join(EVALUATION_DIR, "eval_progress.json")

CYAN, GREEN, YELLOW, RED, RESET = "\033[96m", "\033[92m", "\033[93m", "\033[91m", "\033[0m"

local_client = OpenAI(
    base_url=OLLAMA_LOCAL_ENDPOINT,
    api_key="ollama",
    timeout=LOCAL_REQUEST_TIMEOUT,
    max_retries=1
)


# ==============================================================================
# Multi-Key Pool & Quota Tracking
# ==============================================================================
# LLM Troubleshooting Note: Manages API key rotation and tracks daily usage counts 
# in 'api_usage_pool.json' to prevent exceeding limits.

def load_usage_data():
    today_date = str(date.today())
    if os.path.exists(USAGE_FILE):
        try:
            with open(USAGE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data.get("date") == today_date:
                    return data.get("usage", {})
        except Exception:
            pass
    return {}

def save_usage_data(usage_dict):
    today_date = str(date.today())
    temp_file = USAGE_FILE + ".tmp"
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump({"date": today_date, "usage": usage_dict}, f)
    os.replace(temp_file, USAGE_FILE)

def get_active_gemini_client():
    usage = load_usage_data()
    total_used = sum(usage.values())
    
    if total_used >= MAX_TOTAL_DAILY_CALLS:
        print(f"{RED}[!] Daily pool limit reached ({total_used}/{MAX_TOTAL_DAILY_CALLS}). Stopping Gemini requests.{RESET}")
        return None, None

    for idx, key in enumerate(GEMINI_API_KEYS):
        if not key:
            continue
        key_id = f"key_{idx}"
        if usage.get(key_id, 0) < (MAX_TOTAL_DAILY_CALLS // len(GEMINI_API_KEYS)):
            print(f"[*] Using Gemini Key #{idx + 1} (Total Pool Usage: {total_used}/{MAX_TOTAL_DAILY_CALLS})")
            return OpenAI(base_url=GEMINI_BASE_URL, api_key=key, timeout=REQUEST_TIMEOUT_SECONDS, max_retries=2), key_id
            
    for idx, key in enumerate(GEMINI_API_KEYS):
        if not key:
            continue
        key_id = f"key_{idx}"
        if usage.get(key_id, 0) < MAX_TOTAL_DAILY_CALLS:
            print(f"[*] Using Gemini Key #{idx + 1} (Total Pool Usage: {total_used}/{MAX_TOTAL_DAILY_CALLS})")
            return OpenAI(base_url=GEMINI_BASE_URL, api_key=key, timeout=REQUEST_TIMEOUT_SECONDS, max_retries=2), key_id

    return None, None

def increment_key_usage(key_id):
    if not key_id:
        return
    usage = load_usage_data()
    usage[key_id] = usage.get(key_id, 0) + 1
    save_usage_data(usage)


# ==============================================================================
# Prompt Compatibility Addendum & Utility Functions
# ==============================================================================
# LLM Troubleshooting Note: Provides helper functions for text normalization, 
# safe filename generation, and enforces strict JSON output structure schemas.

API_COMPATIBILITY_ADDENDUM = """
IMPORTANT PYTHON API COMPATIBILITY ADDENDUM:
Return exactly one valid JSON code block conforming to the schema structure:
{
  "evaluation_status": "COMPLETED" or "INSUFFICIENT_INFO",
  "job_title": "string",
  "company": "string",
  "responsibilities_score": integer (0-100) or null,
  "required_qualifications_score": integer (0-100) or null,
  "skills_technologies_education_score": integer (0-100) or null,
  "preferred_qualifications_score": integer (0-100) or null,
  "overall_fit_percentage": "string percentage",
  "fit_rating": "Strong Fit / Moderate Fit / Low Fit / Insufficient Data",
  "confidence": "High / Medium / Low",
  "critical_dealbreaker": "string or None",
  "further_investigation": "Yes / No / Insufficient Information",
  "strongest_alignments": "string",
  "significant_gaps": "string",
  "information_limitations": "string",
  "evaluation_summary": "string"
}
"""

def runtime_string(seconds):
    seconds = max(0, int(seconds))
    return f"{seconds // 60}m {seconds % 60}s" if seconds >= 60 else f"{seconds}s"

def safe_filename(value):
    return re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", str(value)).strip(" .")[:150] or "Unknown_Company"

def normalize_text(value):
    if value is None:
        return ""
    if isinstance(value, list):
        value = ", ".join(str(i) for i in value)
    return re.sub(r"\s+", " ", str(value)).strip()

def escape_html(value):
    return html.escape(str(value or ""), quote=True)

def strip_citations(text):
    return re.sub(r"\s*\\", "", str(text or ""))

def first_available(mapping, keys, default=""):
    if not isinstance(mapping, dict):
        return default
    norm_map = {re.sub(r"[^a-z0-9]+", "_", str(k).strip().lower()): v for k, v in mapping.items()}
    for key in keys:
        val = norm_map.get(re.sub(r"[^a-z0-9]+", "_", str(key).strip().lower()))
        if val is not None and val != "":
            return val
    return default

def normalize_job_record(job, default_company=""):
    if not isinstance(job, dict):
        return {}
    norm = dict(job)
    norm["title"] = normalize_text(first_available(job, ("title", "job_title", "position", "role"), "Unknown Title"))
    norm["company"] = normalize_text(first_available(job, ("company", "company_name", "employer"), default_company))
    norm["link"] = normalize_text(first_available(job, ("link", "url", "job_url", "posting_url", "application_url"), ""))
    norm["description"] = normalize_text(first_available(job, ("description", "job_description", "raw_description", "details"), ""))
    norm["location"] = normalize_text(first_available(job, ("location", "job_location", "city"), "Not specified"))
    norm["work_arrangement"] = normalize_text(first_available(job, ("work_arrangement", "workplace_type", "remote_type"), ""))
    return norm

def make_posting_link(url, label):
    url = str(url or "").strip()
    try:
        parsed = urlparse(url)
        if parsed.scheme.lower() in ("http", "https") and parsed.netloc:
            return f'<a href="{escape_html(url)}" target="_blank" rel="noopener noreferrer">{escape_html(label)}</a>'
    except Exception:
        pass
    return ""


# ==============================================================================
# Input Parsers (Markdown & JSON Reports)
# ==============================================================================
# LLM Troubleshooting Note: Reads job listings stored in markdown or JSON formats 
# inside the companies directory.

def parse_markdown_report(filepath):
    with open(filepath, "r", encoding="utf-8") as handle:
        content = handle.read()

    jobs = []
    for section in content.split("---"):
        if not re.search(r"(?im)^\s*Title\s*:", section):
            continue

        job = {}
        for line in section.strip().splitlines():
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            job[key.strip()] = strip_citations(value).strip()

        normalized_job = normalize_job_record(job)
        if normalized_job.get("title") != "Unknown Title":
            jobs.append(normalized_job)

    return jobs

def parse_company_report(filepath):
    if filepath.lower().endswith(".json"):
        try:
            with open(filepath, "r", encoding="utf-8") as handle:
                data = json.load(handle)

            if isinstance(data, list):
                raw_jobs = data
            elif isinstance(data, dict):
                raw_jobs = None
                for key in ("jobs", "postings", "items"):
                    value = first_available(data, (key,), None)
                    if isinstance(value, list):
                        raw_jobs = value
                        break
                if raw_jobs is None:
                    raw_jobs = [data]
            else:
                return []

            jobs = []
            for item in raw_jobs:
                if isinstance(item, dict):
                    jobs.append(normalize_job_record(item))
            return jobs
        except Exception as error:
            print(f"{YELLOW}[!] Could not parse JSON {filepath}: {error}{RESET}")
            return []

    return parse_markdown_report(filepath)


# ==============================================================================
# Load Prompts & State
# ==============================================================================
# LLM Troubleshooting Note: Loads the candidate resume, evaluation prompt files, 
# and persistent state tracking data.

def load_resume():
    if not os.path.exists(RESUME_PATH):
        raise FileNotFoundError(f"Candidate skills summary not found: {RESUME_PATH}")
    with open(RESUME_PATH, "r", encoding="utf-8") as f:
        return f.read().strip()

def load_evaluation_prompt():
    if not os.path.exists(PROMPT_PATH):
        raise FileNotFoundError(f"Evaluation prompt not found: {PROMPT_PATH}")
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read().strip() + "\n\n" + API_COMPATIBILITY_ADDENDUM

def load_lite_prompt():
    if not os.path.exists(LITE_PROMPT_PATH):
        raise FileNotFoundError(f"Lite prompt file not found: {LITE_PROMPT_PATH}")
    with open(LITE_PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read().strip()

def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                migrated = {}
                for key in data:
                    migrated[str(key)] = {"company": "", "title": "", "status": "completed"}
                return migrated
            return data if isinstance(data, dict) else {}
    except Exception as error:
        raise RuntimeError(f"Could not read progress file '{STATE_FILE}': {error}") from error

def save_state(state_dict):
    temp_path = STATE_FILE + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(state_dict, f, indent=2, ensure_ascii=False)
    
    for attempt in range(5):
        try:
            os.replace(temp_path, STATE_FILE)
            return
        except PermissionError:
            if attempt == 4:
                raise
            time.sleep(0.2)

def make_job_key(company_name, job, index=0):
    title = normalize_text(job.get("title", "Unknown Title"))
    link = normalize_text(job.get("link", ""))
    return f"{company_name}::{title}::{link}" if link else f"{company_name}::{title}::idx_{index}"


# ==============================================================================
# Model Output Validation
# ==============================================================================
# LLM Troubleshooting Note: Validates model JSON responses, computes weighted 
# scores across categories, and handles dealbreakers.

REQUIRED_JSON_KEYS = [
    "evaluation_status", "job_title", "company", "responsibilities_score",
    "required_qualifications_score", "skills_technologies_education_score",
    "preferred_qualifications_score", "overall_fit_percentage", "fit_rating",
    "confidence", "critical_dealbreaker", "further_investigation",
    "strongest_alignments", "significant_gaps", "information_limitations", "evaluation_summary"
]

def strip_markdown_code_fence(text):
    cleaned = (text or "").strip()
    cleaned = re.sub(r"^\s*```[a-zA-Z0-9_-]*\s*\r?\n", "", cleaned, count=1)
    cleaned = re.sub(r"\r?\n```\s*$", "", cleaned, count=1)
    return cleaned.strip()

def parse_category_score(value):
    if value is None:
        return None
    str_val = str(value).strip()
    if str_val.upper() in ("N/A", "NOT PROVIDED", "NONE", "-"):
        return None
    match = re.search(r"\b(\d{1,3})\b", str_val)
    if match:
        score = int(match.group(1))
        if 0 <= score <= 100:
            return score
    return None

def validate_model_response(response_text):
    if not response_text or not response_text.strip():
        raise ValueError("Model returned an empty response.")

    cleaned = strip_markdown_code_fence(response_text)
    try:
        fields = json.loads(cleaned)
    except json.JSONDecodeError as error:
        raise ValueError(f"Model output is not valid JSON: {error}") from error

    if not isinstance(fields, dict):
        raise ValueError("Model JSON output must be an object/dictionary.")

    normalized = {}
    for req in REQUIRED_JSON_KEYS:
        val = fields.get(req)
        if val is None:
            normalized[req] = first_available(fields, [req, req.replace("_", " ")], "Not provided" if req != "critical_dealbreaker" else "None")
        else:
            normalized[req] = val

    evaluation_status = str(normalized.get("evaluation_status", "")).strip().upper()
    if not evaluation_status:
        evaluation_status = "COMPLETED"
        normalized["evaluation_status"] = evaluation_status

    cat_scores = {
        "responsibilities_score": parse_category_score(normalized["responsibilities_score"]),
        "required_qualifications_score": parse_category_score(normalized["required_qualifications_score"]),
        "skills_technologies_education_score": parse_category_score(normalized["skills_technologies_education_score"]),
        "preferred_qualifications_score": parse_category_score(normalized["preferred_qualifications_score"]),
    }

    weighted_sum = 0.0
    total_weight = 0.0
    for k, w in CATEGORY_WEIGHTS.items():
        s = cat_scores.get(k)
        if s is not None:
            weighted_sum += s * w
            total_weight += w

    if total_weight > 0:
        calc_score = int(round(weighted_sum / total_weight))
    else:
        calc_score = 0

    raw_db = str(normalized.get("critical_dealbreaker", "None")).lower()
    if any(k in raw_db for k in ("clearance", "license", "certification", "citizenship", "polygraph", "ts/sci")):
        dealbreaker = normalized["critical_dealbreaker"]
        calc_score = 0
        rating = "Dealbreaker Mismatch"
    elif evaluation_status == "INSUFFICIENT_INFO" or total_weight == 0:
        dealbreaker = "None"
        rating = "Insufficient Data"
    else:
        dealbreaker = "None"
        rating = "Strong Fit" if calc_score >= STRONG_FIT_THRESHOLD else ("Moderate Fit" if calc_score >= MODERATE_FIT_THRESHOLD else "Low Fit")

    normalized["overall_fit_percentage"] = f"{calc_score}%"
    normalized["fit_rating"] = rating

    return {
        "status": "completed",
        "rating": rating,
        "score": calc_score,
        "confidence": str(normalized.get("confidence", "Medium")),
        "critical_dealbreaker": dealbreaker,
        "report_text": json.dumps(fields, indent=2, ensure_ascii=False),
        "fields": normalized,
    }


# ==============================================================================
# HTML Dashboard & Multi-Section Email Reporting
# ==============================================================================
# LLM Troubleshooting Note: Builds the local HTML dashboard and sends out 
# multi-section email summaries via SMTP.

def generate_html_dashboard(successful_evals):
    dashboard_path = os.path.join(OUTPUT_DIR, "evaluation_dashboard.html")
    sorted_evals = sorted(
        successful_evals,
        key=lambda item: (item.get("score") is None, -(item.get("score") or 0), str(item.get("title", "")).lower())
    )

    html_parts = [
        "<!DOCTYPE html>", "<html>", "<head>", '<meta charset="utf-8">',
        f"<title>Job Fit Evaluation Dashboard - {TODAY_STR}</title>",
        """<style>
            body { font-family: Arial, sans-serif; margin: 20px; background: #f4f4f4; color: #333; }
            .container { max-width: 1000px; margin: auto; background: #fff; padding: 30px; border-radius: 8px; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { padding: 12px; border: 1px solid #ddd; text-align: left; }
            th { background: #0066cc; color: #fff; }
            .strong { color: #2e7d32; font-weight: bold; }
            .moderate { color: #f57c00; font-weight: bold; }
            .low { color: #c62828; font-weight: bold; }
            .dealbreaker { color: #8b0000; font-weight: bold; }
        </style></head><body><div class="container">""",
        f"<h1>Job Fit Evaluation Dashboard</h1><p>Run Date: <b>{escape_html(TODAY_STR)}</b> | Completed: <b>{len(sorted_evals)}</b></p>",
        "<table><tr><th>Company</th><th>Job Title</th><th>Location</th><th>Work Arrangement</th><th>Fit Rating</th><th>Score</th></tr>"
    ]

    for item in sorted_evals:
        rating = item.get("rating", "Unknown")
        dealbreaker = item.get("critical_dealbreaker", "None")
        css_class = "dealbreaker" if dealbreaker != "None" else ("strong" if "Strong" in rating else ("moderate" if "Moderate" in rating else "low"))
        display_rating = f"Dealbreaker: {escape_html(dealbreaker)}" if dealbreaker != "None" else escape_html(rating)
        title = escape_html(item.get("title", "Unknown Title"))
        company = escape_html(item.get("company", "Unknown Company"))
        link_html = make_posting_link(item.get("link", ""), title)
        score_text = f"{item.get('score')}%" if item.get('score') is not None else "N/A"

        html_parts.append(f"""<tr>
            <td>{company}</td><td>{link_html or title}</td>
            <td>{escape_html(item.get('location', 'Not specified'))}</td>
            <td>{escape_html(item.get('work_arrangement', 'Not specified'))}</td>
            <td class="{css_class}">{display_rating}</td><td>{score_text}</td></tr>""")

    html_parts.extend(["</table></div></body></html>"])
    with open(dashboard_path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(html_parts))
    print(f"{GREEN}[*] Standalone HTML dashboard generated: {dashboard_path}{RESET}")


def send_email_summary(total_attempted, successful_evals, insufficient_evals, failed_evals, excluded_evals):
    if not MAIL_TO or not MAIL_FROM or not APP_PASSWORD:
        return

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Job Fit Evaluation - {len(successful_evals)} completed, {len(failed_evals)} failed"
    msg["From"] = MAIL_FROM
    msg["To"] = MAIL_TO
    msg["Date"] = formatdate(localtime=True)

    sorted_evals = sorted(
        successful_evals,
        key=lambda item: (item.get("score") is None, -(item.get("score") or 0), str(item.get("title", "")).lower())
    )

    rows_html = ""
    for item in sorted_evals:
        rating = item.get("rating", "Unknown")
        dealbreaker = item.get("critical_dealbreaker", "None")
        
        if dealbreaker != "None":
            badge_style = "background-color: #f8d7da; color: #842029;"
            display_rating = f"Dealbreaker: {escape_html(dealbreaker)}"
        elif "Strong" in rating:
            badge_style = "background-color: #d1e7dd; color: #0f5132;"
            display_rating = escape_html(rating)
        elif "Moderate" in rating:
            badge_style = "background-color: #fff3cd; color: #664d03;"
            display_rating = escape_html(rating)
        else:
            badge_style = "background-color: #f8d7da; color: #842029;"
            display_rating = escape_html(rating)

        title = escape_html(item.get("title", "Unknown Title"))
        link_url = item.get("link", "")
        title_link = f'<a href="{escape_html(link_url)}" target="_blank">{title}</a>' if link_url else title
        score_text = f"{item.get('score')}%" if item.get('score') is not None else "N/A"

        rows_html += f"""
        <tr>
            <td style="padding: 10px; border-bottom: 1px solid #ddd;"><b>{escape_html(item.get('company'))}</b></td>
            <td style="padding: 10px; border-bottom: 1px solid #ddd;">{title_link}</td>
            <td style="padding: 10px; border-bottom: 1px solid #ddd; text-align: center;">
                <span style="padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 12px; {badge_style}">
                    {display_rating}
                </span>
            </td>
            <td style="padding: 10px; border-bottom: 1px solid #ddd; text-align: center; font-weight: bold;">{score_text}</td>
        </tr>
        """

    excluded_html = ""
    if excluded_evals:
        excluded_rows = "".join([
            f"<li><b>{escape_html(x.get('company'))}</b> - {escape_html(x.get('title'))} (<i>{escape_html(x.get('reason'))}</i>)</li>"
            for x in excluded_evals
        ])
        excluded_html = f"<h3>Excluded Postings</h3><ul>{excluded_rows}</ul>"

    html_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.5; padding: 10px;">
        <h2>Job Fit Evaluation Summary ({escape_html(TODAY_STR)})</h2>
        <p>
            <b>Total Attempted:</b> {total_attempted} | 
            <b>Completed:</b> {len(successful_evals)} | 
            <b>Failed:</b> {len(failed_evals)} | 
            <b>Excluded:</b> {len(excluded_evals)}
        </p>
        <table style="width: 100%; border-collapse: collapse; margin-top: 15px;">
            <thead>
                <tr style="background-color: #0066cc; color: #ffffff;">
                    <th style="padding: 10px; text-align: left;">Company</th>
                    <th style="padding: 10px; text-align: left;">Job Title</th>
                    <th style="padding: 10px; text-align: center;">Rating</th>
                    <th style="padding: 10px; text-align: center;">Score</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
        {excluded_html}
    </body>
    </html>
    """

    msg.attach(MIMEText(html_body, "html", "utf-8"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(MAIL_FROM, APP_PASSWORD)
            server.sendmail(MAIL_FROM, MAIL_TO, msg.as_string())
        print(f"{GREEN}[*] Summary email sent successfully.{RESET}")
    except Exception as error:
        print(f"{RED}[!] Failed to send email: {error}{RESET}")


# ==============================================================================
# Main Runner Execution Flow
# ==============================================================================
# LLM Troubleshooting Note: Controls the two-stage pipeline execution:
# 1. Loads configuration files and scans companies directory.
# 2. Stage 1: Local Ollama triage.
# 3. Stage 2: Deep Gemini evaluation with key pool rotation.
# 4. Generates HTML reports and sends emails.

def main():
    if os.name == "nt":
        os.system("cls")

    args = parse_arguments()
    print(f"{CYAN}" + "=" * 65)
    print("  JOB FIT EVALUATOR API RUNNER (Two-Stage + Key Pool v1.8.9)")
    print("=" * 65 + f"{RESET}")

    try:
        resume_content = load_resume()
        full_prompt = load_evaluation_prompt()
        lite_prompt_template = load_lite_prompt()
    except Exception as e:
        print(f"{RED}[!] Error loading files: {e}{RESET}")
        return

    state = load_state()
    ignore_files = {"scraper_run_summary.md", "scraper_run_summary.json", "api_usage_pool.json", "api_usage.json", os.path.basename(STATE_FILE).lower()}
    company_files = [f for f in os.listdir(COMPANIES_DIR) if f.lower().endswith((".md", ".json")) and f.lower() not in ignore_files]

    if args.company:
        target = args.company if args.company.lower().endswith((".md", ".json")) else args.company + ".md"
        company_files = [f for f in company_files if f.lower() == target.lower()]

    all_jobs = []
    excluded = []
    for filename in company_files:
        c_name = os.path.splitext(filename)[0]
        filepath = os.path.join(COMPANIES_DIR, filename)
        for idx, job in enumerate(parse_company_report(filepath)):
            job = normalize_job_record(job, default_company=c_name)
            j_key = make_job_key(c_name, job, idx)
            if not args.force and state.get(j_key, {}).get("status") in ("completed", "needs_review", "failed"):
                continue
            reason = get_title_exclusion_reason(job.get("title"))
            if reason:
                excluded.append({"company": c_name, "title": job.get("title"), "reason": reason})
                continue
            all_jobs.append((c_name, job, j_key))

    print(f"{CYAN}[*] Postings to triage locally: {len(all_jobs)}{RESET}")
    print(f"{YELLOW}[*] Excluded: {len(excluded)}{RESET}")

    if not all_jobs or args.dry_run:
        return

    # STAGE 1: Fast Local Triage
    print(f"\n{CYAN}[*] --- STAGE 1: Local Triage (Ollama / {OLLAMA_LOCAL_MODEL}) ---{RESET}")
    print(f"{YELLOW}[!] Note: Running local inference. CPU/RAM usage may spike temporarily.{RESET}")
    triaged = []

    for idx, (c_name, job, j_key) in enumerate(all_jobs, 1):
        title = job.get("title")
        print(f"[*] [{idx}/{len(all_jobs)}] Triage: {c_name} - {title}...")

        desc = job.get("description", "")[:STAGE1_MAX_DESC_CHARS]
        prompt = lite_prompt_template.format(title=title, company=c_name, location=job.get("location", "Not specified"), description=desc)

        try:
            resp = local_client.chat.completions.create(
                model=OLLAMA_LOCAL_MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                response_format={"type": "json_object"}
            )
            parsed = json.loads(strip_markdown_code_fence(resp.choices[0].message.content))
            job["stage1_score"] = parsed.get("fit_score", 0)
            job["stage1_reason"] = parsed.get("quick_reason", "No reason provided.")
        except Exception as e:
            print(f"    [!] Triage timeout/error (defaulting score 50 to pass through): {e}")
            job["stage1_score"] = 50
            job["stage1_reason"] = "Timeout fallback"

        job["job_key"] = j_key
        job["company_name"] = c_name
        triaged.append(job)

    triaged.sort(key=lambda x: x.get("stage1_score", 0), reverse=True)

    # STAGE 2: Gemini Deep Polish via Key Pool
    print(f"\n{CYAN}[*] --- STAGE 2: Deep Gemini Evaluation (Key Pool Rotation) ---{RESET}")
    target_candidates = [j for j in triaged if j.get("stage1_score", 0) >= STAGE1_SCORE_THRESHOLD]

    if not target_candidates:
        print(f"{YELLOW}[!] No candidates met score threshold ({STAGE1_SCORE_THRESHOLD}%).{RESET}")
        return

    total_attempted = 0
    successful = []
    insufficient = []
    failed = []

    for idx, job in enumerate(target_candidates, 1):
        total_attempted += 1
        client, key_id = get_active_gemini_client()
        if not client:
            print(f"{RED}[!] Daily pool limit reached or all keys exhausted. Stopping run.{RESET}")
            break

        c_name = job["company_name"]
        title = job.get("title")
        print(f"[*] [{idx}/{len(target_candidates)}] Deep Polish: {c_name} - {title}...")

        payload = f"CANDIDATE SKILLS SUMMARY:\n{resume_content}\n\nJOB DETAILS:\nCompany: {c_name}\nTitle: {title}\nDescription:\n{job.get('description', '')[:MAX_DESCRIPTION_CHARS]}"

        try:
            resp = client.chat.completions.create(
                model=GEMINI_MODEL,
                messages=[{"role": "system", "content": full_prompt}, {"role": "user", "content": payload}],
                temperature=0.0,
                response_format={"type": "json_object"}
            )
            increment_key_usage(key_id)
            val = validate_model_response(resp.choices[0].message.content)

            report_file = os.path.join(OUTPUT_DIR, f"{safe_filename(c_name)} - {safe_filename(title)}.json")
            with open(report_file, "w", encoding="utf-8") as f:
                f.write(val["report_text"] + "\n")

            record = {**val, "company": c_name, "title": title, "link": job.get("link", ""), "status": "completed"}
            state[job["job_key"]] = record
            save_state(state)
            successful.append(record)
            print(f"    {GREEN}[✓] Done: {val['rating']} ({val['score']}%){RESET}")
        except Exception as e:
            print(f"    {RED}[!] Error: {e}{RESET}")
            error_record = {
                "status": "failed",
                "error": str(e),
                "company": c_name,
                "title": title,
                "link": job.get("link", ""),
                "score": None,
                "rating": "Failed"
            }
            state[job["job_key"]] = error_record
            save_state(state)
            failed.append({"company": c_name, "title": title, "error": str(e)})

        if COOLDOWN_SECONDS > 0:
            time.sleep(COOLDOWN_SECONDS)

    print(f"\n{GREEN}[*] Pipeline Run Complete. Completed: {len(successful)}{RESET}")

    if successful:
        generate_html_dashboard(successful)
        send_email_summary(total_attempted, successful, insufficient, failed, excluded)

if __name__ == "__main__":
    main()