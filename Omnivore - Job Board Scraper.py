# ==============================================================================
# Project Name: Job Board Scraper & Filter Tool (Omnivore Project)
# Author: Scott Malin, CISSP
# Version: 1.6.1
# Purpose: Scrapes enterprise and tech job boards (bypassing bot protections via
#          Scrapling and platform APIs), filters relevant roles using configurable
#          keywords, and maintains a rolling 30-day markdown history.
#
# Changelog:
#    - 2026-09-29: Initial script structure and multi-platform scraping logic.
#    - 2026-10-04: Added dependency checks, beginner documentation, LLM context 
#                  notes, and replaced personal targets with clean examples.
#    - 2026-10-04: Added changelog back into the header for development tracking.
#
# NOTE FOR LLMS & BEGINNERS:
# This script scrapes job listings from popular applicant tracking systems like 
# Greenhouse, Workday, and custom career pages. If you run into errors or need 
# to modify how it works, you can paste this entire script into an AI assistant 
# along with your error message or request, and it will help you update it.
# ==============================================================================

from datetime import datetime, timedelta
import importlib.util
import json
import os
import random
import re
import sys
import time
from urllib.parse import urlparse
import warnings

# mute routine third-party deprecation warnings to keep the terminal clean
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ==============================================================================
# Terminal Colors
# Makes the text in your command prompt look nice with green/red/cyan highlights.
# ==============================================================================
class C:
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

# ==============================================================================
# Prerequisite Checks
# Automatically checks if required third-party libraries are installed. If any 
# are missing, it stops the script and gives you the exact pip commands to fix it.
# ==============================================================================
REQUIRED_MODULES = ["scrapling", "curl_cffi", "patchright", "msgspec", "browserforge"]
MISSING_DEPS = [mod for mod in REQUIRED_MODULES if importlib.util.find_spec(mod) is None]

if MISSING_DEPS:
    print(f"{C.RED}{'=' * 60}{C.RESET}")
    print(f"{C.RED}[!] ERROR: Missing required Python packages.{C.RESET}")
    print(f"    Missing: {', '.join(MISSING_DEPS)}")
    print(f"\n{C.CYAN}[-] Run these commands in your terminal to install them:{C.RESET}")
    print(f"    pip install scrapling curl_cffi patchright msgspec browserforge")
    print(f"    python -m patchright install")
    print(f"{C.RED}{'=' * 60}{C.RESET}")
    sys.exit(1)

from scrapling import StealthyFetcher
from curl_cffi import requests as cffi_requests
from patchright.sync_api import sync_playwright

# ==============================================================================
# Configuration & Variables
# Adjust these lists to change what jobs you look for and which companies to scrape.
# ==============================================================================
VERSION = "1.6.1"
COMPANIES_DIR = "company_files"
MAX_AGE_DAYS = 30
VERBOSE_DEBUG = False

# Keywords used to filter job titles. Only jobs containing these words are saved.
KEYWORDS = [
    'Software Engineer',
    'Python',
    'Cloud Architect',
    'DevOps',
]

# Dictionary of companies and their official career site or job board URLs.
TARGET_URLS = {
    "ExampleTech": "https://boards.greenhouse.io/exampletech",
    "GlobalCorp": "https://globalcorp.wd5.myworkdayjobs.com/en-US/Careers",
}

# ==============================================================================

os.makedirs(COMPANIES_DIR, exist_ok=True)


def detect_platform(url):
    """
    Looks at the provided URL and figures out which applicant tracking system 
    or platform it uses (Greenhouse, Workday, Lever, etc.) so we know how to scrape it.
    """
    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    if "greenhouse.io" in domain:
        return "greenhouse"
    elif "lever.co" in domain:
        return "lever"
    elif "myworkdayjobs.com" in domain:
        return "workday"
    elif "apply." in domain or "phenompeople" in domain or "csod.com" in domain:
        return "phenom"
    elif "dayforcehcm.com" in domain:
        return "dayforce"
    else:
        return "custom"


def should_keep_job(title):
    """
    Checks if a job title matches any of our target keywords. 
    If no keywords are set, it keeps everything.
    """
    if not KEYWORDS:
        return True
    title_lower = title.lower()
    return any(kw.lower() in title_lower for kw in KEYWORDS)


def load_existing_jobs(filepath):
    """
    Reads previously saved job listings from a markdown file so we don't 
    duplicate jobs we've already found.
    """
    if not os.path.exists(filepath):
        return []

    jobs = []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    sections = content.split("---")
    for sec in sections:
        if "Title:" in sec:
            job = {}
            for line in sec.strip().split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    job[key.strip().lower()] = val.strip()
            if "title" in job and "captured" in job:
                jobs.append(job)
    return jobs


def save_jobs(company_name, jobs):
    """
    Saves or updates the rolling markdown history file for a specific company, 
    dropping jobs older than our 30-day limit.
    """
    filepath = os.path.join(COMPANIES_DIR, f"{company_name}.md")
    today = datetime.now().date()

    active_jobs = []
    for job in jobs:
        try:
            captured_date = datetime.strptime(
                job.get("captured", str(today)), "%Y-%m-%d"
            ).date()
            if (today - captured_date).days <= MAX_AGE_DAYS:
                active_jobs.append(job)
        except ValueError:
            active_jobs.append(job)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {company_name} Job Postings\n\n")
        for job in active_jobs:
            f.write("--- \n")
            f.write(f"Title: {job.get('title')}\n")
            f.write(f"Company: {company_name}\n")
            f.write(f"Platform: {job.get('platform')}\n")
            f.write(f"Captured: {job.get('captured')}\n")
            f.write(f"Link: {job.get('link')}\n")
            f.write(f"Description:\n{job.get('description')}\n\n")
    return len(active_jobs)


def scrape_greenhouse(company_name, url):
    """Scrapes job listings from Greenhouse job boards via their public API."""
    board_token = url.rstrip("/").split("/")[-1]
    api_url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs?content=true"
    
    fetcher = StealthyFetcher()
    try:
        response = fetcher.fetch(api_url, headless=True)
        if response.status != 200:
            return []

        data = response.json()
        postings = data.get("jobs", [])
        
        jobs = []
        for item in postings:
            title = item.get("title")
            jobs.append({
                "title": title,
                "link": item.get("absolute_url"),
                "description": item.get("content", "No description provided.")[:500] + "..."
            })
        return jobs
    except Exception:
        return []


def scrape_workday(company_name, url):
    """Scrapes job listings from Workday portals using direct API requests or a browser fallback."""
    session = cffi_requests.Session(impersonate="chrome110")
    parsed = urlparse(url)
    tenant = parsed.netloc.split(".")[0]
    
    path_parts = [p for p in parsed.path.split("/") if p]
    site_name = path_parts[-1] if path_parts else company_name.replace(" ", "")
    
    endpoints = []
    base_sites = {
        site_name, 
        site_name.lower(), 
        company_name.replace(" ", ""), 
        company_name.replace(" ", "").lower()
    }
    for s in base_sites:
        if s:
            endpoints.append(f"https://{parsed.netloc}/wday/cxs/{tenant}/{s}/jobs")
            endpoints.append(f"https://{parsed.netloc}/wday/cxs/{tenant}/en-US/{s}/jobs")
            endpoints.append(f"https://{parsed.netloc}/wday/cxs/{tenant}/external/{s}/jobs")

    endpoints.append(f"https://{parsed.netloc}/wday/cxs/{tenant}/external/jobs")
    
    seen = set()
    unique_endpoints = []
    for ep in endpoints:
        if ep not in seen:
            seen.add(ep)
            unique_endpoints.append(ep)

    response = None
    for api_url in unique_endpoints:
        try:
            payload = {
                "appliedFacets": {},
                "limit": 20,
                "offset": 0,
                "searchText": "",
                "sortBy": "postedOnDesc"
            }
            res = session.post(
                api_url, 
                json=payload, 
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                }
            )
            if res.status_code == 200:
                response = res
                break
        except Exception:
            continue

    if not response or response.status_code != 200:
        captured_jobs = []
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
                page = context.new_page()

                def handle_response(res):
                    if "/wday/cxs/" in res.url and "/jobs" in res.url and res.status == 200:
                        try:
                            data = res.json()
                            if "jobPostings" in data:
                                for item in data["jobPostings"]:
                                    title = item.get("title")
                                    external_path = item.get("externalPath")
                                    job_link = f"https://{parsed.netloc}{external_path}" if external_path else url
                                    desc = " | ".join(item.get("bulletFields", [])) or "No description provided."
                                    captured_jobs.append({
                                        "title": title,
                                        "link": job_link,
                                        "description": desc
                                    })
                        except Exception:
                            pass

                page.on("response", handle_response)
                page.goto(url, timeout=60000)
                page.wait_for_timeout(5000)
                browser.close()
        except Exception:
            pass
        
        if captured_jobs:
            return captured_jobs
        return []
        
    try:
        data = response.json()
        postings = data.get("jobPostings", [])
        
        jobs = []
        for item in postings:
            title = item.get("title")
            external_path = item.get("externalPath")
            job_link = f"https://{parsed.netloc}{external_path}" if external_path else url
            
            desc = item.get("bulletFields", [])
            desc_text = " | ".join(desc) if desc else "No description provided."
            
            jobs.append({
                "title": title,
                "link": job_link,
                "description": desc_text
            })
        return jobs
    except Exception:
        return []


def scrape_generic(company_name, url):
    """Fallback scraper for custom websites by extracting links that look like job postings."""
    fetcher = StealthyFetcher()
    try:
        response = fetcher.fetch(url, headless=True)
        if response.status != 200:
            return []

        items = []
        for link in response.css("a"):
            title = link.text.strip()
            href = link.attrib.get("href", "")
            if title and len(title) > 6:
                if not href.startswith("http"):
                    parsed_base = urlparse(url)
                    href = f"{parsed_base.scheme}://{parsed_base.netloc}{href}"
                items.append({
                    "title": title,
                    "link": href,
                    "description": "Scraped via StealthFetcher fallback."
                })
        return items
    except Exception:
        return []


def scrape_company(company_name, url):
    """Coordinates scraping a single company, filters the results, and saves them."""
    platform = detect_platform(url)
    print(f"{C.CYAN}[+] Scraping {C.BOLD}{company_name}{C.RESET}{C.CYAN} via {platform}...{C.RESET}")

    today = str(datetime.now().date())
    filepath = os.path.join(COMPANIES_DIR, f"{company_name}.md")
    existing_jobs = load_existing_jobs(filepath)
    existing_titles = {j["title"] for j in existing_jobs}
    
    scraped_items = []
    if platform == "greenhouse":
        scraped_items = scrape_greenhouse(company_name, url)
    elif platform == "workday":
        scraped_items = scrape_workday(company_name, url)
    else:
        scraped_items = scrape_generic(company_name, url)

    status_flag = "[EMPTY/WARN]" if not scraped_items and platform != "custom" else "[OK]"

    new_jobs_found = 0
    for item in scraped_items:
        title = item.get("title", "")
        if should_keep_job(title):
            if title not in existing_titles:
                existing_jobs.append({
                    "title": title,
                    "platform": platform,
                    "captured": today,
                    "link": item.get("link"),
                    "description": item.get("description"),
                })
                existing_titles.add(title)
                new_jobs_found += 1

    total_active = save_jobs(company_name, existing_jobs)
    print(f"{C.GREEN}[✓] Done. Added {new_jobs_found} new roles ({total_active} total active) for {company_name}.{C.RESET}\n")

    time.sleep(random.uniform(2.5, 5.0))
    return new_jobs_found, total_active, status_flag


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    print(f"{C.BOLD}{C.GREEN}" + "=" * 65 + f"{C.RESET}")
    print(f"{C.BOLD}{C.CYAN}JOB SCRAPER v{VERSION} STARTING{C.RESET}")
    print(f"Target Sites: {list(TARGET_URLS.keys())}")
    print(f"Keywords: {KEYWORDS}")
    print(f"Max Age: {MAX_AGE_DAYS} days")
    print(f"{C.BOLD}{C.GREEN}" + "=" * 65 + f"{C.RESET}\n")

    summary_stats = {}
    total_new_all = 0

    for name, target_url in TARGET_URLS.items():
        new_count, active_count, status_flag = scrape_company(name, target_url)
        summary_stats[name] = {
            "new": new_count, 
            "active": active_count, 
            "status": status_flag
        }
        total_new_all += new_count

    print(f"{C.BOLD}{C.GREEN}" + "=" * 65 + f"{C.RESET}")
    print(f"{C.BOLD}{C.CYAN}SCRAPE RUN COMPLETE — SUMMARY STATS{C.RESET}")
    print(f"{C.BOLD}{C.GREEN}" + "=" * 65 + f"{C.RESET}")
    print(f"Total New Roles Found: {C.BOLD}{C.GREEN}{total_new_all}{C.RESET}")
    print("-" * 65)
    for name, stats in summary_stats.items():
        status_color = C.RED if "ERROR" in stats['status'] or "WARN" in stats['status'] else C.GREEN
        print(f"  {name:<18} | New: {stats['new']:<3} | Active: {stats['active']:<3} | Status: {status_color}{stats['status']}{C.RESET}")
    print(f"{C.BOLD}{C.GREEN}" + "=" * 65 + f"{C.RESET}\n")