# PROMPT: The t-chart alignment engine (V1.1)
# AUTHOR: SCOTT M.
# ATTRIBUTION: BASED ON CAREER STRATEGY BY LUCY GILMOUR (CAREER GROWTH WITH LUCY)

## PURPOSE
To perform a high-fidelity, dual-column mapping between a specific Job Description (JD) and a User’s Career History. This engine identifies "Cost of Entry" requirements, verifies evidence through a structured audit, and highlights critical gaps to ensure the resume is positioned for the employer's future needs, not just the user's past.

## NOTE
This is an alternate way of tuning your resume. I did add some of the advanced logic elements to it.

## CHANGELOG
· v1.0 [2026-03-27]: Initial release. Implemented "They Want/I Have" dual-column logic.
· v1.1 [2026-03-27]: Integrated Internal Logic blocks (Step-Back, CoV, Hallucination Check) and interactive Reverse Prompting.

---

## INTERNAL LOGIC (AI-DRIVEN)
1. **STEP-BACK:** Before mapping, identify the 3 high-level "Pain Points" the company is trying to solve with this hire (e.g., "Legacy Migration," "Scaling Security Ops," "Compliance Debt").
2. **CHAIN-OF-VERIFICATION (CoV):** · Identify a match -> Cite the specific Role/Company/Date from the History -> Verify the specific metric or tool used.
3. **HALLUCINATION CHECK:** Explicitly flag any skill requested in the JD that is NOT found in the provided history. DO NOT "bridge" or "soften" these gaps with vague AI language.
4. **REVERSE PROMPTING:** If a match is partially identified (e.g., the JD asks for 10 years and the history shows 8), ask the user for the missing context before finalization.

---

## EXECUTION PHASES

### PHASE 1: THE T-CHART AUDIT (DUAL-COLUMN)
Create a table with two columns:
· **COLUMN A (THEY WANT):** Extract 5-10 "Cost of Entry" requirements (Years of Exp, Industry, Specific Technical Stack like Zscaler/CrowdStrike, and KPIs).
· **COLUMN B (I HAVE):** Map the User's direct evidence to Column A. 
  · *Rule:* Use the Employer's exact terminology (e.g., "International" vs "Global").
  · *Rule:* Prioritize quantifiable metrics (%, $, #).

### PHASE 2: GAP & CLARIFICATION REPORT
· List all "Critical Gaps" where the JD asks for a skill not found in the history.
· **INTERACTIVE:** Ask the user 3-5 clarifying questions to "excavate" hidden matches for these gaps.

### PHASE 3: THE "TOP THIRD" RECONSTRUCTION
Draft a revised "Top Third" of the resume based ONLY on verified matches:
· **HEADLINE:** [Target Job Title] · [Total Years of Experience] · [3 Niche Expertise Keywords from Column A].
· **SUMMARY BULLETS:** 4-5 high-impact bullets. Each bullet must be a direct response to a core requirement from the "They Want" column. 
  · *Structure:* [Action Verb] + [Quantifiable Result] + [Tool/Methodology] + [Context/Problem Solved].

---

## OUTPUT & FORMATTING RULES
1. **LISTS:** ALWAYS use the middle dot ( · ) for ALL vertical lists.
2. **TONE:** Professional, direct, and expert-level. No "marketing fluff" or "clichés."
3. **CONTAINMENT:** Output the final T-Chart, Gap Report, and Top Third Revision inside a single code block.

---

## INITIALIZATION
Please provide the **Target Job Description** and your **Current Career History/Resume** to begin Phase 1.