# Universal Job Fit Evaluation Prompt – Fully Generic & Shareable
# Author: Scott M
# Version: 1.7.0
# Last Modified: 2026-05-21

## Changelog
- **v1.7.0 (2026-05-21):** Standardized version string formatting to 3-point notation. Integrated Chain-of-Verification (CoV) scoring logic and adversarial red-teaming checks from advanced prompt logic files to permanently stop drift and hallucination. Stripped output bracket formatting for direct document export.
- **v1.6 (2026-03-06):** Integrated "Read Between the Lines" (Vibe Check), ATS Keyword Translation, and Interview Prep "Gotchas."
- **v1.5 (2026-03-04):** Added "User Action Advice" for blocked URLs. Restored visible author headers.

## Goal
Help a candidate objectively evaluate how well a job posting matches their skills, experience, and portfolio, while producing actionable guidance for applications, portfolio alignment, and skill gap mitigation.

---

## Pre-Evaluation Checklist (User: please provide these)
- [ ] Step 0: Candidate Priorities (Remote? Salary? Tech stack?)
- [ ] Step 1: Skills & Experience (Markdown link or pasted text)
- [ ] Step 1a: Key Skills Anchor List (What matters most right now?)
- [ ] Step 2: Portfolio links/descriptions
- [ ] Job Posting: URL or full text

---

## Step 0: Candidate Priorities
- Roles/Domains:
- Location preference (remote / hybrid / city / region):
- Compensation expectations or constraints:
- Non-negotiables (e.g., on-call, travel, clearance, tech stack):
- Nice-to-haves:

---

## Step 1 & 1a: Skills, Experience, & Focus Areas
---

## Step 2: Portfolio / Work Samples
---

## URL Access & Fallback Protocol

**If a provided URL is broken, empty, or blocked by a paywall/login:**
1. **Internal Search:** Attempt to find the job details via LinkedIn, Indeed, or the company’s career page.
2. **Warn:** If data is still missing, display: "⚠️ Inaccessible Source: I cannot read the data at the provided URL."
3. **User Action Advice:** If I cannot access the posting, please try the following:
   - **Direct Paste:** Copy the full job description text from your browser and paste it here.
   - **File Upload:** Save the webpage as a PDF or take a screenshot and upload the file.
   - **Print to PDF:** Use "Print to PDF" in your browser to generate a clean document of the JD.

---

## Task: Job Fit Evaluation

Analyze the **Job Posting** against the **Candidate Info** provided above.

### Anti-Hallucination, Drift, & Scoring Guardrails
1. **Chain-of-Verification (CoV):** Before assigning any match percentage to a section, you must extract the exact underlying text evidence from both the candidate profile and the JD. If no direct evidence exists, the score must penalize appropriately.
2. **Adversarial Red-Teaming:** Actively look for hidden friction points or scale mismatches. (e.g., Does the candidate have the right tool but at a vastly different scale or environment size? Is there a legacy technology listed in the JD that the candidate has moved away from?)
3. **Ignore Source Evaluations:** Completely disregard any pre-existing internal screening matrices, evaluations, or grading tables present in the raw job description text. Perform the evaluation fresh.
4. **No Placeholders or Conversational Filler:** Do not output empty bracket templates, raw template strings like "XX%", or conversational "fluff." If critical data points are missing, state "Not provided in source" directly in the space.

### Scoring Instructions
For each section, assign a percentage match based on actual content alignment. Use semantic alignment, not just keyword matching.

**Default Weighting:**
- Responsibilities: 30%
- Required Qualifications: 30%
- Skills / Technologies / Edu: 25%
- Preferred Qualifications: 15%

### Specific Analysis Requirements
1. **Read Between the Lines:** Identify "hidden" requirements or red flags (e.g., signs of burnout culture, vague scope, or unstated seniority).
2. **ATS Translation:** List 5-10 specific keywords from the JD that are missing from the candidate's markdown but represent experience they likely have based on their background.
3. **Interview Prep "Gotchas":** Identify the 3 toughest questions a recruiter will likely ask based on the candidate's specific gaps or "weakest" match areas.

---

## Output Requirements (Format for Direct Export)
Do not include markdown checkbox brackets `[ ]` or raw template markers in this output. Generate clean, professional text ready for document conversion.

- **Overall Fit Percentage** (Calculated weighted average based on CoV validation)
- **Confidence Level** (High/Medium/Low based on info completeness)
- **Vibe Check:** Summary of the "Read Between the Lines" analysis.
- **Top 3 Alignments:** Specific areas where the candidate matches, including the exact grounding details from the text.
- **Top 3 Gaps:** Missing skills or experience with advice on how to mitigate them.
- **Portfolio-Specific Guidance:** Connect a specific job requirement to a concrete portfolio action.
- **Additional Commentary:** Flag location, salary, or culture mismatches.

---

### Final Summary Table

| Section | Match % | Key Alignments & Gaps | Confidence |
| :--- | :--- | :--- | :--- |
| Responsibilities | | | |
| Required Qualifications | | | |
| Preferred Qualifications | | | |
| Skills / Technologies / Edu | | | |
| **Overall Fit** | ** ** | | **High/Med/Low** |

---

## Job Posting Source