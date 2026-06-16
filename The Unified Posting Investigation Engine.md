# Unified Posting Investigation Engine (Enterprise Modular OSINT Edition)

VERSION: 1.1.0 (Modular Integrity Release)
AUTHOR: Scott M.
LAST UPDATED: 2026-06-16

============================================================
CHANGELOG
============================================================
v1.1.0 (2026-06-16)
· Introduced explicit internal modular architecture to preserve original 5-prompt behavior boundaries
· Added Job Legitimacy Module, Hiring Intent Module, Culture Intelligence Module, Positioning Module, and Decision Arbitration Layer
· Added cross-module contradiction detection rules
· Introduced unified confidence normalization scale (0–10)
· Added explicit evidence segregation per module
· Enforced final arbitration step to resolve conflicting signals
· Improved traceability between inference types and source evidence

============================================================
PURPOSE
============================================================
Provide a single structured intelligence report that preserves the analytical separation of:
- Job legitimacy and OSINT validation
- Hiring intent and opportunity realism
- Interview and positioning strategy
- Company culture and values inference
- Final decision arbitration

This system ensures completeness of the original 5-prompt architecture while maintaining unified output delivery.

============================================================
CORE ARCHITECTURE RULE
============================================================
You MUST execute all modules independently first.
Then synthesize outputs in the Final Arbitration Layer.

Do NOT merge reasoning between modules until arbitration stage.

============================================================
TAGGING SYSTEM (GLOBAL)
============================================================
[VERBATIM] = Direct quote from job posting
[PARAPHRASED] = Restated content
[INFERRED] = Evidence-based conclusion (must include justification)
[SUBTEXT] = Organizational implication (must include justification)
[RED FLAG] = Risk signal tied to evidence
[KITCHEN-SINK] = Overloaded/conflicting requirements
[TECH-CONFIRMED] = Explicit technologies listed

============================================================
MODULE 1: JOB LEGITIMACY & OSINT VALIDATION
============================================================
Purpose:
Detect whether the job posting is real, inflated, recycled, or misleading.

Analyze:
- Posting freshness signals
- Role specificity vs template language
- Repost indicators or evergreen hiring patterns
- Internal vs external candidate bias signals
- Salary transparency signals

Output:
- Legitimacy Score (0–10)
- Ghost Job Risk (Low / Medium / High)
- Evidence-backed red flags
- Key uncertainty factors

============================================================
MODULE 2: HIRING INTENT ANALYSIS
============================================================
Purpose:
Determine why this role exists.

Classify:
- Backfill
- Growth hire
- Pipeline / evergreen posting
- Compliance / resume collection role
- Internal promotion placeholder

Analyze:
- Language specificity
- Urgency signals
- Scope clarity
- Market alignment

Output:
- Hiring Intent Classification
- Confidence Score (0–10)
- Supporting evidence

============================================================
MODULE 3: CULTURE & REALITY INTELLIGENCE
============================================================
Purpose:
Infer organizational behavior patterns and working environment.

Analyze:
- Leadership messaging vs operational reality
- Likely performance expectations
- Structural pressure signals
- Burnout indicators
- Decision-making speed signals

Output:
- Culture Profile (Stable / High Pressure / Transitional / Unstable)
- Burnout Risk (Low / Medium / High)
- Key inferred operational traits

============================================================
MODULE 4: POSITIONING & INTERVIEW STRATEGY
============================================================
Purpose:
Translate job into candidate advantage strategy.

Analyze:
- Core pain points (“So What” factor)
- Required competencies vs implied needs
- Resume alignment hooks
- Messaging angles for interviews

Output:
- Positioning Strategy
- Key Resume Signals to emphasize
- 3 core interview narratives
- What NOT to emphasize

============================================================
MODULE 5: DECISION ARBITRATION LAYER
============================================================
Purpose:
Resolve contradictions across all modules.

Inputs:
- Legitimacy Score
- Hiring Intent
- Culture Risk
- Positioning Fit

Rules:
- If Legitimacy ≤ 4 → recommend Skip unless strong external justification
- If Culture Burnout = High AND Positioning Fit = Weak → Skip
- If Hiring Intent = Evergreen AND Legitimacy < 6 → Treat as low priority
- Otherwise evaluate composite opportunity score

Output:
- Final Decision: Apply / Light Apply / Skip
- Composite Opportunity Score (0–10)
- Primary Reasoning Summary
- Key Risk Tradeoffs

============================================================
CONTRADICTION HANDLING RULE
============================================================
If modules disagree:
- Do NOT overwrite results
- Preserve both signals
- Explicitly list contradiction in Arbitration Layer
- Resolution must be justified, not assumed

============================================================
CONFIDENCE NORMALIZATION
============================================================
All module confidence scores MUST map to:
- 0–3 = Low
- 4–6 = Medium
- 7–8 = High
- 9–10 = Very High (rare, evidence-rich)

============================================================
OUTPUT FORMAT (STRICT)
============================================================
Return a single markdown codeblock containing:

### UNIFIED POSTING INVESTIGATION REPORT

Include sections in this order:

1. Job Legitimacy & OSINT Validation (Module 1)
2. Hiring Intent Analysis (Module 2)
3. Culture & Reality Intelligence (Module 3)
4. Positioning & Interview Strategy (Module 4)
5. Decision Arbitration Layer (Module 5)

No text outside the codeblock.

============================================================
INPUT
============================================================
[INSERT JOB POSTING OR URL HERE]