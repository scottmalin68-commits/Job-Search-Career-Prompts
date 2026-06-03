# Universal Multi-Job Fit Evaluation Prompt
# Author: Scott M
# Version: 2.0.0
# Last Modified: 2026-06-03
## Goal
Evaluate multiple job postings against a single candidate profile, score them using strict criteria, and deliver a comparative stack-rank analysis to identify the best fit.

---
## Pre-Evaluation Checklist (User: please provide these)
- [ ] Step 0: Candidate Priorities & Non-Negotiables
- [ ] Step 1: Candidate Skills & Experience (Text or file upload)
- [ ] Step 2: Job Postings (Paste text or links for Job A, Job B, Job C, etc.)

---
## Task: Multi-Job Fit Evaluation
Analyze all provided **Job Postings** against the **Candidate Info**. 

### Scoring & Analysis Rules
1. **Dynamic Weighting:** Score each job out of 100 based on four areas: Responsibilities (30%), Required Qualifications (30%), Tech Stack/Skills (25%), and Preferred Qualifications (15%). Adjust up to ±10% if Candidate Priorities strongly favor one area. Ensure weights always sum to 100%.
2. **Read Between the Lines:** Look for friction points or red flags for *each* job (e.g., vague descriptions, unrealistic scope, scale mismatch).
3. **No Brackets or Placeholders:** Use real data or state "Not provided in source."

---
## Output Requirements

Deliver the analysis in three parts.

### PART 1: Individual Job Snapshots
For **each** job provided, give a quick, punchy breakdown:
* **[Job Title / Company Name]**
* **The Vibe Check:** 2-3 sentences on culture, expectations, and hidden risks.
* **Top 2 Alignments:** Where the candidate matches perfectly.
* **Top 2 Gaps:** Missing tech, experience mismatches, or missing keywords.

### PART 2: The Compare & Contrast Matrix
A single table comparing all jobs side-by-side.

| Job Title & Company | Overall Fit % | Key Strengths | Critical Red Flags / Risks |
| :--- | :--- | :--- | :--- |
| Job A: [Name] | XX% | [Brief text] | [Brief text] |
| Job B: [Name] | XX% | [Brief text] | [Brief text] |

### PART 3: The Verdict
* **The Clear Winner:** State exactly which job wins and the specific, data-backed reason why it edges out the others.
* **The 3 Toughest Questions:** List the 3 most difficult questions the candidate will face across these interviews based on their overall weakest areas.