# ==============================================================================
# Project Name: Omnivore ATS Config Discovery Utility
# Author: Scott Malin, CISSP
#
# Purpose:
#   Takes a company name or starting URL, discovers the underlying ATS platform
#   (Greenhouse, Lever, Workday, etc.), verifies a working careers endpoint,
#   and outputs a ready-to-use configuration mapping.
#
# Version: 1.0.0
# Updated: 2026-10-12
# ==============================================================================

import os
import sys
import json
import re
import urllib.parse
import importlib.util

# ==============================================================================
# Prerequisite Checks
# ==============================================================================

REQUIRED_MODULES = ["playwright"]

MISSING_DEPS = [
    module for module in REQUIRED_MODULES
    if importlib.util.find_spec(module) is None
]

if MISSING_DEPS:
    print("=" * 65)
    print("[!] ERROR: Missing required Python packages.")
    print(f"    Missing: {', '.join(MISSING_DEPS)}")
    print("\n[-] Install them using:")
    print("    pip install playwright")
    print("    playwright install chromium")
    print("=" * 65)
    sys.exit(1)

from playwright.sync_api import sync_playwright

# ANSI terminal colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# Common ATS URL patterns to test if given a generic domain or company name
KNOWN_ATS_PATTERNS = [
    ("Greenhouse", "https://boards.greenhouse.io/{company}"),
    ("Greenhouse Embed", "https://job-boards.greenhouse.io/{company}"),
    ("Lever", "https://jobs.lever.co/{company}"),
    ("Workday", "https://{company}.wd5.myworkdayjobs.com/en-US/Careers"),
    ("Workday Alt", "https://{company}.myworkdayjobs.com/Careers"),
    ("SmartRecruiters", "https://jobs.smartrecruiters.com/{company}"),
    ("Breezy", "https://{company}.breezy.hr/"),
    ("ICIMS", "https://{company}.icims.com/jobs/search"),
]

def sanitize_slug(name):
    slug = name.lower().strip()
    slug = re.sub(r'[^a-z0-9]', '', slug)
    return slug

def test_url_active(url):
    """Uses Playwright to test if a URL loads and returns valid page content."""
    browser = None
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(
                user_agent=(
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
                )
            )
            response = page.goto(url, timeout=10000, wait_until="domcontentloaded")
            
            if response and response.status < 400:
                title = page.title()
                text = page.evaluate("() => document.body ? document.body.innerText : ''")
                # Basic sanity check to ensure it's not a generic 404 page
                if len(text.strip()) > 200 and "not found" not in title.lower():
                    return True, title
    except Exception:
        pass
    finally:
        if browser:
            try:
                browser.close()
            except Exception:
                pass
    return False, ""

def discover_ats(target_input):
    print(f"\n{CYAN}[*] Analyzing target: '{target_input}'...{RESET}")
    
    # If the user provided a direct URL
    if target_input.startswith(("http://", "https://")):
        print(f"[*] Testing direct URL: {target_input}")
        active, title = test_url_active(target_input)
        if active:
            print(f"{GREEN}[✓] Direct URL verified! Page Title: {title}{RESET}")
            parsed = urllib.parse.urlparse(target_input)
            domain_parts = parsed.netloc.split('.')
            company_label = domain_parts[-2] if len(domain_parts) >= 2 else parsed.netloc
            return [{"company": company_label.title(), "ats": "Direct/Custom", "url": target_input}]
        else:
            print(f"{YELLOW}[!] Direct URL did not respond or failed validation.{RESET}")
            return []

    # Otherwise treat input as a company name or slug
    slug = sanitize_slug(target_input)
    company_proper = target_input.strip().title()
    
    discovered = []
    
    print(f"[*] Probing common ATS patterns for slug: '{slug}'")
    for ats_name, pattern in KNOWN_ATS_PATTERNS:
        test_url = pattern.format(company=slug)
        print(f"    -> Testing {ats_name}: {test_url}")
        active, title = test_url_active(test_url)
        if active:
            print(f"    {GREEN}[✓] Found active {ats_name} board! Title: {title}{RESET}")
            discovered.append({
                "company": company_proper,
                "ats": ats_name,
                "url": test_url
            })
            # Found a working endpoint, can stop or keep looking for alternates
            break
        else:
            print(f"    {RED}[x] Inactive or invalid{RESET}")
            
    return discovered

def main():
    print("=" * 65)
    print(" Omnivore ATS Config Discovery Utility v1.0.0")
    print("=" * 65)
    
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("\nEnter company name or careers URL to test: ").strip()
        
    if not query:
        print(f"{RED}[!] No input provided. Exiting.{RESET}")
        return

    results = discover_ats(query)

    print("\n" + "=" * 65)
    if results:
        print(f"{GREEN}[✓] Discovery Complete. Config entry found:{RESET}\n")
        for res in results:
            print(f"  ATS Platform : {res['ats']}")
            print(f"  Config Format:")
            print(f'  "{res["company"]}": "{res["url"]}"\n')
    else:
        print(f"{YELLOW}[!] No standard ATS endpoints automatically verified for '{query}'.{RESET}")
        print("    Consider providing the direct ATS link or checking the company's main careers page.")
    print("=" * 65)

if __name__ == "__main__":
    main()