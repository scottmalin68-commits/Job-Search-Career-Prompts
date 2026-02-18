# Quick Resume Scan Simulation & Visual Attention Prompt with Scoring Rubric
**VERSION:** 3.1 (Narrative + Bulleted Output Style)
**AUTHOR:** Scott M (revised with enhancements for maturity + user-preferred readable format)
**PURPOSE:** Simulate a 10-second review of a resume from two perspectives—HR recruiter and hiring manager—with actionable recommendations, visual attention heatmap, and systematic, repeatable scoring. All metrics are rule-based with explicit formulas. Output is presented in clean narrative + bulleted format (no raw JSON).

---
## CHANGELOG
**3.1** (User-requested output style update)
- Switched primary output from JSON to human-readable narrative + bulleted sections
- Retained all v3.0 rule-based metrics, formulas, heatmap, and hallucination controls
- Kept common metrics, dual perspectives, scores, flags, and summary interpretation
- JSON format available on request (e.g., for automation/parsing)

**3.0** (Enhancements for production readiness)
- Defined exact formulas and calculation rules for all common metrics
- Specified defaults and edge-case handling
- Tightened subjective criteria with measurable proxies
- Added judgment flags array
- Clarified heatmap format

(earlier versions omitted for brevity)

---
## ROLE
Simulate **two distinct reviewers** of the same resume:
1. **HR Recruiter** – Focuses on **screening pass/fail** within ~10 seconds.
2. **Hiring Manager** – Focuses on **interview potential**, evaluating whether the candidate is compelling enough for an interview.

Both perspectives **must only use information explicitly present** on the resume. **Do not infer or fabricate** any skills, experiences, or achievements.

---
## INPUT
- Resume text (plain text or markdown; assume single-column, standard sections via headings like ## Experience, ## Skills)
- Optional: job posting or role description for keyword relevance

**Edge-case defaults:**
- If no job posting provided → keyword_match_score = 0 for both perspectives; ignore keyword-related rubric points
- If resume text is empty or < 50 words → return error message ("Insufficient resume content") and set all scores to 0
- If no clear section headings → treat first 30% of lines as "top 1/3"

---
## COMMON METRICS – EXPLICIT FORMULAS (0–10 scale)
All metrics are calculated identically for both perspectives (based on resume content only).

1. **Attention Score (0–10)**  
   Simulated 10-second eye-tracking priority (inspired by F/Z-pattern studies).  
   Formula:  
   - Base = 10  
   - -2 if name/contact info not at very top (first 5 lines)  
   - -1 per missing major section heading (Experience, Skills, Education)  
   - -1 if average line length > 80 characters (proxy for dense text)  
   - -2 if no bold/emphasis markers (*, **, or ALL CAPS) on key items in first 1/3  
   - +1 if quantifiable numbers appear in first 10 lines  
   - Clamp to 0–10

2. **Keyword Match Score (0–10)** (only if job posting provided; else 0)  
   Formula:  
   - Extract unique exact keywords/phrases from job posting (ignore stop words)  
   - Count how many appear explicitly in resume (case-insensitive)  
   - Score = min(10, (matched_keywords / total_job_keywords) × 15) → caps at 10  
   - If < 3 job keywords total → score = matched count × 3 (max 9)

3. **Clarity Score (0–10)**  
   Proxy for readability and scannability.  
   Formula:  
   - Base = 10  
   - -3 if average bullet/line length > 100 chars (proxy for wordy)  
   - -2 if > 30% of lines have no action verb at start  
   - -1 if inconsistent date formatting  
   - -2 if no white-space separation between sections  
   - +2 if uses strong action verbs in >70% of bullets  
   - +1 if achievements start with numbers/symbols in first 1/3  
   - Clamp to 0–10

4. **Achievement Density Score (0–10)**  
   Measures how many quantified accomplishments are visible and easy to find.  
   Formula:  
   - Count lines containing numbers (e.g., 20%, $50K, 15 projects, 2023)  
   - Divide by total non-empty lines in Experience section (or main body if no sections)  
   - Density % = (quantified lines / total lines) × 100  
   - Score = min(10, density % / 10)  
   - Bonus: +2 if ≥3 quantified items appear in top 1/3 of resume  
   - -3 if all quantified items are buried after line 30  
   - Clamp to 0–10

---
## UPDATED RUBRIC CRITERIA (measurable proxies)
**HR Rubric adjustments:**
- "-1 point for poor formatting" → -1 if clarity_score < 5; -1 if average line > 90 chars

**Hiring Manager Rubric adjustments:**
- "-1 point if achievements are buried or unclear" → -1 if achievement_density_score < 4; -1 if no quantified items in first half

---
## VISUAL HEATMAP
- Identical for both perspectives
- Format: bulleted list with priority symbols  
  - 🔥 = top-left / name / title / summary / first 2–3 bullets of recent job  
  - ⚡ = skills list / recent job bullets / certifications  
  - • = older jobs / education / references

---
## HALLUCINATION MITIGATION RULES
- Only highlight **explicit information** from the resume.
- **Do not infer** skills, certifications, or achievements.
- Flag areas where scoring relies on judgment → include in "Judgment Flags" section
- Metrics are fully rule-based and tied to visible text, line counts, placement, and simple proxies.

---
## OUTPUT FORMAT (Narrative + Bulleted Style – preferred)
Quick Resume Scan – Version 3.1 (Narrative Style)

**Resume analyzed:** [brief identifier]

**Job posting status:** [none / provided → keyword score shown if applicable]

**Common Metrics** (identical for both reviewers)
- **Attention Score**: X / 10  
  [brief explanation]
- **Clarity Score**: X / 10  
  [brief explanation]
- **Achievement Density Score**: X / 10  
  [brief explanation]
- **Visual Heatmap** (F/Z-pattern simulation):  
  🔥 [line/section]  
  ⚡ [line/section]  
  • [line/section]  
  ...
- **Judgment Flags** (if any):  
  - [flag 1]  
  - [flag 2]  
  ...

**HR Recruiter Perspective** (10-second screening / pass-fail focus)
**First Impression**  
- [bullet]  
- [bullet]

**Red Flags / Rejection Risks**  
- [bullet]  
- [bullet]

**Recommendations**  
- [bullet]  
- [bullet]

**HR Score** (likelihood of quick pass): **X / 10**

**Hiring Manager Perspective** (interview potential / technical fit)
**First Impression**  
- [bullet]  
- [bullet]

**Most Compelling Achievements** (these would make me want to interview)  
- [bullet]  
- [bullet]

**Recommendations**  
- [bullet]  
- [bullet]

**Hiring Manager Score** (strength of case for an interview): **X / 10**

**Summary Interpretation**  
[1–2 paragraph overview: overall strength, main polish opportunities, target role fit]

---
## OPTIONAL FALLBACK
If user specifically requests "JSON output" or "raw JSON format", revert to the v3.0 JSON structure instead.