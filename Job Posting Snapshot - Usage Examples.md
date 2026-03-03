# Job Posting Snapshot & Preservation Engine – Operations Manual

**Version:** 2.0  
**Author:** Scott M  
**Last Updated:** 2026-03  

---

## Purpose

This manual explains how to use the Job Posting Snapshot & Preservation Engine for:

- Accurate, evidence-based extraction of job postings.
- Creating a reusable archive of postings.
- Strategic analysis, trend identification, and resume optimization.
- Long-term version-controlled job intelligence.

All steps adhere strictly to the tagging and hallucination control rules defined in the main prompt.

---

## 1. Quick Start Workflow

### Step 1: Prepare Inputs
Provide these values before running the engine:

- **Source Type:** URL, Full pasted text, PDF, Screenshot OCR, Partial reconstructed content.  
- **Source Location:** Direct URL, Platform name, or “NOT STATED”.  
- **Capture Date:** If missing, use today’s date.  
- **Posting Date:** If visible in source.  
- **Expiration Date / Close Date:** If visible.  

> Tip: Full source text ensures more [VERBATIM] tagging and higher confidence.

---

### Step 2: Run Engine
1. Open the main engine prompt in your AI platform (ChatGPT, Grok, Claude, etc.).
2. Paste the prepared inputs at the top.
3. Paste the full source text immediately after.
4. Execute the prompt.
5. Receive **two code blocks**:  
   - **Codeblock 1:** Suggested Filename  
   - **Codeblock 2:** Job Posting Snapshot Markdown

---

### Step 3: Save Snapshot
1. Copy the snapshot code block into a `.md` file using the suggested filename.
2. Save in a structured folder system (e.g., `Job-Snapshots-2026/`).
3. Do not edit tags or remove `[NOT STATED]` entries — preserve archival purity.

---

## 2. Usage Examples

### Example 1: Live URL from LinkedIn or Company Site
**Input:**
```

Source Type: URL
Source Location: [https://www.linkedin.com/jobs/view/senior-security-engineer/123456789](https://www.linkedin.com/jobs/view/senior-security-engineer/123456789)
Capture Date: 2025-10-15
Posting Date: 2025-10-01
Expiration Date: NOT STATED

```
- Paste full job description text if AI cannot fetch directly.  
**Output:** Filename and tagged markdown snapshot.  
**Best for:** Fresh postings you find while browsing.

---

### Example 2: PDF from Internal Portal
**Input:**
```

Source Type: PDF
Source Location: Internal career portal - printed from browser
Capture Date: 2025-11-02
Posting Date: 2025-10-20
Expiration Date: 2025-12-31

```
- Upload PDF or paste extracted text.  
**Output:** Tagged snapshot, ready for archival.  
**Best for:** Sites blocking copy-paste or dynamic content.

---

### Example 3: Partial / Reconstructed Content
**Input:**
```

Source Type: Partial reconstructed content
Source Location: Memory + screenshot
Capture Date: 2025-09-10
Posting Date: NOT STATED
Expiration Date: NOT STATED

```
- Include whatever you remember or OCR extracted.  
**Output:** Most fields marked `[NOT STATED]` or `[NOT LISTED]`.  
**Best for:** Roles where original posting is no longer available.

---

### Example 4: Post-Snapshot Interview Prep
1. Copy snapshot markdown.
2. Use Section 6 “Interview Preparation” prompt.
3. Ask for behavioral questions, probing areas, and suggested answers strictly based on snapshot content.  
**Output:** Grounded interview prep aligned to the posting.

---

### Example 5: Hiring Motivation Analysis
1. Paste snapshot into Section 6 “Hiring Intent Analysis” prompt.  
2. AI tags drivers based on Business Context Signals, Responsibilities, and Keywords:
   - `[INFERRED] Growth` – multiple openings, new teams.
   - `[NOT STATED] Cost Reduction` – no efficiency/optimization language.  
**Output:** Strategic insight into role intent.

---

## 3. Archival Strategy

- Save snapshots in year-specific folders (e.g., `Job-Snapshots-2026`).  
- Keep snapshots **immutable**; never overwrite older versions.  
- Use a separate “Working Copy” if you annotate.  
- Track multi-level roles in a single snapshot with clear notes.

---

## 4. Metadata Indexing (Optional but Recommended)

Maintain a master index (CSV or Markdown table):

| Company | Role | Capture Date | Status | Applied? | Interviewed? |
|---------|------|--------------|--------|----------|---------------|

**Benefits:**
- Identify recurring requirements.
- Spot trending tools/frameworks.
- Track keywords converting to interviews.

---

## 5. Trend Analysis / Pattern Recognition

- Extract “Explicit Keywords” across multiple snapshots.
- Compare frequency of tools, certifications, and responsibilities.
- Adjust resume language and application focus based on high-frequency [VERBATIM] items.

---

## 6. Quality Assurance Checklist

Before saving snapshots:

- [ ] All list items include proper tags.  
- [ ] Compensation & Benefits fields tagged.  
- [ ] Completeness Assessment reflects source fidelity.  
- [ ] ⚠ SOURCE INCOMPLETE included only if applicable.  
- [ ] Filename matches capture date.  
- [ ] Multi-level/multi-role structure noted when applicable.

---

## 7. “Do Not” Rules

- Do not edit or paraphrase `[VERBATIM]` bullets.  
- Do not remove `[NOT STATED]` or `[NOT LISTED]` entries.  
- Do not mix external research into snapshot markdown.  
- Do not modify tags after generation.

---

## 8. Resume Optimization Workflow

1. Generate 5–10 snapshots for similar roles.  
2. Extract common Required Qualifications and Responsibilities.  
3. Identify gaps in your resume.  
4. Update resume using exact phrasing from [VERBATIM] bullets.  
5. Test application outcomes and iterate.

---

## 9. Tag Confidence Guidance

- `[VERBATIM]` = Strongest signal, guaranteed.  
- `[PARAPHRASED]` = High confidence; grounded in posting.  
- `[INFERRED]` = Weak signal; only when explicitly allowed.  
- `[NOT STATED]` = Likely not a priority in this posting.  
- `[NOT LISTED]` = Field absent; probably irrelevant.

---

## 10. Practical Tips

- Always provide Capture Date for consistent filenames.  
- Use full source text whenever possible.  
- If PDF upload fails, extract text manually and select Source Type: Full pasted text.  
- Review tags before reusing for interview prep or resume optimization.  
- Add your own examples as you expand your archive.

---

**End of Operations Manual**
```

This version:

* Keeps all original examples.
* Adds archival strategy, metadata indexing, trend analysis, QA, “Do Not” rules, and resume optimization.
* Gives tag confidence guidance.
* Reads like a full **Operations Manual**, not just a “how to paste text” guide.
