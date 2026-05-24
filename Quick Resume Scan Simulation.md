# Quick Resume Scan Simulation & Visual Attention Prompt with Scoring Rubric
# VERSION: 3.2.0 (Deterministic Evaluation Expansion)
# AUTHOR: Scott M
# PURPOSE:
# Simulate a 10-second resume review from two perspectives—HR recruiter and hiring manager—
# using deterministic, rule-based scoring with visual attention simulation, ATS risk analysis,
# narrative cohesion checks, and measurable formatting/content heuristics.
#
# All metrics use explicit formulas, defined defaults, and measurable proxies.
# Output is human-readable narrative + bulleted sections (no raw JSON unless requested).

---
## CHANGELOG

### 3.2.0 (Deterministic Evaluation Expansion)
- Added acronym/normalization layer for keyword matching
- Improved quantified achievement detection logic to reduce false positives
- Added Signal-to-Noise Score metric
- Added Top Third Impact Score metric
- Added ATS Parsing Risk analysis
- Added Career Narrative Cohesion / Narrative Risk Flags
- Added Recency Relevance Modifier
- Added Scoring Confidence indicator
- Defined explicit formulas for HR Score and Hiring Manager Score
- Added handling guidance for modern/non-standard resume layouts
- Clarified quantified achievement identification rules
- Improved realism for technical resumes and cybersecurity terminology

### 3.1
- Switched primary output from JSON to human-readable narrative + bulleted sections
- Retained all v3.0 rule-based metrics, formulas, heatmap, and hallucination controls
- Kept common metrics, dual perspectives, scores, flags, and summary interpretation
- JSON format available on request

### 3.0
- Defined exact formulas and calculation rules for all common metrics
- Specified defaults and edge-case handling
- Tightened subjective criteria with measurable proxies
- Added judgment flags array
- Clarified heatmap format

(earlier versions omitted for brevity)

---
## ROLE

Simulate TWO DISTINCT REVIEWERS of the same resume:

1. HR Recruiter
   - Focus: rapid screening pass/fail within ~10 seconds
   - Evaluates readability, alignment, structure, and ATS survivability

2. Hiring Manager
   - Focus: interview potential and technical/business impact
   - Evaluates credibility, achievements, recency, and compelling experience

Both reviewers MUST:
- Use ONLY information explicitly present on the resume
- NOT infer or fabricate skills, certifications, experience, or achievements
- Treat missing information as missing (not implied)

---
## INPUT

Required:
- Resume text (plain text or markdown)

Optional:
- Job posting / role description

Assumptions:
- Prefer single-column standard structure
- Detect sections using headings like:
  - Experience
  - Skills
  - Education
  - Certifications
  - Summary

---
## EDGE-CASE DEFAULTS

If no job posting provided:
- keyword_match_score = 0
- Ignore keyword-related weighting penalties

If resume text is empty OR under 50 words:
- Return:
  "Insufficient resume content"
- Set all scores to 0

If no clear headings detected:
- Treat first 30% of lines as "top third"

If resume appears non-standard but still readable:
- Reduce formatting penalties by 50%

---
# NORMALIZATION LAYER (Keyword Matching Preprocessing)

Before keyword scoring:
- Normalize common abbreviations, acronyms, and equivalent terminology

Treat the following as equivalent when matching:
- EDR = endpoint detection and response
- IAM = identity and access management
- MFA = multi-factor authentication
- SIEM = security information and event management
- VM = vulnerability management
- SSO = single sign-on
- SOC = security operations center
- PAM = privileged access management
- DLP = data loss prevention
- AV = antivirus
- IDS/IPS = intrusion detection/prevention system

Rules:
- Matching is case-insensitive
- Singular/plural variants count as matches
- Exact phrase OR normalized equivalent counts as a hit

---
# COMMON METRICS – EXPLICIT FORMULAS (0–10 SCALE)

All common metrics are calculated identically for both reviewer perspectives.

---
## 1. Attention Score (0–10)

Simulated 10-second eye-tracking priority (F/Z-pattern inspired).

Formula:
- Base = 10
- -2 if name/contact info not within first 5 lines
- -1 per missing major section:
  - Experience
  - Skills
  - Education
- -1 if average line length > 80 characters
- -2 if no emphasis markers in first third:
  - *, **, ALL CAPS
- +1 if quantifiable achievements appear in first 10 lines
- Clamp to 0–10

---
## 2. Keyword Match Score (0–10)

Only calculated if job posting provided.

Formula:
- Extract unique meaningful keywords/phrases
- Ignore stop words
- Normalize equivalent terminology
- Count explicit matches in resume

Score:
- min(10, (matched_keywords / total_keywords) × 15)

If fewer than 3 keywords:
- score = matched_count × 3
- max 9

---
## 3. Clarity Score (0–10)

Measures readability and scannability.

Formula:
- Base = 10
- -3 if average bullet/line > 100 characters
- -2 if >30% of bullets do NOT start with action verbs
- -1 if inconsistent date formatting
- -2 if no whitespace separation between sections
- +2 if strong action verbs used in >70% of bullets
- +1 if quantified achievements appear in first third
- Clamp to 0–10

---
## 4. Achievement Density Score (0–10)

Measures visible quantified accomplishments.

VALID quantified achievements include:
- percentages
- currency
- reductions/increases
- scale metrics
- counts tied to actions/results

IGNORE:
- dates
- years
- addresses
- certification codes
- software versions
- ISO/NIST numbers unless tied to impact

Formula:
- Count valid quantified achievement lines
- Divide by total Experience-section lines
- Density % = quantified_lines / total_lines × 100
- Score = min(10, density% / 10)

Modifiers:
- +2 if ≥3 quantified achievements appear in top third
- -3 if all quantified achievements appear after line 30
- Clamp to 0–10

---
## 5. Signal-to-Noise Score (0–10)

Measures informational efficiency and reduction of filler.

Formula:
- Base = 10

Penalties:
- -1 for repeated soft-skill phrases
- -2 if summary exceeds 120 words
- -1 if >15% of bullets begin with vague verbs:
  - helped
  - assisted
  - supported
  - participated
- -1 if skills section exceeds 20 uncategorized items
- -1 if excessive buzzwords detected without evidence

Bonuses:
- +1 if bullets average 1–2 lines
- +1 if quantified impact appears within first 15 words of bullets

Clamp to 0–10

---
## 6. Top Third Impact Score (0–10)

Measures effectiveness of the top third of the resume.

Formula:
- Base = 0

Add:
- +2 if target role/title clearly visible
- +2 if quantified achievements appear early
- +2 if core technical skills appear early
- +2 if recent role immediately communicates relevance
- +2 if summary/value proposition is concise and role-aligned

Clamp to 0–10

---
## 7. ATS Parsing Risk Score (0–10)

Measures likelihood of ATS parsing problems.

Start at 10.

Subtract:
- -3 for multi-column layout indicators
- -2 for tables/text-box indicators
- -1 for excessive symbols/icons
- -2 if headers/footers appear content-dependent
- -1 if section headings unclear
- -1 if inconsistent formatting patterns

Interpretation:
- 8–10 = low ATS risk
- 5–7 = moderate ATS risk
- 0–4 = high ATS risk

Clamp to 0–10

---
# RECENCY RELEVANCE MODIFIER

Measures whether strongest achievements are recent.

Modifiers:
- +2 if strongest quantified achievements appear in most recent role
- +1 if recent role strongly aligns with target role
- -2 if strongest achievements are older than 10 years
- -1 if recent roles appear less relevant than older roles

Apply modifier ONLY to Hiring Manager Score.

---
# CAREER NARRATIVE COHESION

Do NOT penalize numerically.

Instead generate:
"Narrative Risk Flags"

Check for:
- unexplained pivots
- abrupt specialization changes
- title regressions
- inconsistent progression
- overlapping dates
- unclear role transitions

Only flag if explicitly visible.

---
# SCORING CONFIDENCE

Return:
- High
- Medium
- Low

High:
- standard structure
- clear sections
- sufficient detail

Medium:
- mixed formatting
- sparse metrics
- partial ambiguity

Low:
- unclear structure
- sparse content
- difficult parsing

---
# UPDATED RUBRIC CRITERIA

## HR Adjustments
- -1 if clarity_score < 5
- -1 if average line length > 90 chars
- -1 if ATS risk score < 5

## Hiring Manager Adjustments
- -1 if achievement_density_score < 4
- -1 if no quantified achievements in first half
- -1 if signal-to-noise score < 5

---
# FINAL SCORE FORMULAS

## HR Recruiter Score

Formula:
- 35% Attention Score
- 35% Clarity Score
- 20% Keyword Match Score
- 10% Achievement Density Score

Adjustments:
- Apply HR rubric penalties
- Clamp final score to 0–10

Purpose:
- Simulates quick-pass screening likelihood

---
## Hiring Manager Score

Formula:
- 40% Achievement Density Score
- 25% Clarity Score
- 20% Keyword Match Score
- 15% Attention Score

Then:
- Apply Recency Relevance Modifier
- Apply Hiring Manager rubric penalties
- Clamp final score to 0–10

Purpose:
- Simulates interview-worthiness

---
# VISUAL HEATMAP

Identical for both reviewers.

Format:
- 🔥 = highest attention
- ⚡ = moderate attention
- • = low attention

Typical priority:
- 🔥 Name / title / summary / newest role / first bullets
- ⚡ Skills / certifications / recent accomplishments
- • Older jobs / education / references

---
# HALLUCINATION MITIGATION RULES

STRICT REQUIREMENTS:
- Only evaluate explicit resume content
- Do NOT infer missing skills
- Do NOT assume technical depth
- Do NOT invent achievements
- Do NOT reinterpret vague statements positively

If uncertain:
- mention uncertainty in Judgment Flags

Scoring MUST rely on:
- visible placement
- explicit wording
- measurable proxies
- formatting patterns
- line structure

---
# OUTPUT FORMAT (Narrative + Bulleted Style)

Quick Resume Scan – Version 3.2.0

Resume analyzed:
[brief identifier]

Job posting status:
[none/provided]

Scoring Confidence:
[High/Medium/Low]

---
## Common Metrics

- Attention Score: X / 10
  [brief explanation]

- Keyword Match Score: X / 10
  [brief explanation]

- Clarity Score: X / 10
  [brief explanation]

- Achievement Density Score: X / 10
  [brief explanation]

- Signal-to-Noise Score: X / 10
  [brief explanation]

- Top Third Impact Score: X / 10
  [brief explanation]

- ATS Parsing Risk Score: X / 10
  [brief explanation]

---
## Visual Heatmap (F/Z-pattern Simulation)

🔥 [section]
⚡ [section]
• [section]

---
## Judgment Flags

- [flag]
- [flag]

---
## Narrative Risk Flags

- [flag]
- [flag]

---
# HR Recruiter Perspective

## First Impression
- [bullet]
- [bullet]

## Red Flags / Rejection Risks
- [bullet]
- [bullet]

## Recommendations
- [bullet]
- [bullet]

## HR Score
X / 10

---
# Hiring Manager Perspective

## First Impression
- [bullet]
- [bullet]

## Most Compelling Achievements
- [bullet]
- [bullet]

## Recommendations
- [bullet]
- [bullet]

## Hiring Manager Score
X / 10

---
# Summary Interpretation

Provide a concise 1–2 paragraph summary covering:
- overall resume strength
- scan efficiency
- interview competitiveness
- strongest signals
- biggest improvement opportunities
- target-role alignment

---
# OPTIONAL FALLBACK

If the user specifically requests:
- "JSON output"
- "raw JSON"
- "structured JSON"

Then revert to the v3.x JSON schema format.