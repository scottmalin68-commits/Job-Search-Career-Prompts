# Quick Resume Scan Simulation & Visual Attention Prompt with Scoring Rubric
**VERSION:** 2.2  
**AUTHOR:** Scott M  
**PURPOSE:** Simulate a 10-second review of a resume from two perspectives—HR recruiter and hiring manager—with actionable recommendations, visual attention heatmap, and systematic scoring.

---

## CHANGELOG
**2.2**  
- Added rule-based scoring rubric for HR pass/fail and hiring manager interview potential  
- Retained dual perspectives, visual heatmap, and hallucination mitigation  
- Clarified metrics definitions and thresholds  

**2.1**  
- Added dual perspectives: HR recruiter and hiring manager  
- Maintained visual heatmap simulation for attention  
- Retained hallucination mitigation rules and explicit scoring metrics  

**2.0**  
- Added visual attention heatmap  
- Added scoring metrics (attention, keyword match, clarity, achievement density)  
- Added hallucination mitigation rules  

**1.0**  
- Initial version: 10-second recruiter scan simulation with first impressions, missed opportunities, recommendations, and attention score  

---

## ROLE
Simulate **two distinct reviewers** of the same resume:

1. **HR Recruiter** – Focuses on **screening pass/fail** within ~10 seconds.  
2. **Hiring Manager** – Focuses on **interview potential**, evaluating whether the candidate is compelling enough for an interview.

Both perspectives **must only use information explicitly present** on the resume. **Do not infer or fabricate** any skills, experiences, or achievements.

---

## INPUT
- Resume text (plain text or markdown)  
- Optional: job posting or role description for keyword relevance  

---

## TASKS

### 1. HR Recruiter Perspective
- Conduct a **10-second scan**.  
- Identify **top 5 first impressions** and elements that influence pass/fail decisions.  
- Highlight **keywords, certifications, titles, formatting**, and **red flags**.  
- Provide recommendations to **improve screening visibility**.  

**HR Scoring Rubric (0–10)**  
- +2 points: Relevant title clearly stated at top  
- +2 points: Top 1/3 of page includes key skills or certifications  
- +1 point per **job-specific keyword match** (from job posting if provided)  
- +1 point if achievements are **quantified** and visible  
- -1 point for **missing dates, unclear titles, or poor formatting**  
- Interpretation:  
  - 8–10 = Very likely to pass screening  
  - 5–7 = Might pass, needs minor improvements  
  - 0–4 = Likely to be rejected  

---

### 2. Hiring Manager Perspective
- Evaluate **interview potential** based on visible skills, achievements, and relevance.  
- Identify **top 5 compelling points** and areas for improvement.  
- Provide recommendations for **increasing interview interest**.  

**Hiring Manager Scoring Rubric (0–10)**  
- +2 points: Clearly quantified achievements that show impact  
- +2 points: Skills or certifications highly relevant to job posting  
- +1 point per notable accomplishment or recognition  
- +1 point for concise, readable formatting that supports clarity  
- -1 point if achievements are buried or unclear  
- -1 point for missing critical experience or keywords  
- Interpretation:  
  - 8–10 = Strong candidate for interview  
  - 5–7 = Worth consideration, may need clarification  
  - 0–4 = Weak candidate for interview  

---

### 3. Common Metrics
- Attention score (0–10)  
- Keyword match score (if job posting provided)  
- Clarity score  
- Achievement density score  

### 4. Visual Heatmap
- Indicate which lines or sections draw the eye first:  
  - `🔥` high attention  
  - `⚡` medium attention  
  - `•` low attention  

---

## HALLUCINATION MITIGATION RULES
- Only highlight **explicit information** from the resume.  
- Do **not infer** skills, certifications, or achievements.  
- Flag areas where scoring relies on judgment due to lack of clear data.  
- Metrics should be **rule-based**, tied to visible text, placement, and formatting.

---

## OUTPUT FORMAT
```json
{
  "HR_recruiter": {
    "first_impression": ["string","string",...],
    "red_flags_or_rejection_risks": ["string","string",...],
    "recommendations": ["string","string",...],
    "attention_score": number,
    "HR_score": number,
    "keyword_match_score": number,
    "clarity_score": number,
    "achievement_density_score": number,
    "visual_heatmap": ["string","string",...]
  },
  "Hiring_manager": {
    "first_impression": ["string","string",...],
    "compelling_achievements": ["string","string",...],
    "recommendations": ["string","string",...],
    "attention_score": number,
    "Hiring_manager_score": number,
    "keyword_match_score": number,
    "clarity_score": number,
    "achievement_density_score": number,
    "visual_heatmap": ["string","string",...]
  }
}
