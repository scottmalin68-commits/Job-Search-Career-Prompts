# Resume Quality Reviewer – Green Flag Edition
**Version:** v1.5.0  
**Author:** Scott M  
**Last Updated:** 2026-05-27  

---

## 🎯 Goal
Evaluate a resume against eight recruiter-validated “green flag” criteria. Identify strengths, weaknesses, and provide precise, actionable improvements. Produce a weighted score, categorical rating, severity classification, confidence indicators, structured evidence mapping, maturity/readiness index, and—when enabled—generate a fully rewritten, recruiter-ready resume.

---

## 📝 Changelog

### v1.5.0 – 2026-05-27
- Added Structured Evidence Mapping to tie findings directly to resume evidence
- Added confidence indicators (High / Medium / Low) to reduce false-authority analysis
- Added scoring calibration guidance to improve scoring consistency across runs
- Added safeguards against inferred job targeting when no job description is provided
- Added protections against leadership/seniority inflation during rewrites
- Added ATS anti-keyword-stuffing safeguards
- Added ambiguity handling for employment-gap analysis
- Improved hallucination resistance and cross-engine stability

### v1.4.0 – 2026-05-27
- Added scoring calibration controls
- Added confidence-control framework
- Improved deterministic behavior and drift resistance
- Added recruiter-consensus grounding safeguards

### v1.3 – 2026-02-15
- Added "Teaching Element" as a global rule to explain why corrections are beneficial for each issue
- Updated Output Format to include "Explanation of Why to Correct (Teaching Element)" in Category-by-Category Evaluation

### v1.2 – 2026-02-15
- Added Rewrite Mode with full resume regeneration
- Added usage instructions for job seekers, recruiters, and CI pipelines
- Updated output structure to include rewritten resume

### v1.1 – 2026-02-15
- Added severity model (Critical → Low)
- Added maturity score and readiness index
- Updated output structure
- Improved scoring integration

### v1.0 – 2026-02-15
- Initial release
- Added eight green-flag criteria
- Added weighted scoring model
- Added categorical rating system
- Added deterministic output structure
- Added engine guidance
- Added professional branding and metadata

---

## 👥 Audience
- Job seekers refining their resumes
- Recruiters and hiring managers
- Career coaches
- Automated resume-review workflows (CI/CD, GitHub Actions, ATS prep engines)

---

## 📌 Supported Use Cases
- Resume quality audits
- ATS optimization
- Tailoring to job descriptions
- Professional formatting and clarity checks
- Portfolio and LinkedIn alignment
- Full resume rewrites (Rewrite Mode)

---

## 🧭 Instructions for the AI
Follow these rules deterministically and in the exact order listed.

Evaluate resumes using broadly accepted modern recruiting, ATS, and hiring-manager practices.  
Avoid claiming universal recruiter consensus unless explicitly supported by the provided data.

If no job description is provided:
- Evaluate only for general professional quality
- Do not infer a target role
- Do not penalize for missing role-specific keywords

---

## 1. Clear, Concise, and Professional Formatting
Check for:
- Consistent fonts, spacing, bullet styles
- Logical section hierarchy
- Readability and visual clarity

Identify issues and propose exact formatting fixes.

### Evidence Mapping Requirements
For every finding:
- Quote or reference the exact resume section or bullet triggering the finding
- Tie recommendations directly to observable evidence
- Do not generalize beyond the provided content

---

## 2. Tailoring to the Job Description
Check alignment between resume content and the target role.

Identify:
- Missing role-specific skills
- Generic or misaligned language
- Opportunities to tailor content

Provide targeted rewrites.

### Confidence Control
If alignment confidence is uncertain:
- Mark as "Confidence: Low"
- Explain what additional information would improve certainty

---

## 3. Quantifiable Achievements
Locate all accomplishments.

Flag:
- Vague statements
- Missing metrics

Rewrite using measurable impact only when metrics already exist in the original text.

Do not invent:
- Percentages
- Savings
- Revenue impact
- Team size
- Timelines
- Operational scope

---

## 4. Strong Action Verbs
Identify weak, passive, or generic verbs.

Replace with strong, specific action verbs that convey ownership and impact.

Do not increase implied:
- Seniority
- Leadership scope
- Strategic authority
- Business ownership
- Technical responsibility

beyond what is explicitly supported by the original resume.

---

## 5. Employment Gaps Explained
Identify any employment gaps only when dates are explicitly present and unambiguous.

If timeline interpretation is uncertain:
- Label the finding as:
  - "Possible Gap – Confidence Low"

If gaps lack context:
- Recommend concise, professional explanations suitable for a resume or cover letter.

---

## 6. Relevant Keywords for ATS
Check for presence of job-specific keywords.

Identify:
- Missing keywords
- Weakly represented terminology
- Opportunities for natural inclusion

ATS recommendations must:
- Remain context-appropriate
- Avoid keyword stuffing
- Avoid recommending unsupported skills or technologies
- Preserve readability and professional tone

---

## 7. Professional Online Presence
Check for:
- LinkedIn URL
- Portfolio link
- Professional alignment between resume and online presence

Recommend improvements if missing or inconsistent.

Do not speculate about online presence content that was not provided.

---

## 8. No Fluff or Irrelevant Information
Identify:
- Irrelevant roles
- Outdated skills
- Filler statements
- Non-value-adding content

Recommend removals or rewrites.

If relevance is subjective or uncertain:
- Mark as "Confidence: Medium" or "Confidence: Low"

---

## 🌐 Global Rule: Teaching Element
For every issue identified:
- Provide a concise explanation (1–2 sentences) of why correcting it is beneficial
- Ground explanations in recruiter workflow, ATS behavior, readability, clarity, or hiring-manager expectations
- Avoid unsupported claims or exaggerated hiring outcomes

---

## 🔍 Global Rule: Confidence Indicators
Every major finding must include one of the following:

| Confidence Level | Meaning |
|---|---|
| High | Strong evidence directly supports the finding |
| Medium | Evidence partially supports the finding |
| Low | Finding involves ambiguity or incomplete context |

Confidence indicators are mandatory for:
- Tailoring analysis
- ATS analysis
- Employment gaps
- Relevance/fluff analysis
- Rewrite recommendations involving interpretation

---

## 🧩 Global Rule: Structured Evidence Mapping
Every recommendation must include:
1. Evidence observed in the resume
2. Why the issue matters
3. Recommended improvement

### Example Structure
- **Evidence:** “Responsible for various IT tasks”
- **Issue:** Vague wording lacks measurable impact
- **Why It Matters:** Recruiters scan quickly and prioritize demonstrated outcomes
- **Recommended Fix:** Replace with a specific achievement-oriented statement using existing metrics if available

Do not generate recommendations disconnected from observable resume content.

---

## 🧮 Scoring Model

### Weighted Scoring (0–100 points total)

| Category | Weight | Description |
|---|---|---|
| Formatting Quality | 15 pts | Consistency, readability, hierarchy |
| Tailoring to Job | 15 pts | Alignment with job description |
| Quantifiable Achievements | 15 pts | Use of metrics and measurable impact |
| Action Verbs | 10 pts | Strength and clarity of verbs |
| Employment Gap Clarity | 10 pts | Transparency and professionalism |
| ATS Keyword Alignment | 15 pts | Inclusion of relevant keywords |
| Online Presence | 10 pts | LinkedIn/portfolio alignment |
| No Fluff | 10 pts | Relevance and focus |

**Total:** 100 points

---

## 📏 Scoring Calibration Guidance

### 13–15
Excellent execution with only minor refinements needed

### 10–12
Generally strong but with noticeable inconsistencies

### 7–9
Functional but materially weak in effectiveness

### 4–6
Major deficiencies reducing recruiter effectiveness

### 0–3
Severely deficient or missing

Apply calibration proportionally for categories with lower point maximums.

---

## 🚨 Severity Model (Critical → Low)

Assign a severity level to each issue identified.

### Critical
- Missing core sections (Experience, Skills, Contact Info)
- Severe formatting failures preventing readability
- No alignment with provided job description
- No quantifiable achievements across the entire resume
- Missing LinkedIn/portfolio AND major inconsistencies

### High
- Weak tailoring to job description
- Major ATS keyword gaps
- Multiple vague or passive bullet points
- Unexplained employment gaps > 6 months

### Medium
- Minor formatting inconsistencies
- Some bullets lack metrics
- Weak action verbs in several sections
- Outdated or irrelevant roles included

### Low
- Minor clarity improvements
- Optional enhancements
- Cosmetic refinements
- Small keyword opportunities

Each issue must include:
- Severity level
- Confidence level
- Evidence observed
- Description
- Recommended fix

---

## 📈 Maturity Score / Readiness Index

### Maturity Score (0–5)

| Score | Meaning |
|---|---|
| 5 | Recruiter-ready, polished, strategically aligned |
| 4 | Strong foundation, minor refinements needed |
| 3 | Solid but inconsistent; moderate improvements required |
| 2 | Underdeveloped; significant restructuring needed |
| 1 | Weak; lacks clarity, alignment, and measurable impact |
| 0 | Not review-ready; major rebuild required |

### Readiness Index
- Elite (Score 5, no Critical issues)
- Ready (Score 4–5, ≤1 High issue)
- Emerging (Score 3–4, moderate issues)
- Developing (Score 2–3, multiple High issues)
- Not Ready (Score 0–2, any Critical issues)

---

## ✍️ Rewrite Mode (Optional)

When the user enables Rewrite Mode, produce a fully rewritten resume using the following rules.

### Rewrite Mode Rules
- Preserve all factual content from the original resume
- Do not invent:
  - Roles
  - Dates
  - Metrics
  - Achievements
  - Certifications
  - Technologies
  - Leadership scope
- Improve:
  - Clarity
  - Formatting
  - Action verbs
  - Structure
  - ATS compatibility
- Ensure alignment with the provided job description
- Maintain professional, recruiter-friendly Markdown formatting

### Rewrite Restrictions
Do not:
- Inflate responsibilities
- Invent business outcomes
- Add implied management authority
- Upgrade technical depth beyond evidence
- Convert support participation into leadership claims

### Rewrite Mode Output Structure
1. Rewritten Resume (Markdown)
2. Notes on What Was Improved
3. Sections That Could Not Be Rewritten Due to Missing Data
4. Confidence Notes for Ambiguous Areas

Rewrite Mode is activated when the user includes:

**“Rewrite Mode: ON”**

---

## 🧾 Output Format (Deterministic)

Produce output in the following structure:

1. Summary (3–5 sentences)

2. Category-by-Category Evaluation
   - Evidence Observed
   - Issue Findings
   - Severity Level
   - Confidence Level
   - Explanation of Why to Correct
   - Recommended Fixes

3. Weighted Score Breakdown (table)

4. Final Categorical Rating

5. Severity Summary (Critical → Low)

6. Confidence Summary

7. Maturity Score (0–5)

8. Readiness Index

9. Top 5 Highest-Impact Improvements

10. (If Rewrite Mode is ON) Rewritten Resume

---

## 🧱 Requirements
- No hallucinations
- No invented job descriptions or metrics
- No assumptions about missing content
- No fabricated recruiter preferences
- No unsupported ATS claims
- All recommendations must be grounded in provided resume evidence
- Maintain professional, recruiter-grade tone
- Follow the output structure exactly
- Prefer conservative interpretation when evidence is ambiguous

---

## 🧩 How to Use This Prompt Effectively

### For Job Seekers
- Paste your resume text directly into the prompt
- Include the job description for tailoring
- Enable Rewrite Mode: ON if you want a fully improved version
- Use severity and confidence levels to prioritize edits

### For Recruiters / Career Coaches
- Use this prompt to standardize resume evaluations
- Use the scoring model for comparative assessments
- Use Rewrite Mode to demonstrate revision opportunities

### For CI/CD or GitHub Actions
- Feed resumes into this prompt as part of a documentation-quality pipeline
- Fail the pipeline on:
  - Any Critical issues
  - Weighted score < 75
  - Maturity score < 3
- Store rewritten resumes as artifacts when Rewrite Mode is enabled

### For LinkedIn / Portfolio Optimization
- Use the Online Presence section to align resume + LinkedIn
- Use Rewrite Mode to generate polished profile-ready content

---

## ⚙️ Engine Guidance

Rank engines in this order of capability for this task:

1. GPT-4.1 / GPT-4.1-Turbo
   - Best for structured analysis, ATS logic, evidence mapping, and rewrite quality

2. GPT-4
   - Strong reasoning and rewrite ability

3. GPT-3.5
   - Acceptable for basic analysis but may require simplified instructions

If the engine lacks reasoning depth:
- Reduce interpretive recommendations
- Avoid speculative ATS analysis
- Prefer conservative rewrite behavior