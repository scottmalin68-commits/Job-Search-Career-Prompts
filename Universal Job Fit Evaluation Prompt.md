<!-- Universal Job Fit Evaluation Prompt – Fully Generic & Shareable -->
<!-- Author: Scott M -->
<!-- Version: 1.3 -->
<!-- Last Modified: 2026-02-04 -->

## Goal
Help a candidate objectively evaluate how well a job posting matches their skills, experience, and portfolio, while producing actionable guidance for applications, portfolio alignment, and skill gap mitigation.

This prompt is designed to be:
- Profession-agnostic
- Shareable
- Resume- and portfolio-aware
- Explicit about assumptions and fallbacks

---

## Pre-Evaluation Checklist (User: please confirm these are provided before proceeding)
- [ ] Step 0: Candidate Priorities customized
- [ ] Step 1: Skills & Experience source (markdown link or pasted content)
- [ ] Step 1a: Key Skills Anchor List (optional but strongly recommended if focusing on specific areas)
- [ ] Step 2: Portfolio links/descriptions (optional but recommended)
- [ ] Job Posting: URL or full text inserted below

If any are missing, the evaluation may have reduced confidence.

---

## Step 0: Candidate Priorities (Evaluate With These in Mind)
<!-- These priorities should influence scoring, weighting, and commentary -->
<!-- ←←← CUSTOMIZE THIS SECTION →→→ -->

- Highest priority roles or domains:
- Location preference (remote / hybrid / city / region):
- Compensation expectations or constraints:
- Non-negotiables (e.g., on-call, travel, clearance, tech stack):
- Nice-to-haves:

---

## Step 1: Skills & Experience Source (Primary Reference)

### Preferred: Skills & Experience Markdown File
Provide access to a structured markdown file describing the candidate.

**Expected sections (recommended, not mandatory):**
- Core Skills (strongest, production-ready)
- Supporting / Secondary Skills
- Tools & Technologies
- Years of Experience / Seniority indicators
- Notable Projects or Achievements
- Certifications / Education (if relevant)

<!-- INSERT ONE OR MORE METHODS BELOW -->

<!-- Option A – Direct link(s) to a markdown file -->
<!-- Example: https://raw.githubusercontent.com/username/skills-summary/main/Skills_Experience.md -->

<!-- Option B – Paste the full markdown content directly here -->
<!-- ←←← PASTE SKILLS & EXPERIENCE MARKDOWN HERE →→→ -->

---

## Step 1a: Key Skills to Explicitly Evaluate (Anchor List)
<!-- Use this to force evaluation of specific skills, even if the resume is broad -->
<!-- Especially useful for career pivots or skill-building phases -->

<!-- Example:
- Python (data analysis, automation)
- Cloud security (AWS, IAM, threat modeling)
- Technical writing for non-technical audiences
-->

<!-- ←←← INSERT KEY SKILLS / EXPERIENCE FOCUS AREAS HERE →→→ -->

---

## Step 2 (Optional but Recommended): Portfolio / Work Samples
<!-- Provide access the same way as skills: links or pasted descriptions -->
<!-- Examples:
- Portfolio site
- GitHub repos
- Case study PDFs
- Design files, demos, videos
-->

<!-- ←←← INSERT PORTFOLIO LINKS OR DESCRIPTIONS HERE →→→ -->

---

## Fallback Rule (Do Not Remove)
If any provided links are broken, empty, or inaccessible, display:

"⚠️ One or more reference files inaccessible – proceeding with conversation history, attached resumes, and any portfolio details already shared."

Then continue with available information. If critical sections are missing, note reduced confidence in the output.

---

## Task: Job Fit Evaluation

Analyze the provided job posting (URL or full text) against:
- Skills & Experience Markdown
- Key Skills Anchor List
- Portfolio (when applicable)
- Candidate Priorities

### Scoring Instructions
For each section, assign a percentage match calculated as:
- Approximate proportion of listed job requirements / duties / qualifications that are demonstrably met by the candidate’s provided skills, experience, portfolio, and anchor list (e.g., 4 out of 5 key duties align → ~80%).
- Use semantic alignment, not just keyword matching.
- Provide 2–3 concise sentences explaining key alignments and gaps.

Sections to score:
- Responsibilities / Key Duties
- Required Qualifications / Experience
- Preferred Qualifications (if listed)
- Skills / Technologies / Education / Certifications

**Default Weighting (unless overridden):**
- Responsibilities:          30%
- Required Qualifications:   30%
- Skills / Technologies:     25%
- Preferred Qualifications:  15%

Explain any adjustment to weighting if role seniority, domain, or candidate priorities warrant it (e.g., heavy emphasis on seniority might increase Required Qualifications weight).

---

## Output Requirements

Provide:
- Overall Fit Percentage (weighted average of section scores)
- Confidence Level: High / Medium / Low  
  (based on completeness of provided candidate info: High = full markdown + portfolio + priorities; Medium = partial; Low = minimal info)
- 2–4 tailored application recommendations
- Portfolio-Specific Guidance (when relevant): Tie each recommendation to a specific skill gap or requirement + a concrete portfolio action  
  Example: “This JD emphasizes X; your Project Y demonstrates this partially. Expand the case study to highlight Z to close the gap.”

---

## Additional Commentary
Call out any visible:
- Location constraints
- Salary range mismatches
- Remote/hybrid policies
- Clearance, travel, or on-call expectations
- Cultural or structural deal-breakers

---

## Final Summary Table (Use This Exact Format)

| Section                        | Match % | Key Alignments & Gaps                              | Confidence |
|--------------------------------|---------|----------------------------------------------------|------------|
| Responsibilities               | XX%     |                                                    |            |
| Required Qualifications        | XX%     |                                                    |            |
| Preferred Qualifications       | XX%     |                                                    |            |
| Skills / Technologies / Edu    | XX%     |                                                    |            |
| **Overall Fit**                | **XX%** |                                                    | **High/Medium/Low** |

---

## Job Posting
<!-- INSERT JOB URL OR FULL JOB DESCRIPTION HERE -->

If the job URL is inaccessible, search LinkedIn, Indeed, Glassdoor, or the company’s career page for the current version of the role and note that you did so.
