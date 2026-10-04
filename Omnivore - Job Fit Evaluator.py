# ==============================================================================
# Project Name: Job Fit Evaluator API Runner (Local Ollama Version - Omnivore)
# Author: Scott Malin, CISSP
# Version: 1.6.0
# Purpose: Reads scraped company markdown reports, loops through jobs, 
#          sends the job details and master skills summary to the local Ollama LLM 
#          using the evaluation prompt, saves results, supports resume/pause,
#          and emails a summary of new evaluations.
#
# Changelog:
#    - 2026-09-30: Switched OpenAI client to local Ollama base URL.
#    - 2026-09-30: Pointed resume path to candidate skills summary markdown.
#    - 2026-09-30: Added prerequisite checks for openai library.
#    - 2026-10-02: Added multi-company batch scanning and active ETA progress tracker.
#    - 2026-10-02: Added state tracking for graceful pausing/resuming, cls, and color.
#    - 2026-10-02: Added automated SMTP email notification for newly processed jobs.
#    - 2026-10-04: Removed personal paths, added beginner documentation, LLM context 
#                  notes, and integrated the evaluation prompt documentation link.
#
# NOTE FOR LLMS & BEGINNERS:
# This script takes scraped job listings, pairs them with your master skills 
# summary and evaluation prompt, and sends them to a local AI (Ollama) to 
# analyze how well you fit each role. If you run into errors or want to change 
# how it behaves, you can paste this entire script into an AI assistant along 
# with your error message, and it will help you fix or adjust it.
#
# NOTE ABOUT PERFORMANCE:
# This uses Ollama a local LLM to process the job fit evaluation, it really can hit your system hard
# Expect your CPU to max out when it is running
# ==============================================================================

import os
import sys
import time
import json
import smtplib
import importlib.util
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Enable ANSI escape sequences on Windows terminals so colors render properly
if os.name == 'nt':
    os.system('')

# ==============================================================================
# Prerequisite Checks
# Automatically checks if required third-party libraries are installed. If any 
# are missing, it stops the script and gives you the exact pip command to fix it.
# ==============================================================================
REQUIRED_MODULES = ["openai"]
MISSING_DEPS = [mod for mod in REQUIRED_MODULES if importlib.util.find_spec(mod) is None]

if MISSING_DEPS:
    print("=" * 60)
    print("[!] ERROR: Missing required Python packages.")
    print(f"    Missing: {', '.join(MISSING_DEPS)}")
    print("\n[-] Run this command in your terminal to install them:")
    print("    pip install openai")
    print("=" * 60)
    sys.exit(1)

from openai import OpenAI

# Connects the OpenAI library to a local Ollama instance running on your machine.
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" # Required by the client library, but value doesn't matter for local Ollama
)

# Directory configurations
COMPANIES_DIR = "company_files"
OUTPUT_DIR = "evaluation_reports"
STATE_FILE = "eval_progress.json"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Path to your master skills summary document used for evaluating job fit.
# Update this path to point to your local skills summary markdown file.
RESUME_PATH = r"C:\Path\To\Your\Skills_Summary.md"

# SMTP Mail Server Configuration (Update these details to receive email alerts)
SMTP_SERVER  = "smtp.gmail.com"
SMTP_PORT    = 587
MAIL_FROM    = "your_email@gmail.com"
MAIL_TO      = "your_email@gmail.com"
APP_PASSWORD = "your_email_app_password"

# ANSI Color Codes for terminal highlighting
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def load_resume():
    """Reads and returns the candidate's master skills summary text from disk."""
    if os.path.exists(RESUME_PATH):
        with open(RESUME_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "[ERROR: Skills summary file not found on disk.]"

def load_evaluation_prompt():
    """
    Loads the evaluation prompt logic. 
    Note: You can download the required prompt template from:
    https://github.com/scottmalin68-commits/Job-Search-Career-Prompts/blob/main/Universal%20Job%20Fit%20Evaluation%20Prompt%20-%20API%20Call.md
    """
    prompt_path = "Universal Job Fit Evaluation Prompt - API Call.md"
    if os.path.exists(prompt_path):
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def parse_markdown_report(filepath):
    """Parses a company's markdown report file to extract individual job listings."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    jobs = []
    sections = content.split("---")
    for sec in sections:
        if "Title:" in sec:
            job = {}
            for line in sec.strip().split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    job[key.strip().lower()] = val.strip()
            if "title" in job:
                jobs.append(job)
    return jobs

def load_state():
    """Loads the progress state file so the script can resume where it left off if interrupted."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_state(completed_list):
    """Saves the current progress state to disk."""
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(completed_list, f, indent=2)

def send_notification_email(new_evaluations_count, summary_lines):
    """Sends an email summary notification containing newly processed job evaluations."""
    if new_evaluations_count == 0:
        return

    print(f"{CYAN}[*] Sending email notification for {new_evaluations_count} new job evaluations...{RESET}")
    try:
        subject = f"JOB ALERT: {new_evaluations_count} New Roles Evaluated"
        body = "Here are the newly processed job evaluations from your run:\n\n" + "\n".join(summary_lines)

        msg = MIMEMultipart()
        msg['From'] = MAIL_FROM
        msg['To'] = MAIL_TO
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtp.starttls()
        smtp.login(MAIL_FROM, APP_PASSWORD)
        smtp.sendmail(MAIL_FROM, MAIL_TO, msg.as_string())
        smtp.quit()
        print(f"{GREEN}[✓] Notification email sent successfully.{RESET}")
    except Exception as e:
        print(f"{YELLOW}[!] Failed to send email notification: {e}{RESET}")

def evaluate_job(company_name, job, eval_prompt, resume_text):
    """Sends the candidate summary, evaluation instructions, and job description to local Ollama."""
    user_content = f"""
## Candidate Master Skills & Experience Summary:
{resume_text}

## Evaluation Instructions / Prompt:
{eval_prompt}

## Job Posting to Evaluate:
Title: {job.get('title')}
Company: {company_name}
Link: {job.get('link')}
Description:
{job.get('description')}
"""

    response = client.chat.completions.create(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are an expert technical recruiter and career advisor evaluating job fit accurately and critically based on the provided candidate summary."},
            {"role": "user", "content": user_content}
        ],
        temperature=0.2
    )
    
    return response.choices[0].message.content

def run_all_evaluations():
    """Main execution loop that manages batch scanning, progress tracking, evaluation, and reporting."""
    os.system('cls' if os.name == 'nt' else 'clear')

    if not os.path.exists(COMPANIES_DIR):
        print(f"[!] Directory not found: {COMPANIES_DIR}")
        return

    company_files = [f for f in os.listdir(COMPANIES_DIR) if f.endswith(".md")]
    if not company_files:
        print("[!] No company markdown files found to evaluate.")
        return

    eval_prompt = load_evaluation_prompt()
    resume_text = load_resume()

    all_tasks = []
    for cf in company_files:
        company_name = cf.replace(".md", "")
        filepath = os.path.join(COMPANIES_DIR, cf)
        jobs = parse_markdown_report(filepath)
        for job in jobs:
            job_key = f"{company_name}::{job.get('title')}::{job.get('link')}"
            all_tasks.append((company_name, cf, job, job_key))

    total_jobs = len(all_tasks)
    if total_jobs == 0:
        print("[!] Found company files, but zero active jobs inside them.")
        return

    completed_keys = load_state()
    
    print(f"{CYAN}[*] Starting evaluation batch: {total_jobs} total jobs across {len(company_files)} companies.{RESET}")
    print(f"{CYAN}[*] Previously completed: {len(completed_keys)} / {total_jobs}{RESET}")
    print("=" * 60)

    completed_count = len(completed_keys)
    start_time = time.time()
    file_handles = {}
    newly_processed_summaries = []

    try:
        for company_name, cf, job, job_key in all_tasks:
            if job_key in completed_keys:
                continue

            completed_count += 1
            job_title = job.get('title', 'Unknown Title')
            job_link = job.get('link', 'No Link')
            
            elapsed_total = time.time() - start_time
            active_done = completed_count - len(completed_keys)
            avg_time_per_job = (elapsed_total / active_done) if active_done > 0 else 300
            remaining_jobs = total_jobs - completed_count
            eta_seconds = remaining_jobs * avg_time_per_job
            
            eta_str = time.strftime('%H:%M:%S', time.gmtime(eta_seconds)) if remaining_jobs > 0 else "00:00:00"

            print(f"{YELLOW}[{completed_count}/{total_jobs}] ({company_name}) Evaluating: {job_title}{RESET}")
            print(f"    -> Elapsed: {int(elapsed_total)}s | Est. Remaining: {eta_str}")

            job_start = time.time()
            result = evaluate_job(company_name, job, eval_prompt, resume_text)
            job_duration = int(time.time() - job_start)
            print(f"    -> {GREEN}Done in {job_duration}s.{RESET}")

            report_output_path = os.path.join(OUTPUT_DIR, f"{company_name}_Evaluations.md")
            if company_name not in file_handles:
                mode = "a" if job_key in completed_keys or os.path.exists(report_output_path) else "w"
                file_handles[company_name] = open(report_output_path, mode, encoding="utf-8")
                if mode == "w":
                    file_handles[company_name].write(f"# Job Fit Evaluations: {company_name}\n\n")

            out = file_handles[company_name]
            out.write(f"# Job: {job_title}\n")
            out.write(f"Link: {job_link}\n\n")
            out.write(result)
            out.write("\n\n---\n\n")
            out.flush()

            completed_keys.append(job_key)
            save_state(completed_keys)
            
            # Track for email summary
            newly_processed_summaries.append(f"- Company: {company_name}\n  Role: {job_title}\n  Link: {job_link}\n")

    except KeyboardInterrupt:
        print(f"\n{YELLOW}[!] Pause requested by user (Ctrl+C). Saving progress state...{RESET}")
        save_state(completed_keys)
        print(f"{GREEN}[✓] State saved. You can resume anytime by running the script again.{RESET}")
        
        if newly_processed_summaries:
            send_notification_email(len(newly_processed_summaries), newly_processed_summaries)
            
        sys.exit(0)

    for f in file_handles.values():
        f.close()

    if os.path.exists(STATE_FILE):
        os.remove(STATE_FILE)

    print("=" * 60)
    print(f"{GREEN}[✓] All evaluations complete! Saved reports to '{OUTPUT_DIR}' directory.{RESET}")

    if newly_processed_summaries:
        send_notification_email(len(newly_processed_summaries), newly_processed_summaries)

if __name__ == "__main__":
    run_all_evaluations()