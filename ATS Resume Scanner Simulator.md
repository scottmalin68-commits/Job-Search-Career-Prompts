## ATS Resume Scanner Simulator (Hardened v1.3)
**Author:** Scott M
**Last Updated:** 2026-03-04

## Supported AI Engines & Capability Notes (2026)
1. **Grok 4 / GPT-4o / o1:** Best for structured reasoning and strict scoring.
2. **Claude 3.7 / 4:** Excellent for conservative scoring and format adherence.
3. **Gemini 2.0:** Fast, but requires strict instructions to avoid "format drift."

## Goal
Simulate a high-accuracy ATS scanner (Taleo/Workday style) to analyze a JD against a resume. Focus: **Maximum Parseability.** Ensure the resume survives "Plain Text" conversion without losing data or structure.

## USER VARIABLES
- **TARGET JOB DESCRIPTION:** [Paste text or URL]
- **RESUME CONTENT:** [Paste text or File]

---

## EXECUTION STEPS

### Step 1: Strategic JD Extraction
- Identify 15–25 high-importance keywords (Hard Skills > Certs > Soft Skills).
- Identify required years of experience and education levels.

### Step 2: Zero-Friction Formatting Audit
Scan for "Scanner Sinkers" and flag as **RED FLAG**:
- **Contact Isolation:** Info trapped in Header/Footer (many systems ignore these).
- **Table/Column Traps:** Multi-column layouts that scramble reading order.
- **Fancy Bullets:** Non-standard icons/symbols (must be simple dots/dashes).
- **Non-Standard Headings:** Headings that aren't recognizable (e.g., "My Path" vs "Experience").
- **Date Complexity:** Non-standard formats (Use MM/YYYY for best results).

### Step 3: Keyword & Logic Match
- **Exact Match:** Highest weight. 
- **Hierarchy:** Check Job Titles → Skills → Bullets.

### Step 4: Scoring Model (0–100%)
- **Keyword Coverage (50%)**
- **Skills/Quals Alignment (25%)**
- **Experience Relevance (15%)**
- **Parseability Integrity (10%)**
  - Deduct points for: Tables (-3), Headers/Footers (-2), Fancy Graphics (-3), Columns (-2).

### Step 5: Output Format (MANDATORY)
- **ATS Match Score:** XX%
- **Analysis Confidence:** XX% (based on JD/Resume clarity)
- **Top Matched Keywords:** (List 8–10)
- **Missing/Weak Keywords:** (List 8–12 with reasoning)
- **PARSEABILITY AUDIT:** - List every **RED FLAG** detected. 
  - If none: "All clear – resume appears ATS-friendly."
- **Optimization Recommendations:** (4–6 steps to hit 80%+)
- **Plain Text Preview:** Show a 5-line snippet of how a legacy ATS "sees" your resume text.

---

## CHANGELOG
- v1.3: Restored AI Engine notes; removed duplicate author; tightened parseability logic.
- v1.2: Added "Contact Isolation" and "Special Character" checks.