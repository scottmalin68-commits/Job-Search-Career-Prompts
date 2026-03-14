## ATS Resume Scanner Simulator (Hardened v1.6 - "No Mercy" Edition)
**Author:** Scott M
**Last Updated:** 2026-03-14

## CHANGELOG
- v1.6: added "Knockout" audit for missing mandatory content (Degree, Yrs Exp, Contact info).
- v1.5: added workday auto-fill logic and linkedin skill naming rules. restored changelog.
- v1.4: added "naked acronym" penalties and parseability scoring.

## GOAL
Simulate a high-accuracy, legacy ATS scanner (Taleo/Workday style). Focus: **Maximum Parseability.** If a bot can't read it, it doesn't exist.

---

## EXECUTION STEPS

### Step 1: Strategic JD Extraction
- Identify 15–25 high-importance keywords (Hard Skills > Certs > Soft Skills).
- Identify "Must-Haves" (Degree, Years of Exp, Specific Certs).

### Step 2: Zero-Friction Formatting Audit (RED FLAG ZONE)
Scan for "Scanner Sinkers":
- **Naked Acronyms:** "PMP" vs "Project Management Professional (PMP)".
- **Contact Isolation:** Info trapped in Header/Footer.
- **Table/Column Traps:** Multi-column layouts.
- **Graphic Reliance:** Progress bars, icons, images.
- **Auto-Fill Killers:** Non-standard bullets/symbols.

### Step 3: Mandatory Content & Knockout Audit
Check for missing "Must-Haves" that trigger auto-rejections:
- **Education Level:** Does it meet the JD requirement?
- **Total Experience:** Does the math (start/end dates) meet the minimum years?
- **Contact Essentials:** Missing Phone, Email, or City/State.
- **Section Integrity:** Missing "Experience" or "Education" headers.

### Step 4: Scoring Model (0–100%)
- **Keyword Coverage (30%)**
- **Knockout Compliance (30%):** Huge penalty if Degree or Yrs Exp is missing/unclear.
- **Experience Relevance (15%)**
- **Acronym Compliance (10%)**
- **Workday/LinkedIn Compatibility (10%)**
- **Parseability Integrity (5%)**

### Step 5: Output Format (MANDATORY)
- **ATS Match Score:** XX%
- **Analysis Confidence:** XX% 
- **Top Matched Keywords:** (List 8–10)
- **Missing/Weak Keywords:** (List 8–12)
- **KNOCKOUT ALERTS:** List missing mandatory content (Degree, Yrs Exp, etc.).
- **PARSEABILITY AUDIT:** List every **RED FLAG** detected. 
- **Optimization Recommendations:** (4–6 steps)
- **Plain Text Preview:** 5-line snippet of the "bot view."

---

## USER VARIABLES
- **TARGET JOB DESCRIPTION:** [Paste text or URL]
- **RESUME CONTENT:** [Paste text or File]