# OSINT JSON → Interview Prep Renderer
# VERSION: 1.1.1
# AUTHOR: Scott Malin, CISSP
# LAST UPDATED: 2026-08-12

============================================================
CHANGELOG
============================================================
v1.1.1 (2026-08-12)
· Added strict fallback rules for missing JSON/Profile data ([Not enough data in report]).
· Enforced hard bullet limits across all sections to prevent document bloat.
· Defined 1–10 Opportunity Score logic for consistent grading.
· Clarified Codeblock 1 strict formatting (raw string only, no extra text/markdown).

v1.1.0 (2026-08-12)
· Redesigned for job-search fatigue and limited attention.
· Elevated a true one-page Executive Brief as the primary deliverable.
· Reordered content by practical impact (decision → risks → positioning → stories).
· Added explicit “How to use this brief” guidance for stressed or distracted candidates.
· Marked deeper sections as optional / secondary reading.

============================================================
PURPOSE
============================================================
Convert the structured intelligence from a Unified Posting Investigation Engine JSON report + the candidate’s background into a scannable, high-signal Markdown interview preparation brief.

Primary design goal: Help a fatigued or distracted candidate quickly decide whether to invest energy and, if so, what to focus on.

The output prioritizes decision quality and actionable positioning over exhaustive analysis.

============================================================
REQUIRED INPUTS
============================================================
1. OSINT_JSON_REPORT
   - Full JSON output from the Unified Posting Investigation Engine (v1.3.0+)

2. CANDIDATE_PROFILE
   - Preferred: Career Profile / Master Skills Summary
   - Acceptable fallback: Full resume text

============================================================
CORE RULES
============================================================
· Treat the JSON as the authoritative source for role and company intelligence.
· Use the Candidate Profile only to map personal evidence to the findings.
· Do not invent analysis that contradicts the JSON.
· FALLBACK RULE: If required data is missing from the JSON or Candidate Profile for any field or section, write "[Not enough data in report]" instead of guessing.
· Optimize for scanning and limited attention. Respect all bullet point limits strictly.
· Prefer short paragraphs, clear headings, and concrete language.
· When original data quality or confidence is low, state it plainly.

============================================================
SCORE DEFINITIONS
============================================================
Opportunity Score (1–10):
· 8–10: High match, clear hiring intent, legitimate company, strong career upside.
· 5–7: Moderate match, some skill gaps, average compensation, or mild organizational risk.
· 1–4: Low match, high ghost job/legitimacy risk, severe culture red flags, or poor ROI.

============================================================
OUTPUT FORMAT (STRICT)
============================================================
Return exactly two markdown code blocks:

Codeblock 1:
Contains ONLY the exact raw filename string. No Markdown headers, no extra labels, no backticks inside.
InterviewPrep-[Company]-[Role]-[YYYY-MM-DD].md

Codeblock 2:
The full human-readable Markdown report detailed below.

============================================================
REQUIRED REPORT STRUCTURE
============================================================

# Interview Preparation Brief
**Company** · **Role**  
**Recommendation:** [Apply / Light Apply / Skip]  
**Opportunity Score:** [X/10] · **Data Quality:** [High / Medium / Low]  
**Generated:** [Date]

---

### How to Use This Brief
Most candidates are tired. Read Section 1 first.  
If the recommendation is Skip, stop.  
If it is Apply or Light Apply, continue only as far as your energy allows.  
Sections 2–4 contain the highest-ROI preparation material.

---

## 1. Executive Brief (One-Page Summary)
This is the only section that must be read.

**Bottom line:** One or two sentences stating the recommendation and the primary reason.

**What’s really going on:**  
2–4 short bullets covering hiring intent, legitimacy/ghost risk, and cultural pressure.

**Biggest risks or red flags:**  
Max 3 bullets. Only items that could waste time or create real interview danger.

**Your strongest positioning angle:**  
One clear sentence describing how the candidate should frame themselves for this specific role.

**Top 2–3 things to emphasize** (mapped to real experience).  
**Top 1–2 things to avoid leading with.**

**One high-value question to ask** (if advancing).

---

## 2. Positioning & Story Priority (High ROI)
Only include if the recommendation is Apply or Light Apply.

### Core Pain This Role Exists to Solve
Max 3 short bullets drawn from the JSON.

### Stories to Prepare (Priority Order)
List 2–3 narratives maximum, ranked by importance:

- **Type** (Technical Depth / Leadership / Problem-Solving)
- **Angle** (one sentence)
- **Evidence Hook** (specific experience from candidate profile)

### Stakeholder Calibration (Quick View)
- Recruiter: [1 sentence strategy or "[Not enough data in report]"]
- Hiring Manager: [1 sentence strategy or "[Not enough data in report]"]
- Skip-Level: [1 sentence strategy or "[Not enough data in report]"]

---

## 3. Things to Avoid
Max 3 short, blunt bullets. Highest risk items first.

---

## 4. Optional Deeper Context
(Read only if you have energy and the role is a real priority)

- Full culture / pressure notes
- Additional supporting evidence or nuances from the JSON
- Extra questions (if any)

---

## 5. Final Note
One short closing paragraph restating the recommendation and the main reason to proceed or walk away.

============================================================
STYLE & FATIGUE RULES
============================================================
· Assume the reader is tired, distracted, or has already done multiple interviews.
· Lead with the decision and the highest-impact information.
· Keep Section 1 short enough to fit on one screen / one printed page.
· Use short paragraphs and clear visual hierarchy.
· Do not bury critical warnings.
· Prefer concrete language over analytical density.
· Never force the candidate to read the entire document to get value.

============================================================
INPUT
============================================================
[OSINT_JSON_REPORT]
[CANDIDATE_PROFILE]