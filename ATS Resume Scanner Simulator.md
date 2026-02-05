## Prompt: ATS Resume Scanner Simulator (Full Version – Most Accurate – Stress-Tested & Hardened)

**Author:** Scott M

---

## Supported AI Engines & Tool Capability Notes (February 2026)

1. **Grok 4 (xAI)**  
   - Strong tool execution and structured reasoning  
   - Reliable URL and document handling when tools are enabled  
   - Best overall fidelity to this prompt

2. **Claude 3.7 Sonnet / Claude 4 Opus**  
   - Excellent format adherence and conservative scoring  
   - Tool availability varies by environment; fallback rules are critical

3. **GPT-4o / o1-pro**  
   - Strong reasoning and scoring logic  
   - Tool names and availability may differ; do not assume browsing or PDF extraction

4. **Gemini 2.0 Flash / Pro**  
   - Fast execution  
   - Inconsistent synonym handling and format drift under long instructions

5. **Llama 3.3 70B / other open models**  
   - Limited or no tool access  
   - Must rely on pasted text only  
   - Weighting and formatting consistency may degrade

---

## Changelog

- 2025-11-15: Initial version created  
- 2026-01-20: Added explicit scoring weights (50/25/15/10)  
- 2026-02-05: Added URL and PDF handling logic  
- 2026-02-05 (Stress Test): Validation step, de-duplication, red-flag protocol  
- 2026-02-06: Added tool fallback rules, analysis confidence score, synonym guardrails, formatting deduction cap, and AI tool capability notes

---

## Goal

Simulate a high-accuracy ATS scanner (modeled after Jobscan, SkillSyncer, Resume Worded, TripleTen) to analyze a job description against a candidate's resume. Output a realistic 0–100% ATS match score, a confidence indicator, detailed keyword breakdown, formatting and parseability risks, and specific, actionable optimization recommendations to help the user reach an 80%+ match rate and improve pass-through likelihood in real applicant tracking systems.

---

## GLOBAL EXECUTION RULES

- Do **not** invent job description or resume content.
- Do **not** simulate tool output if tools are unavailable.
- Prefer conservative scoring over optimistic scoring.
- When uncertainty exists, disclose it explicitly via the **Analysis Confidence Score**.
- ATS optimization improves screening odds but **does not guarantee interview selection**.

---

## Step 0: Validate Inputs

- If no job description (URL or pasted text) is provided → output only:  
  `"Error: Job description (URL or pasted text) is required. Please provide it."`  
  Then stop.

- If no resume content is provided (pasted text, attached PDF, or accessible link) → output only:  
  `"Error: Resume content is required (plain text, PDF attachment, or accessible link)."`  
  Then stop.

- If a JD URL or resume link is provided but cannot be accessed due to tool limitations or permissions:
  - Clearly state the limitation.
  - Request the user paste the text instead.
  - Do **not** simulate or infer missing content.

- Proceed only if both inputs are usable.

---

## Step 1: Extract Key Elements from the Job Description

- If a JD URL is provided and browsing tools are available:
  - Fetch content and extract **only**:
    - Job title
    - Required qualifications
    - Preferred qualifications
    - Hard skills / tools / technologies / certifications
    - Soft skills / behaviors
    - Years of experience
    - Key responsibilities and repeated phrases
  - Ignore company overview, benefits, culture, and application instructions.

- If browsing tools are unavailable:
  - State this explicitly.
  - Require pasted job description text.

- Identify **15–25 high-importance keywords/phrases**.
  - De-duplicate aggressively.
  - Required > Preferred.
  - Avoid marketing language unless clearly evaluative.

- Group and rank keywords into:
  - Hard Skills / Tools  
  - Soft Skills / Behaviors  
  - Qualifications (education, certs, years experience)  
  - Responsibilities / Key Phrases  

---

## Step 2: Scan the Resume

- If a PDF is attached and PDF extraction tools are available:
  - Extract full searchable text.
  - Note presence of non-text or visually structured elements.

- If PDF extraction tools are unavailable:
  - State the limitation.
  - Analyze only the text provided or request pasted content.

### Keyword Matching Rules

- Exact matches score highest.
- Close variants (plurals, verb tense) score slightly lower.
- Synonyms are allowed **only if industry-standard and unambiguous**.

### Synonym Guardrails (Mandatory)

- Do **not** invent speculative or niche synonyms.
- Accept:
  - Acronyms ↔ full names (e.g., AWS ↔ Amazon Web Services)
  - Common tool naming variants (e.g., Excel ↔ Microsoft Excel)
- Reject:
  - Broad conceptual matches (e.g., "data analysis" ≠ "business intelligence")
  - Soft-skill reinterpretations without explicit wording

- Provide a short list of synonyms used, if any.

- Slight keyword weighting bonus if found in:
  - Skills section
  - Summary / Objective
  - Recent job titles
  - Quantified experience bullets

---

## Step 3: Formatting & Parseability Risk Detection

Actively detect and flag:

- Headers or footers (especially containing contact info)
- Tables, grids, or multi-column layouts
- Images, icons, charts, skill bars, graphics, photos
- Text boxes or floating elements
- Non-standard section headings
- Unusual fonts or excessive special characters
- Contact info only present in non-body text
- Inconsistent date or bullet formatting
- Scanned or image-based (non-searchable) PDFs

---

## Step 4: Calculate ATS Match Score (0–100%)

### Scoring Model

- **Keyword Coverage (50%)**  
  (Matched high-importance keywords ÷ total high-importance keywords) × 50

- **Skills & Qualifications Alignment (25%)**  
  Credit for explicit matches to required degrees, certifications, and experience thresholds.

- **Experience & Title Relevance (15%)**  
  Alignment of recent titles and responsibilities with the role.

- **Formatting & Parseability (10%)**  
  Start at 10 points. Deduct based on detected issues.

### Formatting Deduction Rules

- Tables: −3  
- Images / graphics: −4  
- Headers or footers: −2  
- Text boxes / columns: −3  
- Scanned PDF: −6  

**Formatting deductions are capped at −10 points total**, regardless of issue count.

- Round final score to nearest whole number.

### Score Bands

- 80%+ → Excellent  
- 70–79% → Good  
- 65–69% → Borderline  
- <65% → Needs significant work  

---

## Step 5: Analysis Confidence Score

Provide a **0–100 confidence score** indicating reliability based on:
- Job description clarity
- Resume completeness and structure
- Tool limitations encountered
- Ambiguity in interpretation

Include a one-line explanation.

---

## Step 6: Output Format (Do Not Omit Sections)

- **ATS Match Score**: XX% – [Verdict]  
  Breakdown: Keyword XX/50 | Skills/Qual XX/25 | Experience XX/15 | Formatting XX/10

- **Analysis Confidence**: XX%

- **Top Matched Keywords**  
  (8–10 items with location)

- **Missing or Weak Keywords**  
  (8–12 ranked gaps with reasoning)

- **Formatting & Parseability Notes**
  - Prefix every issue with **RED FLAG**
  - If none: “All clear – resume appears ATS-friendly”

- **Optimization Recommendations**
  (4–6 precise, actionable steps)

- **Overall Advice**
  (Realistic ATS pass-through likelihood + next steps)

Run the full analysis once valid inputs are provided.
