# Universal Job Fit Evaluation Prompt – Fully Generic & Shareable
# Author: Scott M
# Version: 1.7.5
# Last Modified: 2026-05-21
## Changelog
- **v1.7.5 (2026-05-21):** Major functional upgrades for tool usage, file handling, dynamic weighting, portfolio analysis, and email-ready output. Addressed key gaps in URL fetching, absent data scoring, and professional formatting.
- **v1.7.0 (2026-05-21):** Standardized version string formatting to 3-point notation. Integrated Chain-of-Verification (CoV) scoring logic and adversarial red-teaming checks.
- **v1.6 (2026-03-06):** Integrated "Read Between the Lines" (Vibe Check), ATS Keyword Translation, and Interview Prep "Gotchas."
- **v1.5 (2026-03-04):** Added "User Action Advice" for blocked URLs. Restored visible author headers.
## Goal
Help a candidate objectively evaluate how well a job posting matches their skills, experience, and portfolio, while producing actionable guidance for applications, portfolio alignment, and skill gap mitigation. Output must be clean, professional, and ready for direct email or document use.

---
## Pre-Evaluation Checklist (User: please provide these)
- [ ] Step 0: Candidate Priorities (Remote? Salary? Tech stack?)
- [ ] Step 1: Skills & Experience (Markdown, pasted text, or file upload)
- [ ] Step 1a: Key Skills Anchor List (What matters most right now?)
- [ ] Step 2: Portfolio links/descriptions or file uploads
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

## Tool & Content Access Protocol (Critical)
You have access to web browsing and file reading tools. Use them proactively:
- **Job Posting URLs:** Use `open_page_with_find` or equivalent tools to fetch full, clean content. Extract job title, company, responsibilities, qualifications, and requirements. If paywalled or blocked, attempt LinkedIn/Indeed/company career page search as fallback.
- **Candidate Files:** If resume, portfolio, or documents are uploaded as files (PDF, DOCX, images), use file reading tools to extract full text. For screenshots or images, analyze visible content for experience, skills, and projects.
- **Portfolio Links:** For any provided portfolio or GitHub URLs, browse the most relevant 1-2 projects and extract concrete evidence (technologies, scale, outcomes, impact).
- **Fallback:** If data remains inaccessible after tool use, clearly state: "⚠️ Inaccessible Source: [details]. Recommend user pastes full text or uploads file."

## Task: Job Fit Evaluation
Analyze the **Job Posting** against the **Candidate Info** provided above.

### Anti-Hallucination, Drift, & Scoring Guardrails
1. **Chain-of-Verification (CoV):** Before assigning any match percentage, extract exact underlying text evidence from both candidate profile and job description. No direct evidence = appropriate score penalty.
2. **Adversarial Red-Teaming:** Actively identify hidden friction points, scale mismatches, legacy tech issues, or environment differences.
3. **Ignore Source Evaluations:** Disregard any internal screening matrices or grading tables in the job description. Evaluate fresh.
4. **No Placeholders:** Do not use empty brackets, raw template strings like "XX%", or conversational filler. Use "Not provided in source" when data is missing.

### Scoring Instructions
- Use semantic alignment, not just keyword matching.
- **Dynamic Weighting:** Start with default (Responsibilities 30%, Required Qualifications 30%, Skills/Tech/Edu 25%, Preferred 15%). Adjust weights by up to ±10% per section if Candidate Priorities strongly emphasize certain areas (e.g., heavy tech stack focus increases Skills weighting).
- **Missing Data Rule:** If a major section has zero extractable evidence from the candidate, cap that section at 35% maximum and note "Insufficient data provided."

### Specific Analysis Requirements
1. **Read Between the Lines:** Identify hidden requirements, red flags (burnout culture, vague scope, seniority signals, company stage).
2. **ATS Translation:** List 5-10 specific keywords/phrases from the JD that are missing from the candidate's materials but align with their likely experience.
3. **Interview Prep "Gotchas":** Identify the 3 toughest questions a recruiter will likely ask based on the candidate's specific gaps or weakest areas.
4. **Years of Experience:** Explicitly flag any mismatches in required vs. candidate experience levels.

## Output Requirements (Professional & Email-Ready)
Generate clean, professional prose suitable for direct copying into email, Word, or PDF. Use clear headings, bullet points, and professional tone. No markdown checkboxes or raw templates.

- **Overall Fit Percentage** (Calculated weighted average based on CoV validation)
- **Confidence Level** (High/Medium/Low based on info completeness)
- **Vibe Check:** Summary of the "Read Between the Lines" analysis, including culture, remote signals, and growth trajectory.
- **Top 3 Alignments:** Specific strong matches with exact grounding quotes from both JD and candidate info.
- **Top 3 Gaps:** Critical missing skills/experience with practical mitigation advice.
- **Portfolio-Specific Guidance:** Connect 1-2 job requirements to concrete portfolio improvements or highlights.
- **Additional Commentary:** Flag location, salary, culture, or non-negotiable mismatches.

### Final Summary Table
| Section                    | Match % | Key Alignments & Gaps                          | Confidence   |
|----------------------------|---------|------------------------------------------------|--------------|
| Responsibilities           |         |                                                |              |
| Required Qualifications    |         |                                                |              |
| Preferred Qualifications   |         |                                                |              |
| Skills / Technologies / Edu|         |                                                |              |
| **Overall Fit**            | ** **   |                                                | **High/Med/Low** |

## Job Posting Source