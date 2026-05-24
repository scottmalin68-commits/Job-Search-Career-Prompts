# Quick Resume Scan Simulation & Visual Attention Prompt with Scoring Rubric
# VERSION: 3.2.1 (Anti-Drift & Deterministic Calibration)
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

### 3.2.1 (Anti-Drift & Deterministic Calibration)
- Added mandatory SCORING PROTOCOL scratchpad block to eliminate AI calculation drift
- Quantified "excessive buzzwords" to exactly >5 unmeasured corporate buzzwords
- Defined "inconsistent formatting patterns" to explicitly mean shifting date formats or bullet styles
- Tied Visual Heatmap to deterministic line ranges and sections instead of subjective generation
- Patched math edge cases (division-by-zero for 0 keywords, and base/bonus clamping calibration)

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

If no job posting provided OR total_keywords calculated is 0:
- keyword_match_score = 0
- Ignore keyword-related weighting penalties entirely

If resume text is empty OR under 50 words:
- Return: "Insufficient resume content"
- Set all scores to 0 and terminate execution

If no clear headings detected:
- Treat first 30% of lines as "top third" for all calculations

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
- -2 if no emphasis markers (*, **, ALL CAPS) used in the top third of the resume
- +1 if quantifiable achievements appear in first 10 lines
- Clamp final subtotal to a strict maximum of 10 and minimum of 0

---
## 2. Keyword Match Score (0–10)

Only calculated if job posting is provided and contains >0 valid keywords.

Formula:
- Extract unique meaningful keywords/phrases from job posting
- Ignore stop words
- Normalize equivalent terminology using the Normalization Layer
- Count explicit matches in resume

Score:
- If 3 or more total keywords extracted: score = min(10, (matched_keywords / total_keywords) * 15)
- If fewer than 3 keywords extracted: score = min(9, matched_count * 3)

---
## 3. Clarity Score (0–10)

Measures readability and scannability.

Formula:
- Base = 10
- -3 if average bullet/line > 100 characters
- -2 if >30% of bullets do NOT start with action verbs
- -1 if date formatting shifts patterns anywhere in document (e.g., mixing "MM/YYYY" with "Jan 2022")
- -2 if no whitespace separation between sections
- +2 if strong action verbs used in >70% of bullets
- +1 if quantified achievements appear in first third
- Clamp final subtotal to a strict maximum of 10 and minimum of 0

---
## 4. Achievement Density Score (0–10)

Measures visible quantified accomplishments.

VALID quantified achievements include:
- percentages, currency, reductions/increases, scale metrics, counts tied to actions/results

IGNORE:
- dates, years, addresses, certification codes, software versions, ISO/NIST framework numbers unless explicitly tied to a scale/impact metric

Formula:
- Count valid quantified achievement lines
- Divide by total Experience-section lines
- Density % = (quantified_lines / total_lines) * 100
- Score = min(10, density% / 10)

Modifiers:
- +2 if >=3 quantified achievements appear in the top third of the resume
- -3 if all quantified achievements appear after line 30
- Clamp final subtotal to a strict maximum of 10 and minimum of 0

---
## 5. Signal-to-Noise Score (0–10)

Measures informational efficiency and reduction of filler.

Formula:
- Base = 10

Penalties:
- -1 for repeated soft-skill phrases (e.g., "team player", "highly motivated" used >2 times)
- -2 if summary section exceeds 120 words
- -1 if >15% of bullets begin with vague verbs (helped, assisted, supported, participated)
- -1 if skills section exceeds 20 uncategorized items
- -1 if >5 corporate buzzwords (e.g., synergy, paradigm, dynamic, go-getter) appear without a linked metric or proof

Bonuses:
- +1 if bullets average 1–2 lines
- +1 if quantified impact appears within the first 15 words of a bullet

Clamp final subtotal to a strict maximum of 10 and minimum of 0

---
## 6. Top Third Impact Score (0–10)

Measures effectiveness of the top third of the resume (defined as lines 1-20 or first 30% of lines).

Formula:
- Base = 0

Add points incrementally:
- +2 if target role/title is clearly visible in the top third
- +2 if >=1 quantified achievements appear in the top third
- +2 if core technical skills appear in the top third
- +2 if the most recent role immediately communicates target relevance
- +2 if the summary/value proposition is concise (under 60 words) and role-aligned

Clamp final subtotal to a strict maximum of 10 and minimum of 0

---
## 7. ATS Parsing Risk Score (0–10)

Measures likelihood of ATS parsing problems based on text formatting patterns.

Formula:
- Base = 10

Subtract:
- -3 for clear multi-column text layout indicators
- -2 for visible tables, grids, or text-box styling structures
- -1 for excessive decorative symbols or non-standard icons
- -2 if headers/footers contain critical contact information or content dependencies
- -1 if section headings do not use standard plain-text titles
- -1 if bullet styles switch characters midway through a section

Interpretation:
- 8–10 = low ATS risk
- 5–7 = moderate ATS risk
- 0–4 = high ATS risk

Clamp final subtotal to a strict maximum of 10 and minimum of 0

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

Do NOT penalize numerically. Instead generate "Narrative Risk Flags" if explicitly visible:
- unexplained pivots, abrupt specialization changes, title regressions, inconsistent progression, overlapping dates, unclear role transitions.

---
# SCORING CONFIDENCE

Return High, Medium, or Low based on structural parsing clarity, presence of metrics, and ambiguity.

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
- (Attention Score * 0.35) + (Clarity Score * 0.35) + (Keyword Match Score * 0.20) + (Achievement Density Score * 0.10)
Adjustments:
- Apply HR rubric penalties
- Clamp final score to 0–10

## Hiring Manager Score
Formula:
- (Achievement Density Score * 0.40) + (Clarity Score * 0.25) + (Keyword Match Score * 0.20) + (Attention Score * 0.15)
Then:
- Add/subtract Recency Relevance Modifier
- Apply Hiring Manager rubric penalties
- Clamp final score to 0–10

---
# VISUAL HEATMAP DETERMINISTIC MAPPING RULES

Map elements using these strict text/position rules:
- 🔥 Highest Attention: Map to the top third of the document (lines 1-20 or first 30% of lines) AND any specific line item containing a valid quantified achievement.
- ⚡ Moderate Attention: Map to the remaining lines within the Experience and Skills sections that do not contain explicit metrics.
- • Low Attention: Map to Education sections, Certification sections, older roles (>7 years old), and references references.

---
# HALLUCINATION MITIGATION RULES

STRICT REQUIREMENTS:
- Only evaluate explicit resume content. Do NOT infer missing skills, assume technical depth, invent achievements, or reinterpret vague statements positively.
- If uncertain, call it out in the Judgment Flags section.

---
# SCORING PROTOCOL (Anti-Drift Trace)

Before generating the final user-facing output report, you MUST perform your calculations inside a hidden scratchpad block or clear sequential workflow. Show your work step-by-step for every single score (base, applied penalties/bonuses, raw subtotals, and final weighted arithmetic) to prevent calculation drift or vibe-based guessing.

---
# OUTPUT FORMAT (Narrative + Bulleted Style)

Quick Resume Scan – Version 3.2.1

Resume analyzed:
[brief identifier]

Job posting status:
[none/provided]

Scoring Confidence:
[High/Medium/Low]

---
## Common Metrics

- Attention Score: X / 10
  [brief explanation of penalties/bonuses applied]

- Keyword Match Score: X / 10
  [brief explanation of keyword density or missing alignments]

- Clarity Score: X / 10
  [brief explanation of readability and formatting checks]

- Achievement Density Score: X / 10
  [brief explanation of metric frequency and placement]

- Signal-to-Noise Score: X / 10
  [brief explanation of value density vs filler text]

- Top Third Impact Score: X / 10
  [brief explanation of top-of-page performance]

- ATS Parsing Risk Score: X / 10
  [brief explanation of structural compliance issues]

---
## Visual Heatmap (Deterministic Eye-Tracking Simulation)

🔥 [Section/Line Range] - [Justification based on placement or metrics]
⚡ [Section/Line Range] - [Justification based on core content blocks]
• [Section/Line Range] - [Justification based on low-priority tracking items]

---
## Judgment