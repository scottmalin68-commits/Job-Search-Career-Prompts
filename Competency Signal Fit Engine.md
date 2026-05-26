# TITLE: Competency Signal Fit Engine (Resume ↔ Job Matching System)
# VERSION: 1.0.0
# AUTHOR: Scott Malin, CISSP
# PURPOSE:
Transforms resumes/career profiles and job postings into a shared competency space,
then computes explainable, bidirectional fit analysis including:
- skill extraction
- competency scoring
- confidence weighting
- gap detection
- job-to-candidate alignment
- candidate-to-job alignment

The system produces a structured markdown report that is human-readable, archivable,
and suitable for iterative career development tracking.

---

# CHANGELOG

## v1.0.0 (2026-05-26)
- Changed Author to Scott Malin, CISSP.
- Added dynamic taxonomy override rule to handle non-security roles.
- Added baseline calibration rule for 0–20 scoring consistency.

## v0.1.1 (2026-05-26)
- Removed all nested triple-backtick code fences from internal sections to ensure:
  - safe embedding in other prompt systems
  - compatibility with markdown parsers that break on nested fences
  - improved portability for downstream automation
- Retained structural integrity of report specification
- No changes to scoring logic or taxonomy

## v0.1.0 (2026-05-26)
- Initial unified design combining:
  - resume/profile scoring
  - job posting competency extraction
  - bidirectional comparison model
- Introduced shared competency taxonomy concept
- Added:
  - rating legend system (map-style symbology concept)
  - confidence scoring requirement
  - evidence-based scoring (no keyword-only scoring)
  - gap delta matrix (user vs job requirement comparison)
  - fit classification tiers
- Defined standardized output structure for markdown reports
- Introduced filename convention standardization
- Introduced explainability requirement for all scores

---

# INPUT TYPES

The engine accepts any of the following:

- Resume (text or markdown)
- Career Profile document
- Job Posting (URL or captured file)
- Hybrid comparison mode (user + job)

---

# CORE DESIGN PRINCIPLES

1. Evidence > Keywords
   - Scores must be derived from demonstrated experience, not mentions.

2. Explainability Required
   - Every score must include reasoning and evidence references.

3. Bidirectional Analysis
   - Evaluate:
     a) Candidate → Job fit
     b) Job → Candidate readiness

4. Shared Competency Space
   - Both resumes and job postings map into the same skill axes.

5. Confidence-Aware Scoring
   - Every rating includes confidence level (Low / Medium / High)

---

# COMPETENCY MODEL (TAXONOMY RULES)

## Base Taxonomy (Default)

### Technical
· Cloud Security
· Identity & Access Management
· Endpoint Security
· Detection & Response
· Automation & Scripting
· Architecture
· Vulnerability Management

### Delivery & Execution
· Agile Delivery
· Project Management
· Incident Response
· System Reliability

### Governance & Risk
· Compliance
· Risk Management
· Policy Development

### Leadership & Communication
· Stakeholder Management
· Executive Communication
· Team Leadership
· Cross-functional Collaboration

## Dynamic Taxonomy Override
If the provided input files represent a domain outside of core cybersecurity (e.g., Software Engineering, Product Management, Finance), the engine must dynamically adjust or replace the Technical and Delivery categories to map to the core skill axes of that specific domain. The Governance and Leadership sections should be retained and adapted as needed.

---

# RATING SYSTEM (MAP LEGEND STYLE)

## Competency Score Scale (0–20)

· 0–3   = Awareness (minimal exposure)
· 4–7   = Foundational (basic familiarity)
· 8–11  = Working Competency (practical usage)
· 12–15 = Advanced (ownership + execution)
· 16–18 = Expert (deep specialization)
· 19–20 = Authority (industry-level mastery)

### Scoring Calibration Rule
To maintain statistical consistency, default to the midpoint of a tier (e.g., 10 for Working Competency, 14 for Advanced) unless explicit supporting evidence or a lack of secondary skills justifies shifting the score to the upper or lower boundaries of that specific tier.

---

## Confidence Levels

· Low    = inferred / weak signals
· Medium = partial supporting evidence
· High   = strong explicit evidence

---

# OUTPUT STRUCTURE (MARKDOWN REPORT)

## 1. GENERATED FILE NAME (FIRST OUTPUT BLOCK)

SkillFit-[Type]-[Target]-[Entity]-[YYYYMMDD].md

---

## 2. EXECUTIVE SUMMARY

· Overall Fit Score (0–100)
· Fit Classification:
  · Strong Fit
  · Adjacent Fit
  · Stretch Fit
  · Mismatch
· Key Strengths
· Primary Gaps

---

## 3. COMPETENCY MATRIX (CANDIDATE)

| Skill | Score | Confidence |
|------|------|------------|
| Cloud Security | X | High/Med/Low |

---

## 4. JOB REQUIREMENT MATRIX

| Skill | Required Level | Importance Weight |

---

## 5. GAP DELTA ANALYSIS

| Skill | Candidate | Job Req | Delta |
|------|----------|--------|------|
| Cloud Security | 14 | 17 | -3 |

---

## 6. FIT INTERPRETATION

· Strong Matches
· Near Matches
· Weak Matches
· Missing Critical Skills

---

## 7. EVIDENCE BREAKDOWN

For each competency:

### Example Section

Cloud Security (Score: 13/20 | Confidence: Medium)

· Positive Evidence:
  · Azure security implementations
  · Zscaler deployment experience

· Missing Evidence:
  · Kubernetes security hardening
  · IaC security tooling

· Reasoning:
  Narrative explanation of scoring logic

---

## 8. RISK ANALYSIS (JOB VIEW)

· Hiring risks based on gaps
· Execution risks
· Delivery risks
· Knowledge gaps

---

## 9. DEVELOPMENT RECOMMENDATIONS

· Highest ROI skill improvements
· Suggested projects
· Skill adjacency paths

---

## 10. FINAL VERDICT

· Fit classification
· Summary recommendation
· Interview focus areas

---

# NAMING CONVENTION STANDARD

All outputs must include a filename before the report:

SkillFit-[Resume|Job|Match]-[PrimaryRole]-[Entity]-[YYYYMMDD].md

Examples:
· SkillFit-Resume-SecurityEngineer-ScottMalin-20260526.md
· SkillFit-Job-CloudSecurityArchitect-Microsoft-20260526.md
· SkillFit-Match-CloudSecurity-Travelers-R40186-20260526.md

---

# END SPEC