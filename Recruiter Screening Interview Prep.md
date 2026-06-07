# TITLE: Recruiter Screening Interview Prep Report Engine
# VERSION: 2.2.4
# AUTHOR: Scott Malin, CISSP
# PURPOSE:
Generate a lightweight, highly tactical interview preparation report specifically optimized for 15-to-20-minute recruiter screening calls. The focus is on clearing fatigue, hitting mandatory keywords, checking logistical boxes, and delivering a natural, confident first impression.

============================================================
INPUTS
============================================================
1. JOB POSTING:
- Full job description, requirements, and responsibilities

2. APPLICANT PROFILE:
- Resume-style experience summary, skills, achievements, and constraints

3. CURRENT DATE:
- Use the system's current date or user-provided context.

============================================================
CHANGELOG
============================================================
- v1.0.0: Initial release (Deep-dive, heavy analysis report structure).
- v1.1.0: Added explicit data-anchoring, token fatigue reduction constraints, and date variables.
- v2.0.0: Major rewrite. Stripped out hiring manager technical forecasting; optimized format exclusively for short recruiter phone screens.
- v2.1.0: Restored a streamlined, evidence-based "Grounded Confidence Framing" section to address job hunt fatigue.
- v2.2.1: Updated author metadata, added a structured changelog, and integrated specific guardrails for the "Why Are You Looking" script and "Say Less" warning rules.
- v2.2.2: Fortified Section 2 with strict psychological armor, the "Fatigue Counter-Weight," and anti-cheerleading guardrails to protect against positive energy depletion.
- v2.2.3: Corrected block-nesting formatting drift shown in image_d5a225.png. Isolated the filename block into its own unique block and re-indexed the report body sections to begin at 1.
- v2.2.4: Cleaned syntax constraints by removing all nested markdown code block backticks from the layout instructions to guarantee flawless rendering across different LLM runners.

============================================================
OUTPUT FORMAT (STRICT LAYOUT RULES)
============================================================

### BLOCK 1: FILENAME ONLY (FIRST CODEBLOCK)
Your very first output must be a single markdown codeblock containing ONLY the generated filename. Do not include headers, descriptions, or text outside or inside this specific block. 

Format exactly as a standalone string:
ScreeningPrep-CompanyName-Position-YYYYMMDD.md

- CompanyName: extracted from posting
- Position: normalized job title
- YYYYMMDD: current date

---

### BLOCK 2: THE REPORT BODY (SECOND CODEBLOCK)
Immediately following Block 1, generate the full report contained entirely inside a separate markdown codeblock using the exact numbering layout below. Do not nest backticks inside the block:

## 1. GROUNDED CONFIDENCE FRAMING (MENTAL RESET)
Purpose: Directly combat job search fatigue and reset the applicant's psychological posture before the call using objective data.

Rules:
- Must be 100% evidence-based (derived strictly from clear overlap between job demands and applicant history).
- CRITICAL: Absolutely no generic motivational hype, empty cheerleading, clichés, or patronizing AI fluff. 
- Tone: Calm, direct, stabilizing, and quietly confident.

Include:
- **The Reality Check:** A blunt, 1–2 sentence statement explaining why this specific conversation is a completely reasonable, winnable, and logical next step for your career.
- **2–3 Factual Alignment Anchors:** Direct, undeniable matches where your past execution solves their immediate requirements. 
- **The Fatigue Counter-Weight:** Address the most daunting or stressful requirement in the posting by contextualizing it against your actual capabilities, showing why it is manageable and nothing to fear.

## 2. THE RECRUITER’S CHECKLIST (MANDATORY KEYWORDS)
Purpose: Identify the exact terms and core requirements the recruiter is checking off on their screen.

Include:
- **Must-Haves:** 3–5 non-negotiable keywords, tools, or certifications explicitly demanded in the posting.
- **Nice-to-Haves:** 2–3 secondary skills that will make the applicant stand out if mentioned casually.

## 3. THE 60-SECOND ELEVATOR PITCH
Provide a single, conversational response to "Tell me about yourself."

Rules:
- Must be tightly grounded in the applicant's real experience.
- VOCABULARY FIREWALL: No corporate buzzwords, marketing fluff, or AI boilerplate (e.g., "dynamic leader," "proven track record"). 
- Style: Write this exactly how a normal human speaks in a casual, direct, professional conversation. Short sentences.

## 4. SCREENING HURDLES & RISK AREAS
Identify the friction points the recruiter is highly likely to challenge or probe.

Include:
- **The "Why Are You Looking" Pivot:** A dead-simple, positive 2-sentence explanation for entering the job market that hides any search fatigue.
- **Potential Resume Red Flags:** Gaps, short tenures, missing specific tools, or transition reasons.
- **The Pivot Response:** A brief conversational script to address each risk cleanly.
- **The "Say Less" Warning:** 1–2 specific areas or missing skills where the applicant is at risk of over-explaining, with an explicit reminder to keep the answer under 15 seconds.

## 5. LOGISTICS & POLITE CLOSE
- Clear talking points for standard screening logistics (e.g., target salary alignment, work model/location, availability).
- 1–2 smart, high-level questions for the applicant to ask the recruiter about the next steps in the process.

============================================================
GLOBAL BEHAVIOR RULES
============================================================
- Cut all deep-dive business strategy, 12-month success forecasting, and complex technical narrative anchors. 
- Prioritize the "recruiter lens"—vetting for basic fit, constraints, communication skills, and critical keywords.
- All insights must be traceable to the job posting and applicant profile. Do not invent details.
- Keep the language conversational, brief, and highly scannable.