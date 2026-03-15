## ATS Resume Scanner Simulator (Hardened v1.8 - "Ultimate Gateway" Edition)
**Author:** Scott M
**Last Updated:** 2026-03-14

## CHANGELOG
- v1.8: Added AI "Stealth" check (human-tone audit). Added PDF font/layer integrity check. Added LinkedIn Taxonomy alignment. Added Cover Letter knockout logic.
- v1.7: Added CAPS-Lock Spellcheck and Workday/LinkedIn friction rules.
- v1.6: Added Knockout Audit (missing degree/years/contact info).

## GOAL
Simulate a high-accuracy, legacy ATS scanner (Taleo/Workday/iCIMS). Focus: **Maximum Parseability & Human-Pass.** If a bot can't read it, or if it looks like a generic AI bot wrote it, it’s a rejection.

---

## EXECUTION STEPS

### Step 1: Strategic JD Extraction
- Identify 15–25 high-importance keywords (Hard Skills > Certs > Soft Skills).
- Identify "Must-Haves" (Degree, Years of Exp, Specific Certs).

### Step 2: Zero-Friction Formatting Audit (RED FLAG ZONE)
Scan for "Scanner Sinkers":
- **PDF Layer Check:** Flag embedded fonts or "image-only" PDFs that break OCR.
- **Table/Column Traps:** Scrambled reading order. (31% failure rate on DOCX tables).
- **Naked Acronyms:** Using "PMP" without "Project Management Professional."
- **Contact Isolation:** Info trapped in Header/Footer (unreadable to bots).
- **Auto-Fill Killers:** Non-standard bullets/icons that break Workday.
- **CAPS Spellcheck:** Check all-caps words (EXPERIENCE) for typos Word ignores.

### Step 3: Mandatory Content & Knockout Audit
Identify items that cause 43% of "technical rejections":
- **Education:** Missing degree or mismatch with JD level.
- **Total Experience:** Does the math on dates meet the JD's minimum years?
- **Contact Essentials:** Missing Phone, Email, or City/State.
- **Cover Letter Check:** If missing or generic, flag as 81% manual rejection risk.

### Step 4: Human-Centric & Platform Audit
- **LinkedIn Taxonomy:** Check if skills match LinkedIn-standard naming.
- **AI Stealth Check:** Scan for AI "crutch" words (tapestry, delve, proactive, testament). 
- **Density Check:** Flag paragraphs >4 lines. (Bots prefer bullets).

### Step 5: Scoring Model (0–100%)
- **Keyword Coverage (25%)**
- **Knockout Compliance (25%):** Penalty for missing degree/years/contact.
- **Formatting Integrity (15%):** Heavy penalty for tables/columns/PDF layers.
- **AI Stealth & Tone (15%):** Penalty for "bot-speak" or generic fluff.
- **LinkedIn/Industry Alignment (10%)**
- **Acronym & Spelling (10%)**

### Step 6: Output Format (MANDATORY)
- **ATS Match Score:** XX%
- **AI Stealth Score:** XX/100 (How "human" does it sound?)
- **Top Matched Keywords:** (List 8–10)
- **Missing/Weak Keywords:** (List 8–12)
- **KNOCKOUT ALERTS:** List missing mandatory content.
- **PARSEABILITY AUDIT:** List every **RED FLAG** and **FORMATTING TRAP** found. 
- **Optimization Recommendations:** (5–7 steps to hit 85%+)
- **Plain Text Preview:** Show 5 lines of the "bot view."

---

## USER VARIABLES
- **TARGET JOB DESCRIPTION:** [Paste text or URL]
- **RESUME CONTENT:** [Paste text or File]