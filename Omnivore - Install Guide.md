# Omnivore — Installation & Setup Guide

Omnivore is an automated job discovery, screening, and evaluation pipeline built for Python 3.10+. It uses local LLM triage via Ollama alongside cloud models to filter and score career opportunities against candidate profiles.
Author: Scott Malin, CISSP
Version 1.0.0

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

Install the Python package requirements:

pip install -r requirements.txt

If requirements.txt is not present, install directly:

pip install scrapling curl_cffi patchright openai windows-curses

Note: windows-curses is required on Windows systems for Omnivore - Interactive Reviewer.py.

---

## 3. Install Browser Binaries

Install Chromium binaries required for JavaScript-rendered ATS pages and fallback scraping:

python -m patchright install chromium

---

## 4. API Credentials & Environment Variables

Configure your API keys as environment variables or update default values in configuration:

- GEMINI_API_KEY: Required for Stage 2 deep evaluations in Omnivore - Job Fit Evaluator.py.
  * How to get one: Go to Google AI Studio (https://aistudio.google.com), sign in with a Google account, and click "Get API key" to generate a new key.
- SMTP_PASSWORD: Required if email reporting options are enabled.

Example (PowerShell):
$env:GEMINI_API_KEY="your-gemini-api-key-here"

Example (Linux/macOS):
export GEMINI_API_KEY="your-gemini-api-key-here"

---

## 5. File Structure

Ensure all pipeline scripts and prompt files are in the same directory:

- Omnivore - Job Board Scraper.py
- Omnivore - Job Fit Evaluator.py
- Omnivore - Interactive Reviewer.py
- Omnivore - ATS Config Discovery.py
- Lite Job Fit Evaluation Prompt - API Call.md
- Universal Job Fit Evaluation Prompt - API Call.md

---

## Execution Order

1. Discover ATS endpoints (optional):
python "Omnivore - ATS Config Discovery.py"
2. Run the Scraper:
python "Omnivore - Job Board Scraper.py"
3. Run the Evaluator:
python "Omnivore - Job Fit Evaluator.py"
4. Review Results in Terminal UI:
python "Omnivore - Interactive Reviewer.py"