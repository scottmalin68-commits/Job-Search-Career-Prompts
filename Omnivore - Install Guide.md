# Omnivore — Installation & Setup Guide

Omnivore is an automated job discovery, screening, and evaluation pipeline built for Python 3.10+. It uses local LLM triage via Ollama alongside cloud models to filter and score career opportunities against candidate profiles.
Author: Scott Malin, CISSP
Version 1.1.0

---

## Changelog

### v1.1.0
- Added documentation for detailed career profiles in evaluator configuration.
- Added instructions for updating user-configurable variables directly in the scripts.
- Included the complete requirements.txt file contents directly in the guide for easy setup.
- Included prompt markdown files, targeting prompts, and ATS discovery utility in the core file structure.

---

## System Requirements

1. Python 3.10 or higher
Verify your version:
python --version
2. Ollama (for Stage 1 Local Triage)
- Download and install from ollama.com.
- Pull the recommended local triage model:
ollama pull llama3.1
- Ensure the Ollama service is running locally (http://localhost:11434).

---

## 1. Environment Setup

Clone the repository and set up a Python virtual environment:

Create virtual environment:
python -m venv venv

Activate on Windows (PowerShell):
.\venv\Scripts\Activate.ps1

Activate on Linux / macOS:
source venv/bin/activate

---

## 2. Install Required Dependencies

Create a file named requirements.txt in your project root with the package contents shown below, then install the package requirements:

scrapling>=0.2.0
curl_cffi>=0.7.0
patchright>=0.1.4
openai>=1.0.0
windows-curses>=2.4.0; sys_platform == 'win32'

Run the installation command:

pip install -r requirements.txt

Note: windows-curses is required on Windows systems for Omnivore - Interactive Reviewer.py.

---

## 3. Install Browser Binaries

Install Chromium binaries required for JavaScript-rendered ATS pages and fallback scraping:

python -m patchright install chromium

---

## 4. Configuration & Candidate Profiles

1. **API Keys:**
   - `GEMINI_API_KEY`: Required for Stage 2 deep evaluations in Omnivore - Job Fit Evaluator.py.
     * How to get one: Go to Google AI Studio (https://aistudio.google.com), sign in with a Google account, and click "Get API key" to generate a new key.

2. **Email Reporting Setup (Optional):**
   - Open `Omnivore - Job Fit Evaluator.py` and locate the SMTP configuration block near the top.
   - Set `ENABLE_EMAIL = True`, enter your sender/recipient addresses, SMTP server (e.g., `smtp.gmail.com`), and port (`587`).
   - Set `SMTP_PASSWORD` as an environment variable (use an App Password if using Gmail):

   Example (PowerShell):
   $env:GEMINI_API_KEY="your-gemini-api-key-here"
   $env:SMTP_PASSWORD="your-app-password-here"

   Example (Linux/macOS):
   export GEMINI_API_KEY="your-gemini-api-key-here"
   export SMTP_PASSWORD="your-app-password-here"

3. **User-Configurable Values:**
   - Open `Omnivore - Job Board Scraper.py` and `Omnivore - Job Fit Evaluator.py` in your text editor.
   - Look for the configuration block near the top of each script to set target URLs, search keywords, output directories, and thresholds.

4. **Career Profile:**
   - The evaluator matches opportunities against a candidate profile. While a standard resume works, a detailed career profile outlining specific technical skills, tools, and experience yields much better evaluation results. Update your profile path or text block in the evaluator configuration section.

---

## 5. File Structure

Ensure all pipeline scripts, prompt files, and documentation assets are in the same directory:

- requirements.txt
- Omnivore - Job Board Scraper.py
- Omnivore - Job Fit Evaluator.py
- Omnivore - Interactive Reviewer.py
- Omnivore - ATS Config Discovery.py
- Omnivore - Job Board Target.md
- Lite Job Fit Evaluation Prompt - API Call.md
- Universal Job Fit Evaluation Prompt - API Call.md
- Omnivore - Jobseeker Sample email.png

---

## Execution Order

1. Generate targeting strategy (optional):
   - Review `Omnivore - Job Board Target.md` with your career profile to discover potential remote and local target boards.
2. Discover ATS endpoints (optional):
python "Omnivore - ATS Config Discovery.py"
3. Run the Scraper:
python "Omnivore - Job Board Scraper.py"
4. Run the Evaluator:
python "Omnivore - Job Fit Evaluator.py"
   - Once completed, the evaluator generates a summary report. If email reporting is enabled, you will receive an HTML summary email formatted like `Omnivore - Jobseeker Sample email.png`.
5. Review Results in Terminal UI:
python "Omnivore - Interactive Reviewer.py"