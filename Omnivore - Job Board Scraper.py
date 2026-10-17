# ==============================================================================
# Project Name: Job Board Scraper & Filter Tool
# Author: Scott Malin, CISSP
# Version: 1.8.3
# Updated: 2026-10-17
#
# LLM ASSISTANT GUIDE (FOR EXTERNAL LLM USERS)
# ------------------------------------------------------------------------------
# Purpose: This script scrapes enterprise job boards (Workday, Greenhouse, etc.),
#   filters roles using keyword and title exclusion logic, stores results in local
#   JSON files with a 30-day rolling history, and outputs run summaries.
#
# Architecture & Data Flow:
#   1. PREREQUISITES CHECK: Validates Python version, pip packages, directory
#      write access, and browser dependencies before execution.
#   2. TARGET CONFIGURATION: Iterates through `TARGET_URLS` dictionary.
#   3. PLATFORM DISPATCH: Routes each URL to its specific scraper (Workday API with
#      subdomain probing, Greenhouse API, Phenom, Dayforce, COCC, or generic HTML).
#   4. NORMALIZATION & FILTERING: Cleans job data, evaluates relevance against
#      `KEYWORDS` and `SECURITY_TITLE_TERMS`, and drops excluded titles.
#   5. HISTORY MANAGEMENT: Loads existing JSON history from `COMPANIES_DIR`, merges
#      active listings, prunes records older than `MAX_AGE_DAYS`, and saves atomically.
#   6. REPORTING: Prints summary stats to the console and writes JSON/log outputs.
#
# Common Troubleshooting for LLMs:
#   - ModuleNotFoundError: Run `pip install scrapling curl_cffi patchright`
#   - Playwright/Patchright errors: Run `python -m patchright install chromium`
#   - PermissionError on COMPANIES_DIR: Check path or folder write permissions.
#
# CHANGELOG
# ------------------------------------------------------------------------------
# v1.8.3 (2026-10-17)
#   - NEW: Added automated pre-flight prerequisites check function `check_prerequisites()`
#     to validate Python version, required modules, and output write access.
#   - NEW: Added inline LLM Assistant Guide documentation header to streamline AI-assisted
#     debugging and code updates.
#
# v1.8.2 (2026-10-16)
#   - NEW: Added automated Workday subdomain and site slug probing logic to dynamically
#     discover active CXS API endpoints and prevent collection failures.
#   - NEW: Added explicit title exclusion terms (recruiter, intern, etc.) to filter out
#     unwanted postings before saving history.
#
# v1.8.1 (2026-10-15)
#   - NEW: Added Workday individual posting description fetching since the
#     search CXS endpoint only returns listing metadata.
#
# v1.8.0 (2026-10-13)
#   - NEW: Switched company history storage from Markdown (.md) to JSON (.json).
#   - NEW: Captured full raw item payloads and non-visible elements in `raw_data`.
#
# v1.7.0 (2026-10-09)
#   - FIX: Strict Workday endpoint validation requires non-empty job postings.
#   - FIX: HTTP errors (404, 422, 500) correctly bubble up as collection failures.
#   - NEW: Added granular exclusion telemetry to track filtering reasons.
# ==============================================================================

from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from logging.handlers import RotatingFileHandler
import importlib.metadata
import importlib.util
import json
import logging
import os
import platform as python_platform
import random
import re
import sys
import time
import traceback
import warnings

from urllib.parse import (
    urljoin,
    urlparse,
    urlunparse,
    parse_qsl,
    urlencode,
)


# ==============================================================================
# Configuration Constants
# ==============================================================================

VERSION = "1.8.3"

COMPANIES_DIR = os.getenv("JOB_SCRAPER_DIR", "./companies")
MAX_AGE_DAYS = 30

VERBOSE_DEBUG = False

REQUEST_TIMEOUT = 30
BROWSER_TIMEOUT_MS = 60000
BROWSER_WAIT_MS = 5000

MIN_REQUEST_DELAY = 2.5
MAX_REQUEST_DELAY = 5.0

WORKDAY_PAGE_SIZE = 20
WORKDAY_MAX_PAGES = 25

MAX_DESCRIPTION_LENGTH = 5000

DIAGNOSTIC_MODE = False
DIAGNOSTIC_OUTPUT_DIR = "diagnostics"


# ==============================================================================
# Robust Prerequisites Check
# ==============================================================================
# Validates environment health before launching scraping routines. Stops execution
# and outputs actionable fix commands if any requirement fails.
# ==============================================================================

def check_prerequisites():
    errors = []

    # 1. Check Python Version (Requires 3.8+)
    if sys.version_info < (3, 8):
        errors.append(
            f"Python version 3.8 or higher is required. Current version: {python_platform.python_version()}\n"
            f"  Fix: Upgrade Python from python.org."
        )

    # 2. Check Required Pip Modules
    required_modules = ["scrapling", "curl_cffi", "patchright"]
    missing_modules = [m for m in required_modules if importlib.util.find_spec(m) is None]
    if missing_modules:
        errors.append(
            f"Missing required Python packages: {', '.join(missing_modules)}\n"
            f"  Fix: Run 'pip install scrapling curl_cffi patchright'"
        )

    # 3. Check Directory Access & Permissions
    try:
        os.makedirs(COMPANIES_DIR, exist_ok=True)
        test_file = os.path.join(COMPANIES_DIR, ".write_test")
        with open(test_file, "w", encoding="utf-8") as f:
            f.write("test")
        os.remove(test_file)
    except Exception as exc:
        errors.append(
            f"Target directory is not writable: {COMPANIES_DIR}\n"
            f"  Error: {exc}\n"
            f"  Fix: Check path existence and folder write permissions."
        )

    if errors:
        print("=" * 70)
        print("PREREQUISITES CHECK FAILED")
        print("=" * 70)
        for err in errors:
            print(f"\n[!] {err}")
        print("\n" + "=" * 70)
        sys.exit(1)


# Run prerequisites check immediately on script launch
check_prerequisites()

warnings.filterwarnings("ignore", category=DeprecationWarning)

from scrapling import StealthyFetcher
from curl_cffi import requests as cffi_requests
from patchright.sync_api import sync_playwright


# ==============================================================================
# Terminal Colors Utility
# ==============================================================================

class C:
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


# ==============================================================================
# Relevance Filtering & Exclusions
# ==============================================================================

KEYWORDS = [
    "Security Engineer",
    "Endpoint Security",
    "CrowdStrike",
    "BeyondTrust",
    "Zero Trust",
    "PowerShell",
    "Python",
    "CISSP",
    "Security Architect",
    "Tanium",
    "Identity and Access Management",
    "Entra ID",
    "Zscaler",
]

SECURITY_TITLE_TERMS = [
    "cybersecurity",
    "cyber security",
    "information security",
    "security engineer",
    "security engineering",
    "security architect",
    "security specialist",
    "security analyst",
    "endpoint security",
    "endpoint protection",
    "endpoint detection",
    "endpoint response",
    "infrastructure security",
    "identity security",
    "identity engineer",
    "identity and access",
    "privileged access",
    "vulnerability management",
    "security platform",
    "security operations",
    "cloud security",
    "application security",
    "product security",
    "network security",
    "security advisor",
    "security consultant",
    "security administrator",
    "security systems",
    "security technology",
]

EXCLUDED_TITLE_TERMS = (
    "recruiter",
    "administrative business partner",
    "sales engineer",
    "intern",
    "university",
    "student",
)

ALLOW_DESCRIPTION_MATCH = True


# ==============================================================================
# Company Targets & Workday Slug Overrides
# ==============================================================================

TARGET_URLS = {
    "Travelers": "https://travelers.wd5.myworkdayjobs.com/en-US/External",
    "CVS Health": "https://cvshealth.wd1.myworkdayjobs.com/en-US/CVS_Health_Careers",
    "RTX": "https://globalhr.wd5.myworkdayjobs.com/en-US/rec_rtx_ext_gateway",
    "CrowdStrike": "https://crowdstrike.wd5.myworkdayjobs.com/en-US/crowdstrikecareers",
    "Voya": "https://godirect.wd5.myworkdayjobs.com/en-US/voya_jobs",
    "Zscaler": "https://boards.greenhouse.io/zscaler",
    "Tanium": "https://boards.greenhouse.io/tanium",
    "Censys": "https://boards.greenhouse.io/censys",
    "The Hartford": "https://thehartford.wd5.myworkdayjobs.com/TheHartfordCareers",
    "MassMutual": "https://massmutual.wd1.myworkdayjobs.com/MassMutualCareers",
    "BNSF": "https://bnsf.wd1.myworkdayjobs.com/BNSFCareers",
    "Eversource": "https://eversource.wd1.myworkdayjobs.com/External_Career_Site",
    "Barracuda": "https://barracuda.wd1.myworkdayjobs.com/BarracudaCareers",
    "Wells Fargo": "https://wf.wd1.myworkdayjobs.com/WellsFargoJobs",
    "COCC": "https://www.cocc.com/careers/cocc-client-job-opportunities/",
    "AARP": "https://apply.aarp.org",
    "Hanover Insurance": "https://jobs.dayforcehcm.com/en-US/thg/ALLCAREERS",
    "Liberty Bank": "https://libertybankct.com/about-us/careers",
    "GuidePoint Security": "https://www.guidepointsecurity.com/careers/",
    "Hartford HealthCare": "https://www.hhccareers.org/",
    "Cigna": "https://cigna.wd5.myworkdayjobs.com/cignacareers",
    "Stanley Black & Decker": "https://sbdinc.wd1.myworkdayjobs.com/en-US/Stanley_Black_Decker_Career_Site",
    "State of CT (DAS)": "https://www.jobapscloud.com/ct/",
}

WORKDAY_SLUG_OVERRIDES = {
    "The Hartford": ["TheHartfordCareers", "TheHartford", "Careers"],
    "MassMutual": ["MassMutualCareers", "MassMutual", "Careers"],
    "BNSF": ["BNSFCareers", "BNSF"],
    "Eversource": ["External_Career_Site", "EversourceCareers"],
    "Travelers": ["External", "TravelersCareers"],
    "CVS Health": ["CVS_Health_Careers", "CVSHealth"],
    "RTX": ["rec_rtx_ext_gateway", "RTXCareers"],
    "CrowdStrike": ["crowdstrikecareers"],
    "Voya": ["voya_jobs"],
    "Cigna": ["cignacareers"],
    "Stanley Black & Decker": ["Stanley_Black_Decker_Career_Site"],
    "Wells Fargo": ["WellsFargoJobs"],
    "Barracuda": ["BarracudaCareers"],
}


# ==============================================================================
# Logging Configuration
# ==============================================================================

LOG_FILE = os.path.join(COMPANIES_DIR, "scraper_run.log")

logger = logging.getLogger("job_scraper")
logger.setLevel(logging.DEBUG if VERBOSE_DEBUG else logging.INFO)
logger.propagate = False

if not logger.handlers:
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=2_000_000,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    )
    logger.addHandler(file_handler)


# ==============================================================================
# Core Utility Functions
# ==============================================================================

def utc_now():
    """Returns current UTC ISO-formatted timestamp string."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def today_string():
    """Returns current local date in YYYY-MM-DD format."""
    return datetime.now().date().isoformat()

def normalize_text(value):
    """Cleans whitespace from strings and handles null values safely."""
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()

def normalize_date(value):
    """Parses various date formats into standardized YYYY-MM-DD strings."""
    if not value:
        return None
    value = str(value).strip()
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(value, fmt).date().isoformat()
        except ValueError:
            continue
    try:
        return parsedate_to_datetime(value).date().isoformat()
    except (TypeError, ValueError, OverflowError):
        return None

def canonical_url(url):
    """Strips tracking parameters and normalizes URLs for duplicate detection."""
    if not url:
        return ""
    try:
        parsed = urlparse(url.strip())
        if parsed.scheme.lower() not in ("http", "https") or not parsed.hostname:
            return ""
        scheme = parsed.scheme.lower()
        hostname = parsed.hostname.lower()
        if parsed.port:
            default_port = (
                (scheme == "http" and parsed.port == 80)
                or (scheme == "https" and parsed.port == 443)
            )
            if not default_port:
                hostname = f"{hostname}:{parsed.port}"
        path = parsed.path.rstrip("/") or "/"
        tracking_prefixes = ("utm_", "pk_")
        tracking_names = {"fbclid", "gclid", "mc_cid", "mc_eid", "ref", "source"}
        query_items = []
        for key, value in parse_qsl(parsed.query, keep_blank_values=True):
            key_lower = key.lower()
            if key_lower in tracking_names or key_lower.startswith(tracking_prefixes):
                continue
            query_items.append((key, value))
        return urlunparse((scheme, hostname, path, "", urlencode(query_items, doseq=True), ""))
    except (ValueError, TypeError):
        return ""

def resolve_job_url(base_url, href):
    """Resolves relative job listing hrefs against the base career portal URL."""
    if not href:
        return ""
    try:
        resolved = urljoin(base_url, str(href).strip())
        parsed = urlparse(resolved)
        if parsed.scheme.lower() not in ("http", "https") or not parsed.hostname:
            return ""
        return resolved
    except (ValueError, TypeError):
        return ""

def detect_platform(url):
    """Inspects target URL domain to determine scraper dispatch handler."""
    domain = urlparse(url).netloc.lower()
    if "greenhouse.io" in domain:
        return "greenhouse"
    if "lever.co" in domain:
        return "lever"
    if "myworkdayjobs.com" in domain:
        return "workday"
    if "apply." in domain or "phenompeople" in domain or "csod.com" in domain:
        return "phenom"
    if "dayforcehcm.com" in domain:
        return "dayforce"
    if "cocc.com" in domain:
        return "cocc"
    return "custom"

def evaluate_job_relevance(title, description=""):
    """Evaluates job title and description against exclusion lists and target keywords."""
    title_norm = normalize_text(title).lower()
    desc_norm = normalize_text(description).lower()

    if not title_norm:
        return False, "missing_title"

    for term in EXCLUDED_TITLE_TERMS:
        if term in title_norm:
            return False, f"excluded_title_term:{term}"

    combined = f"{title_norm} {desc_norm}"

    if any(term in title_norm for term in SECURITY_TITLE_TERMS):
        return True, "matched_security_title"

    if any(kw.lower() in title_norm for kw in KEYWORDS):
        return True, "matched_title_keyword"

    if ALLOW_DESCRIPTION_MATCH and desc_norm:
        if any(kw.lower() in combined for kw in KEYWORDS):
            return True, "matched_description_keyword"
        if any(term in desc_norm for term in SECURITY_TITLE_TERMS):
            return True, "matched_description_security_term"
        return False, "failed_description_criteria"

    return False, "failed_title_criteria"

def should_keep_job(title, description=""):
    """Boolean wrapper for job relevance evaluation."""
    kept, _ = evaluate_job_relevance(title, description)
    return kept

def get_job_identity(job):
    """Generates a unique composite key for duplicate tracking."""
    company = normalize_text(job.get("company", "")).lower()
    job_id = normalize_text(job.get("job_id", ""))
    if job_id:
        return f"{company}|id:{job_id.lower()}"
    link = canonical_url(job.get("link", ""))
    if link:
        return f"{company}|url:{link}"
    title = normalize_text(job.get("title", "")).lower()
    return f"{company}|title:{title}"

def normalize_job(company_name, platform, item):
    """Maps raw platform job payloads into standard dictionary structure."""
    if not isinstance(item, dict):
        return None
    title = normalize_text(item.get("title") or item.get("JobTitle"))
    if not title:
        return None
    raw_url = item.get("link") or item.get("url") or item.get("absolute_url") or ""
    link = resolve_job_url(TARGET_URLS.get(company_name, ""), raw_url) if raw_url else ""
    description = normalize_text(item.get("description", "") or item.get("content", ""))
    job_id = normalize_text(item.get("job_id") or item.get("jobId") or item.get("jobPostingId") or item.get("id") or "")
    posted_date = normalize_date(item.get("posted_date") or item.get("postedOn") or item.get("postedDate") or item.get("updated_at"))
    
    raw_data = {str(k): v for k, v in item.items()}

    return {
        "company": company_name,
        "title": title,
        "job_id": job_id,
        "platform": platform,
        "link": link,
        "description": description[:MAX_DESCRIPTION_LENGTH],
        "posted_date": posted_date,
        "status": "active",
        "raw_data": raw_data,
    }

def deduplicate_jobs(jobs):
    """Deduplicates a list of job dictionaries, retaining the most detailed records."""
    unique = {}
    missing_counter = 0
    for job in jobs:
        if not job:
            continue
        identity = get_job_identity(job)
        if identity.endswith("|title:"):
            missing_counter += 1
            identity += f"|invalid:{missing_counter}"
        if identity not in unique:
            unique[identity] = job
        elif len(job.get("description", "")) > len(unique[identity].get("description", "")):
            unique[identity] = job
    return list(unique.values())


# ==============================================================================
# Historical JSON Storage Functions
# ==============================================================================

def load_existing_jobs(filepath, company_name):
    """Loads rolling job history from company JSON files."""
    json_path = filepath.rsplit(".", 1)[0] + ".json"
    if not os.path.exists(json_path):
        md_path = filepath.rsplit(".", 1)[0] + ".md"
        if os.path.exists(md_path):
            try:
                os.remove(md_path)
            except OSError:
                pass
        return []

    try:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except Exception as exc:
        logger.error("%s: unable to read json history file: %s", company_name, exc)
    return []

def record_is_within_retention(job, today):
    """Evaluates whether a job record falls within the maximum age retention window."""
    date_value = job.get("last_seen") or job.get("first_seen") or job.get("captured")
    record_date = normalize_date(date_value)
    if not record_date:
        return True
    parsed_date = datetime.strptime(record_date, "%Y-%m-%d").date()
    age_days = (today - parsed_date).days
    if age_days < 0:
        return True
    return age_days <= MAX_AGE_DAYS

def save_jobs(company_name, jobs):
    """Saves active jobs to JSON history atomically, enforcing retention limits."""
    filepath = os.path.join(COMPANIES_DIR, f"{company_name}.json")
    today = datetime.now().date()
    active_jobs = [job for job in jobs if record_is_within_retention(job, today)]
    temp_filepath = filepath + ".tmp"
    try:
        with open(temp_filepath, "w", encoding="utf-8") as file:
            json.dump(active_jobs, file, indent=2, ensure_ascii=False)
        os.replace(temp_filepath, filepath)
    except OSError as exc:
        logger.error("%s: failed to save json history: %s", company_name, exc)
        try:
            if os.path.exists(temp_filepath):
                os.remove(temp_filepath)
        except OSError:
            pass
        raise
    return len(active_jobs)


# ==============================================================================
# HTTP Helpers & Scraping Handlers (Greenhouse, Workday, etc.)
# ==============================================================================

def create_http_session():
    """Creates a curl_cffi HTTP session impersonating Chrome for browser parity."""
    return cffi_requests.Session(
        impersonate="chrome",
        timeout=REQUEST_TIMEOUT,
    )

def get_json_response(response):
    """Safely extracts JSON dictionary payloads from HTTP responses."""
    if response is None:
        return None
    try:
        data = response.json()
    except (ValueError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None

def fetch_page_with_scrapling(url):
    """Fetches complex HTML pages using Scrapling StealthyFetcher."""
    try:
        fetcher = StealthyFetcher()
        response = fetcher.fetch(url, headless=True)
        if response.status != 200:
            logger.warning("Scrapling returned HTTP %s for %s", response.status, url)
            return None
        return response
    except Exception:
        logger.exception("Scrapling request failed for %s", url)
        return None

def extract_anchor_jobs(response, base_url, description):
    """Extracts job candidates from HTML anchor links as a fallback scraper."""
    jobs = []
    for link_element in response.css("a"):
        title = normalize_text(link_element.text)
        href = link_element.attrib.get("href", "")
        if not title or len(title) < 7:
            continue
        job_url = resolve_job_url(base_url, href)
        if not job_url:
            continue
        jobs.append({
            "title": title,
            "link": job_url,
            "description": description,
        })
    return deduplicate_jobs(jobs)


# ==============================================================================
# Greenhouse API Handler
# ==============================================================================

def scrape_greenhouse(company_name, url):
    """Scrapes jobs from Greenhouse job board JSON APIs."""
    board_token = urlparse(url).path.rstrip("/").split("/")[-1]
    if not board_token:
        raise ValueError(f"{company_name}: could not determine Greenhouse board token")

    api_url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs"
    session = create_http_session()
    jobs = []
    seen_ids = set()

    try:
        response = session.get(api_url, params={"content": "true"})
        if response.status_code != 200:
            raise RuntimeError(f"Greenhouse returned HTTP {response.status_code} for {api_url}")

        data = get_json_response(response)
        if data is None or not isinstance(data.get("jobs"), list):
            raise ValueError(f"Invalid Greenhouse API response structure for {api_url}")

        for item in data["jobs"]:
            job_id = str(item.get("id", "")).strip()
            if job_id and job_id in seen_ids:
                continue
            if job_id:
                seen_ids.add(job_id)
            jobs.append(item)
    finally:
        session.close()

    return deduplicate_jobs(jobs)


# ==============================================================================
# Workday API Handler with Subdomain Probing
# ==============================================================================

def scrape_workday(company_name, url):
    """Discovers CXS API endpoints and collects postings from Workday career sites."""
    parsed = urlparse(url)
    base_netloc = parsed.netloc
    tenant = base_netloc.split(".")[0]
    path_parts = [part for part in parsed.path.split("/") if part]
    site_name = path_parts[-1] if path_parts else company_name.replace(" ", "")

    session = create_http_session()
    endpoints = []

    def add_endpoint(netloc, tenant_id, site, language=None, external=False):
        if not site or not tenant_id:
            return
        if external:
            path = f"/wday/cxs/{tenant_id}/external/{site}/jobs"
        elif language:
            path = f"/wday/cxs/{tenant_id}/{language}/{site}/jobs"
        else:
            path = f"/wday/cxs/{tenant_id}/{site}/jobs"
        endpoint = f"https://{netloc}{path}"
        if endpoint not in endpoints:
            endpoints.append(endpoint)

    subdomain_candidates = [base_netloc]
    for sub in ("wd1", "wd2", "wd3", "wd4", "wd5", "wd10", "wd12"):
        if tenant:
            candidate_netloc = f"{tenant}.{sub}.myworkdayjobs.com"
            if candidate_netloc not in subdomain_candidates:
                subdomain_candidates.append(candidate_netloc)

    for netloc in subdomain_candidates:
        t = netloc.split(".")[0]
        for override_site in WORKDAY_SLUG_OVERRIDES.get(company_name, []):
            add_endpoint(netloc, t, override_site)
            add_endpoint(netloc, t, override_site, language="en-US")
            add_endpoint(netloc, t, override_site, external=True)

        base_sites = {
            site_name,
            site_name.lower(),
            company_name.replace(" ", ""),
            company_name.replace(" ", "").lower(),
            company_name.replace("&", "").replace(" ", ""),
        }
        for candidate_site in base_sites:
            add_endpoint(netloc, t, candidate_site)
            add_endpoint(netloc, t, candidate_site, language="en-US")
            add_endpoint(netloc, t, candidate_site, external=True)

        add_endpoint(netloc, t, "external")

    try:
        page_response = session.get(url)
        if page_response.status_code == 200:
            matches = re.findall(r"/wday/cxs/([^/\"?]+)/([^/\"?]+)", page_response.text)
            for discovered_tenant, discovered_site in matches:
                for netloc in subdomain_candidates:
                    add_endpoint(netloc, discovered_tenant, discovered_site)
                    add_endpoint(netloc, discovered_tenant, discovered_site, language="en-US")
                    add_endpoint(netloc, discovered_tenant, discovered_site, external=True)
    except Exception:
        logger.debug("%s: unable to inspect Workday landing page", company_name, exc_info=True)

    endpoints = endpoints[:80]
    selected_endpoint = None
    first_payload = None
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    try:
        for api_url in endpoints:
            payload = {
                "appliedFacets": {},
                "limit": WORKDAY_PAGE_SIZE,
                "offset": 0,
                "searchText": "",
                "sortBy": "postedOnDesc",
            }
            try:
                response = session.post(api_url, json=payload, headers=headers)
                if response.status_code != 200:
                    continue
                data = get_json_response(response)
                if (
                    isinstance(data, dict)
                    and isinstance(data.get("jobPostings"), list)
                    and len(data.get("jobPostings")) > 0
                ):
                    selected_endpoint = api_url
                    first_payload = data
                    break
            except Exception:
                logger.debug("%s: Workday endpoint attempt failed: %s", company_name, api_url, exc_info=True)

        if not selected_endpoint:
            raise RuntimeError(f"{company_name}: No valid Workday API endpoint found returning active job postings.")

        raw_items = []
        seen_ids = set()
        first_postings = first_payload.get("jobPostings", [])
        parsed_selected = urlparse(selected_endpoint)
        selected_origin = f"{parsed_selected.scheme}://{parsed_selected.netloc}"
        selected_parts = [p for p in parsed_selected.path.split("/") if p]
        selected_tenant = selected_parts[2] if len(selected_parts) > 2 else tenant
        selected_site = selected_parts[3] if len(selected_parts) > 3 else site_name

        for page_number in range(WORKDAY_MAX_PAGES):
            if page_number == 0:
                data = first_payload
            else:
                payload = {
                    "appliedFacets": {},
                    "limit": WORKDAY_PAGE_SIZE,
                    "offset": page_number * WORKDAY_PAGE_SIZE,
                    "searchText": "",
                    "sortBy": "postedOnDesc",
                }
                response = session.post(selected_endpoint, json=payload, headers=headers)
                if response.status_code != 200:
                    logger.warning("%s: Workday pagination stopped at page %s after HTTP %s", company_name, page_number + 1, response.status_code)
                    break
                data = get_json_response(response)
                if data is None or not isinstance(data.get("jobPostings"), list):
                    break

            postings = data.get("jobPostings", [])
            if not postings:
                break

            page_added = 0
            for item in postings:
                if not isinstance(item, dict):
                    continue
                job_id = str(item.get("externalPath") or item.get("jobPostingId") or item.get("id") or "").strip()
                if job_id and job_id in seen_ids:
                    continue
                if job_id:
                    seen_ids.add(job_id)

                external_path = item.get("externalPath")
                if external_path and not item.get("link"):
                    item["link"] = urljoin(selected_origin, external_path)

                raw_items.append(item)
                page_added += 1

            if page_added == 0:
                break

            total = data.get("total")
            if isinstance(total, int):
                next_offset = (page_number + 1) * WORKDAY_PAGE_SIZE
                if next_offset >= total:
                    break
            if len(postings) < WORKDAY_PAGE_SIZE:
                break

        if raw_items:
            session_desc = create_http_session()
            for item in raw_items:
                ext_path = item.get("externalPath")
                if ext_path and not item.get("description"):
                    detail_url = f"{selected_origin}/wday/cxs/{selected_tenant}/{selected_site}{ext_path}"
                    try:
                        detail_resp = session_desc.get(detail_url)
                        if detail_resp.status_code == 200:
                            detail_data = get_json_response(detail_resp)
                            if detail_data and "jobPostingInfo" in detail_data:
                                info = detail_data["jobPostingInfo"]
                                item["description"] = info.get("jobDescription", "")
                    except Exception:
                        pass
                time.sleep(0.2)
            session_desc.close()

            return deduplicate_jobs(raw_items)

    finally:
        session.close()

    captured_items = []
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
            page = context.new_page()

            def handle_response(response):
                if "/wday/cxs/" not in response.url or "/jobs" not in response.url or response.status != 200:
                    return
                try:
                    data = response.json()
                    postings = data.get("jobPostings", [])
                    if not isinstance(postings, list):
                        return
                    for item in postings:
                        if not isinstance(item, dict):
                            continue
                        external_path = item.get("externalPath")
                        if external_path and not item.get("link"):
                            item["link"] = urljoin(base_netloc, external_path)
                        captured_items.append(item)
                except Exception:
                    pass

            page.on("response", handle_response)
            page.goto(url, timeout=BROWSER_TIMEOUT_MS, wait_until="domcontentloaded")
            page.wait_for_timeout(BROWSER_WAIT_MS)
            context.close()
            browser.close()
    except Exception:
        logger.exception("%s: Workday browser fallback failed", company_name)

    return deduplicate_jobs(captured_items)


# ==============================================================================
# Phenom, Dayforce, COCC & Generic Handlers
# ==============================================================================

def scrape_phenom(company_name, url):
    """Scrapes jobs from Phenom People career sites via API or HTML fallback."""
    parsed = urlparse(url)
    api_url = f"{parsed.scheme}://{parsed.netloc}/api/v1/jobs?limit=50&sortBy=relevance"
    session = create_http_session()
    try:
        response = session.get(api_url, headers={"Accept": "application/json"})
        if response.status_code == 200:
            data = get_json_response(response)
            if isinstance(data, dict) and isinstance(data.get("jobs"), list):
                raw_items = []
                for item in data["jobs"]:
                    if not isinstance(item, dict):
                        continue
                    job_data = item.get("job", item)
                    if not isinstance(job_data, dict):
                        continue
                    raw_items.append(job_data)
                return deduplicate_jobs(raw_items)
    finally:
        session.close()

    response = fetch_page_with_scrapling(url)
    if response is None:
        return []
    return extract_anchor_jobs(response, url, "Description unavailable from Phenom fallback.")

def scrape_dayforce(company_name, url):
    """Scrapes jobs from Dayforce HCM career sites."""
    parsed = urlparse(url)
    path_parts = [part for part in parsed.path.split("/") if part]
    if len(path_parts) < 2:
        return []
    client_code = path_parts[1].lower()
    api_url = f"{parsed.scheme}://{parsed.netloc}/api/v1/jobs"
    session = create_http_session()
    try:
        response = session.get(api_url, params={"clientCode": client_code, "country": "US", "limit": 100}, headers={"Accept": "application/json"})
        if response.status_code == 200:
            data = get_json_response(response)
            if isinstance(data, dict) and isinstance(data.get("Jobs"), list):
                return deduplicate_jobs(data["Jobs"])
    finally:
        session.close()

    response = fetch_page_with_scrapling(url)
    if response is None:
        return []
    return extract_anchor_jobs(response, url, "Description unavailable from Dayforce fallback.")

def scrape_cocc(company_name, url):
    """Scrapes customized career pages for COCC."""
    response = fetch_page_with_scrapling(url)
    if response is None:
        return []
    items = []
    for element in response.css("a"):
        title = normalize_text(element.text)
        href = element.attrib.get("href", "")
        if not title or len(title) < 6:
            continue
        if not any(term in href.lower() for term in ("job", "career", "employment")):
            continue
        link = resolve_job_url(url, href)
        if not link:
            continue
        items.append({
            "title": title,
            "link": link,
            "description": "Description unavailable from COCC listing page.",
        })
    return deduplicate_jobs(items)

def scrape_generic(company_name, url):
    """Generic scraper fallback extracting job anchor links from HTML pages."""
    response = fetch_page_with_scrapling(url)
    if response is None:
        return []
    return extract_anchor_jobs(response, url, "Description unavailable from generic listing fallback.")


# ==============================================================================
# Platform Dispatch & Company Processing with Telemetry
# ==============================================================================

def scrape_company_platform(company_name, url, platform):
    """Routes company scraping requests to the appropriate platform handler."""
    handlers = {
        "greenhouse": scrape_greenhouse,
        "workday": scrape_workday,
        "phenom": scrape_phenom,
        "dayforce": scrape_dayforce,
        "cocc": scrape_cocc,
        "custom": scrape_generic,
    }
    handler = handlers.get(platform, scrape_generic)
    return handler(company_name, url)

def scrape_company(company_name, url):
    """Orchestrates collection, normalization, filtering, and history updates for a company."""
    started = time.monotonic()
    platform = detect_platform(url)
    filepath = os.path.join(COMPANIES_DIR, f"{company_name}.json")

    print(f"{C.CYAN}[+] Scraping {C.BOLD}{company_name}{C.RESET}{C.CYAN} via {platform}...{C.RESET}")
    logger.info("Starting collection: company=%s platform=%s url=%s", company_name, platform, url)

    existing_jobs = load_existing_jobs(filepath, company_name)
    existing_by_identity = {}
    for job in existing_jobs:
        identity = get_job_identity(job)
        if identity not in existing_by_identity:
            existing_by_identity[identity] = job
        elif len(job.get("description", "")) > len(existing_by_identity[identity].get("description", "")):
            existing_by_identity[identity] = job

    try:
        raw_items = scrape_company_platform(company_name, url, platform)
    except Exception as exc:
        logger.exception("%s: collection failed due to exception: %s", company_name, exc)
        elapsed = time.monotonic() - started
        print(f"{C.RED}[!] Collection failed for {company_name}: {exc}. Existing history preserved.{C.RESET}\n")
        return {
            "company": company_name,
            "platform": platform,
            "new": 0,
            "updated": 0,
            "active": len(existing_jobs),
            "returned": 0,
            "filtered": 0,
            "status": "FAILED",
            "duration_seconds": round(elapsed, 2),
        }

    if raw_items is None:
        raw_items = []

    normalized_items = []
    for item in raw_items:
        normalized = normalize_job(company_name, platform, item)
        if normalized:
            normalized_items.append(normalized)

    normalized_items = deduplicate_jobs(normalized_items)

    filtered_items = []
    exclusion_counts = {}
    for item in normalized_items:
        kept, reason = evaluate_job_relevance(item.get("title", ""), item.get("description", ""))
        if kept:
            filtered_items.append(item)
        else:
            exclusion_counts[reason] = exclusion_counts.get(reason, 0) + 1

    if exclusion_counts:
        logger.debug("%s: filtering exclusions breakdown: %s", company_name, exclusion_counts)

    today = today_string()
    new_count = 0
    updated_count = 0

    for item in filtered_items:
        identity = get_job_identity(item)
        existing = existing_by_identity.get(identity)
        if existing:
            existing["last_seen"] = today
            existing["status"] = "active"
            existing["raw_data"] = item["raw_data"]
            for field in ("job_id", "link", "description", "posted_date", "platform"):
                if item.get(field):
                    existing[field] = item[field]
            if item.get("title"):
                existing["title"] = item["title"]
            updated_count += 1
        else:
            item["first_seen"] = today
            item["last_seen"] = today
            item["captured"] = today
            item["status"] = "active"
            existing_by_identity[identity] = item
            new_count += 1

    combined_jobs = list(existing_by_identity.values())

    try:
        total_active = save_jobs(company_name, combined_jobs)
    except Exception:
        logger.exception("%s: history save failed", company_name)
        return {
            "company": company_name,
            "platform": platform,
            "new": new_count,
            "updated": updated_count,
            "active": len(existing_jobs),
            "returned": len(normalized_items),
            "filtered": len(filtered_items),
            "status": "FAILED",
            "duration_seconds": round(time.monotonic() - started, 2),
        }

    if not normalized_items:
        status = "SUCCESS_EMPTY"
    elif not filtered_items:
        status = "SUCCESS_NO_MATCHES"
    else:
        status = "SUCCESS"

    elapsed = time.monotonic() - started
    logger.info(
        "%s: status=%s returned=%s filtered=%s new=%s updated=%s retained=%s duration=%.2fs",
        company_name, status, len(normalized_items), len(filtered_items), new_count, updated_count, total_active, elapsed,
    )

    print(f"{C.GREEN}[✓] Done. New: {new_count} | Updated: {updated_count} | History: {total_active} | Status: {status}{C.RESET}\n")
    time.sleep(random.uniform(MIN_REQUEST_DELAY, MAX_REQUEST_DELAY))

    return {
        "company": company_name,
        "platform": platform,
        "new": new_count,
        "updated": updated_count,
        "active": total_active,
        "returned": len(normalized_items),
        "filtered": len(filtered_items),
        "status": status,
        "duration_seconds": round(elapsed, 2),
    }


# ==============================================================================
# Main Execution Loop & Reporting
# ==============================================================================

def main():
    """Main execution entry point coordinating scrapers, summary reporting, and logging."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print(f"{C.BOLD}{C.GREEN}" + "=" * 75 + f"{C.RESET}")
    print(f"{C.BOLD}{C.CYAN}JOB SCRAPER v{VERSION} STARTING{C.RESET}")
    print(f"Target Sites: {len(TARGET_URLS)}")
    print(f"Keywords: {KEYWORDS}")
    print(f"Security Title Terms: {len(SECURITY_TITLE_TERMS)}")
    print(f"Maximum History Age: {MAX_AGE_DAYS} days")
    print(f"Workday Page Size: {WORKDAY_PAGE_SIZE}")
    print(f"Workday Maximum Pages: {WORKDAY_MAX_PAGES}")
    print(f"{C.BOLD}{C.GREEN}" + "=" * 75 + f"{C.RESET}\n")

    run_started = utc_now()
    logger.info("Run started: version=%s targets=%s", VERSION, len(TARGET_URLS))

    summary_stats = {}
    for name, target_url in TARGET_URLS.items():
        try:
            result = scrape_company(name, target_url)
        except Exception:
            logger.exception("%s: uncaught company processing error", name)
            result = {
                "company": name,
                "platform": detect_platform(target_url),
                "new": 0,
                "updated": 0,
                "active": 0,
                "returned": 0,
                "filtered": 0,
                "status": "FAILED",
                "duration_seconds": 0,
            }
        summary_stats[name] = result

    total_new = sum(item["new"] for item in summary_stats.values())
    total_updated = sum(item["updated"] for item in summary_stats.values())
    total_returned = sum(item["returned"] for item in summary_stats.values())
    total_filtered = sum(item["filtered"] for item in summary_stats.values())
    successful_runs = sum(item["status"] in ("SUCCESS", "SUCCESS_EMPTY", "SUCCESS_NO_MATCHES") for item in summary_stats.values())
    failed_runs = sum(item["status"] == "FAILED" for item in summary_stats.values())

    print(f"\n{C.BOLD}{C.GREEN}" + "=" * 75 + f"{C.RESET}")
    print(f"{C.BOLD}{C.CYAN}SCRAPE RUN COMPLETE — SUMMARY STATS{C.RESET}")
    print(f"{C.BOLD}{C.GREEN}" + "=" * 75 + f"{C.RESET}")
    print(f"New Roles: {C.BOLD}{C.GREEN}{total_new}{C.RESET}")
    print(f"Updated Existing Roles: {total_updated}")
    print(f"Collected Candidates: {total_returned}")
    print(f"Candidates Passing Filter: {total_filtered}")
    print(f"Successful Company Runs: {successful_runs}")
    print(f"Failed Company Runs: {failed_runs}")
    print("-" * 100)
    print(f"{'Company':<24} | {'New':<5} | {'Updated':<7} | {'History':<7} | {'Status':<20}")
    print("-" * 100)

    for name, stats in summary_stats.items():
        status = stats["status"]
        if status == "FAILED":
            status_color = C.RED
        elif status in ("SUCCESS_EMPTY", "SUCCESS_NO_MATCHES"):
            status_color = C.YELLOW
        else:
            status_color = C.GREEN

        print(
            f"{name[:24]:<24} | "
            f"{stats['new']:<5} | "
            f"{stats['updated']:<7} | "
            f"{stats['active']:<7} | "
            f"{status_color}{status:<20}{C.RESET}"
        )

    print(f"{C.BOLD}{C.GREEN}" + "=" * 100 + f"{C.RESET}\n")

    run_completed = utc_now()
    logger.info(
        "Run completed: new=%s updated=%s returned=%s filtered=%s successful=%s failed=%s",
        total_new, total_updated, total_returned, total_filtered, successful_runs, failed_runs,
    )

    summary_json = os.path.join(COMPANIES_DIR, "scraper_run_summary.json")
    summary_payload = {
        "version": VERSION,
        "started_at": run_started,
        "completed_at": run_completed,
        "totals": {
            "new": total_new,
            "updated": total_updated,
            "returned": total_returned,
            "filtered": total_filtered,
            "successful_companies": successful_runs,
            "failed_companies": failed_runs,
        },
        "companies": summary_stats,
    }

    try:
        with open(summary_json, "w", encoding="utf-8") as file:
            json.dump(summary_payload, file, indent=2, ensure_ascii=False)
        print(f"{C.CYAN}[-] JSON summary written to {summary_json}{C.RESET}")
    except OSError:
        logger.exception("Failed to write JSON summary")

    print(f"{C.CYAN}[-] Diagnostic log: {LOG_FILE}{C.RESET}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("Run interrupted by user.")
        print(f"\n{C.YELLOW}[!] Run interrupted by user.{C.RESET}")
        sys.exit(130)
    except Exception:
        logger.exception("Fatal application error")
        print(f"{C.RED}[!] Fatal application error. Check the diagnostic log.{C.RESET}")
        sys.exit(1)