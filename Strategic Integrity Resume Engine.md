## Resume Customization Prompt – STRATEGIC INTEGRITY v3.24 (GENERIC)
- **Author:** Scott M.
- **Version:** v3.25 (Generic Master)
- **Last Updated:** 2026-03-03
- **Changelog:** - v3.25: Initial generic release.
    - v3.24: Integrated God Mode and Oceangate logic.
    - v3.23: Added GitHub Source Retrieval logic.
    - v3.22: Refined Cover Letter signature and ATS-friendly headers.

---

## QUICK START GUIDE (HOW TO USE THIS PROMPT)
1. **Fill Variables:** Replace the brackets in the "USER VARIABLES" section below.
2. **Attach File:** Upload your Skills Summary markdown file.
3. **Paste Job Posting:** Paste the target Job Description into the chat along with this prompt.
4. **Execute:** The AI will perform a Strategic Audit first, then generate the tailored resume and cover letter.

---

## USER VARIABLES (REQUIRED)
- **NAME & CREDENTIALS:** [Example: Scott Malin, CISSP]
- **TARGET ROLE:** [Example: Network Security Engineer]
- **SOURCE FILE:** [Example: Scott_Malin_Skills_Summary.markdown]
- **SOURCE URL:** [Example: https://github.com/your-repo/your-file.markdown]

### IMPORTANT: SOURCE FILE RETRIEVAL
The master data for this task is in [SOURCE FILE]. If this file is not attached to the current conversation, you must attempt to retrieve its contents from [SOURCE URL] before proceeding.

### PHASE 1: STRATEGIC AUDIT (God Mode + Oceangate Integration)
Before writing anything, perform a brief "Strategic Audit" in plain text:
1. **The Real Problem:** What business or technical problem does this role ACTUALLY solve for the company?
2. **The Unspoken Need:** What are they NOT saying in the JD but desperately need to stay competitive or secure?
3. **The 99% Trap:** What will 99% of applicants emphasize? Contrast the candidate's specific seniority and "battle-tested" history against the "quick-fix" mentality of typical applicants.
4. **The Sinker:** Identify one thing in the candidate's current profile that sounds like "AI garbage," fluff, or is too vague for this specific industry.
5. **The Lead:** What is the ONE specific "receipt" or achievement from the source file that should be the primary hook?

### PHASE 2: MANDATORY OUTPUT ORDER & SECTION REPORTING
Process EVERY section in this exact order. If a section requires no changes, you MUST state "No Changes Required" and display the text as it exists in the source. 

**ORDER:** 1. **Header:** Name as "[NAME & CREDENTIALS]". Use ( • ) to separate phone • email • LinkedIn.
2. **Professional Summary:** (Humanized "I" voice, include portfolio/GitHub links).
3. **AREAS OF EXPERTISE:** (Single paragraph block, items separated by bold middle dot · ).
4. **Key Accomplishments:** (Exactly 3 bullets, max 3 lines each, no personal pronouns).
5. **Professional Experience:** (Job/Company/Dates as text; Bullets in a single code block).
6. **Early Career / Additional History.**
7. **Education.**
8. **TECHNICAL COMPETENCIES:** (Categorized vertical list of tools/platforms - NEVER OMIT).
9. **Certifications / Licenses.**

### PHASE 3: CORE RULES (Integrity & Human-Centric)
- **Problem-Solver Framing:** Frame every bullet as a solution to the needs identified in Phase 1.
- **Before & Revised:** For EVERY section revised, show **Before:** (plain text) then ```Revised``` (code block).
- **No Hallucinations:** Use ONLY facts found in the provided source file.
- **First-Person Implied:** Experience bullets must start with Action Verbs. No "I", "me", or "my" in Experience.
- **Formatting:** Use standard headings. Middle dot ( · ) bullets. No blank lines between list items.

### COVER LETTER & WRAP-UP
- **Cover Letter:** Professional header using [NAME & CREDENTIALS], current date, and company HQ address.
- **Tone:** Focus on solving their problem. Output in one code block.
- **Signature:** Sign off using [Full Name] only (do not repeat credentials here).
- **Recruiter Snapshot:** Fit (%) | Top 3 Matches | Honest Gaps.
- **Revision Changelog:** List every section processed and summarize adjustments made.