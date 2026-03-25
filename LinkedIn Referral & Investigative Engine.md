# 🔍 LinkedIn Referral & Investigative Engine v1.0
**Author:** Scott M. | **Status:** Active | **Date:** 2026-03-22

---

### 🎯 Purpose
This tool is designed to bridge the gap between "cold" applying and "warm" referrals. Since AI cannot directly scrape or interact with LinkedIn's live database due to rate limits and bot defenses, this engine acts as a **strategic co-pilot**. It handles the external research, generates surgical search strings, and drafts high-conversion outreach to turn a job posting into a direct conversation with a decision-maker.

### 📝 Changelog
* **v1.0 (2026-03-22):** Initial build. Features automated job posting analysis, x-ray search string generation, and "no-oriented" outreach logic.

---

### 🛠️ Basic Instructions
1.  **The Intake:** Paste a job posting link or the full text.
2.  **The Search:** Use the generated **x-ray strings** in Google and the **internal queries** inside LinkedIn's search bar. 
3.  **The Find:** Identify 1-3 people (hiring manager, peer, or recruiter) and bring their names/titles back here.
4.  **The Outreach:** Get a custom-tailored message to send as a connection request or DM.

> [!IMPORTANT]
> **Manual execution required:** AI cannot "click" or "see" inside LinkedIn for you. You must perform the searches and the actual outreach within your own account to avoid security flags.

---

### 🤖 Prompt Logic (Copy/Paste)

```text
Act as an investigative career strategist. Your goal is to help me bypass the "resume robot" by finding the right humans at [company]. 

### Phase 1: The Scan
Analyze the job posting I provide. Identify:
1. The likely **hiring manager** (by title).
2. The **primary pain point** the company is trying to solve with this hire.
3. 3-5 unique **keywords** for x-ray searching.

### Phase 2: The "X-Ray" Toolkit
Generate 3 Google x-ray strings to find employees on LinkedIn without hitting search limits:
* **The Boss:** Target director/head of levels.
* **The Peers:** Target people currently in this specific role.
* **The Recruiters:** Target internal talent acquisition for this specific vertical.

### Phase 3: Internal LinkedIn Queries
Provide 2 optimized search strings for me to paste directly into the LinkedIn search bar (e.g., using boolean operators like AND/OR).

### Phase 4: The "No-Oriented" Outreach
Once I provide a name/title, draft two options:
* **The Connection Request (300 chars):** A low-pressure note to get the add.
* **The Direct Message:** A "no-oriented" question (e.g., "Would you be against...") that focuses on their referral bonus or the team's current challenges.

Ready? Here is the job info:
[INSERT JOB POSTING OR LINK HERE]