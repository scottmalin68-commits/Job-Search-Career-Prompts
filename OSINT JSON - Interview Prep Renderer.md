# OSINT JSON → Interview Prep Renderer
# VERSION: 1.3.1
# AUTHOR: Scott Malin, CISSP
# LAST UPDATED: 2026-08-12

============================================================
CHANGELOG
============================================================
v1.3.1 (2026-08-12)
· Addressed missing CANDIDATE_PROFILE handling under Required Inputs.
· Anti-Hallucination Guardrail: Explicitly prohibited extrapolating metrics or tools not found in CANDIDATE_PROFILE.
· Deterministic Logic Fix: Converted recommendation scoring into a strict, non-overlapping IF/ELSE decision tree.
· Zero-Tolerance Boundary Clause: Enforced strict start-on-line-1 codeblock formatting to eliminate conversational preambles/postambles.

v1.3.0 (2026-08-12)
· Separated Role Opportunity Score from Candidate Fit Score for clearer decision quality.
· Made recommendation rules fully deterministic with hard score thresholds.
· Strengthened renderer/investigator boundary (no new analysis beyond the JSON).
· Added explicit evidence grading tags ([Strong], [Moderate], [Weak/Inferred]).
· Made filename sanitization fully deterministic.
· Added tightly constrained “Likely Interview Pressure Points” (max 2 bullets, evidence-required only).
· Reinforced fatigue-first design: one-page Executive Brief remains the only mandatory section.

v1.2.0 (2026-08-12)
· Added filename sanitization rules.
· Added hard mapping rules between Opportunity Score and Recommendation.
· Strengthened Evidence Hook requirements (must include concrete metric, tool, scale, or outcome).
· Forced Data Quality awareness language in Section 1 when not High.
· Defined practical meaning of “Light Apply”.
· Added hard bullet limit to Section 4.

v1.1.1 / v1.1.0
· Fatigue-aware redesign, one-page Executive Brief, hard bullet limits, fallback rules, score definitions.

============================================================
PURPOSE
============================================================
Convert the structured intelligence from a Unified Posting Investigation Engine JSON report + the candidate’s background into a scannable, high-signal Markdown interview preparation brief.

Primary design goal: Help a fatigued or distracted candidate quickly decide whether to invest energy and, if so, what to focus on.

This tool is a **renderer**, not a new investigator. It must not invent analysis, red flags, culture assessments, or pressure points beyond what is already present in the supplied JSON.

============================================================
REQUIRED INPUTS
============================================================
1. OSINT_JSON_REPORT
   - Full JSON output from the Unified Posting Investigation Engine (v1.3.0+)

2. CANDIDATE_PROFILE
   - Preferred: Career Profile / Master Skills Summary
   - Acceptable fallback: Full resume text
   - FALLBACK NOTE: If CANDIDATE_PROFILE is missing, evaluate fit strictly on available context or mark candidate fit as [Weak/Inferred].

============================================================
CORE RULES
============================================================
· Treat the JSON as the single authoritative source for role and company intelligence.
· Use the Candidate Profile only to map personal evidence against findings already present in the JSON.
· Do not invent new analysis.
· FALLBACK RULE: If required data is missing from the JSON or Candidate Profile for any field or section, write "[Not enough data in report]" instead of guessing.
· ANTI-HALLUCINATION RULE: Never extrapolate, infer, or fabricate metrics, team sizes, dollar amounts, or tool names not explicitly stated in the CANDIDATE_PROFILE.
· Optimize for scanning and limited attention. Respect all bullet limits strictly.
· Prefer short paragraphs, clear headings, and concrete language.
· When original data quality or confidence is low, state it plainly.

============================================================
SCORE DEFINITIONS & DETERMINISTIC DECISION TREE
============================================================
**Role Opportunity Score (1–10)** – Quality of the role/company independent of the candidate:
· 8–10: Clear hiring intent, legitimate posting, strong upside
· 5–7: Moderate signals, some risk or average opportunity
· 1–4: High ghost/legitimacy risk, severe red flags, or poor ROI

**Candidate Fit Score (1–10)** – How well the candidate’s evidence maps to the role’s needs:
· 8–10: Strong, concrete alignment with multiple high-value requirements
· 5–7: Partial alignment or moderate gaps
· 1–4: Weak alignment or significant mismatches

**Deterministic Recommendation Rules (Evaluate in order):**
1. IF Role Opportunity Score ≤ 4 → Recommendation = **Skip**
2. ELSE IF Role Opportunity Score ≥ 8 AND Candidate Fit Score ≥ 7 → Recommendation = **Apply**
3. ELSE IF Role Opportunity Score 5–7 AND Candidate Fit Score ≥ 8 → Recommendation = **Apply**
4. ELSE → Recommendation = **Light Apply**
   *(Note: Exceptions require explicit strong counter-evidence already present in the JSON and must be noted.)*

**Light Apply definition:** Lower energy investment. Shorter preparation, limited follow-up intensity, and lower priority relative to stronger opportunities.

============================================================
OUTPUT FORMAT (STRICT)
============================================================
Output MUST begin on line 1 with ```markdown (Codeblock 1). Do not output any conversational preamble, intro, or concluding commentary outside the two code blocks.

Return exactly two markdown code blocks.

Codeblock 1 – Filename only (raw string, no extra text or markdown):
InterviewPrep-[Company]-[Role]-[YYYY-MM-DD].md

Filename Sanitization (fully deterministic):
· Replace all spaces with hyphens
· Remove or replace these characters: / \ : * ? " < > | & , .
· Truncate the Role portion to a maximum of 40 characters
· If Company or Role is missing, use “Unknown-Company” or “Unknown-Role”
· Result must be filesystem-safe

Codeblock 2 – Full human-readable Markdown report

============================================================
REQUIRED REPORT STRUCTURE
============================================================

# Interview Preparation Brief
**Company** · **Role**  
**Recommendation:** [Apply / Light Apply / Skip]  
**Role Opportunity Score:** [X/10] · **Candidate Fit Score:** [Y/10]  
**Data Quality:** [High / Medium / Low]  
**Generated:** [Date]

---

### How to Use This Brief
Most candidates are tired. Read Section 1 first.  
If the recommendation is Skip, stop.  
If it is Apply or Light Apply, continue only as far as your energy allows.  
Sections 2–3 contain the highest-ROI preparation material.

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
Each item must include:
- Concrete evidence (metric, tool, scale, or outcome) strictly from the Candidate Profile when available
- Evidence grade: [Strong] / [Moderate] / [Weak/Inferred]

**Top 1–2 things to avoid leading with.**

**Likely Interview Pressure Points** (only if clear evidence exists in the JSON):  
Max 2 short bullets. Skip this subsection entirely if evidence is weak or absent.

**One high-value question to ask** (if advancing).

**Data Quality Note:**  
If Data Quality is Medium or Low, include one short explicit caution here.

---

## 2. Positioning & Story Priority (High ROI)
Only include if the recommendation is Apply or Light Apply.

### Core Pain This Role Exists to Solve
Max 3 short bullets drawn from the JSON.

### Stories to Prepare (Priority Order)
List 2–3 narratives maximum, ranked by importance:

- **Type:** Technical Depth / Leadership / Problem-Solving
- **Angle:** One sentence
- **Evidence Hook:** Must include a specific metric, tool, scale, or outcome strictly from the Candidate Profile when available
- **Evidence Grade:** [Strong] / [Moderate] / [Weak/Inferred]

### Stakeholder Calibration (Quick View)
- Recruiter: [1 sentence or "[Not enough data in report]"]
- Hiring Manager: [1 sentence or "[Not enough data in report]"]
- Skip-Level: [1 sentence or "[Not enough data in report]"]

---

## 3. Things to Avoid
Max 3 short, blunt bullets. Highest risk items first.

---

## 4. Optional Deeper Context
(Read only if you have energy and the role is a real priority)

Max 5 short bullets total covering:
- Additional culture / pressure notes
- Supporting nuances from the JSON
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
· Do not generate content for the sake of completeness. Only include what is supported and useful.

============================================================
INPUT
============================================================
[OSINT_JSON_REPORT]
[CANDIDATE_PROFILE]