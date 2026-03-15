# Job Posting Snapshot & Preservation Engine – Operations Manual

**Version:** 2.2  
**Author:** Scott M  
**Last Updated:** 2026-03  

---

## Purpose

This manual explains how to use the Job Posting Snapshot & Preservation Engine for:
- **Archival Integrity:** Creating a permanent, evidence-based record of job posts before they vanish.
- **Strategic Briefing:** Using the "Strategic Decoder" to identify hidden cultural red flags and subtext.
- **Interview Readiness:** Generating targeted prep questions based strictly on the source text.
- **Trend Intelligence:** Identifying recurring KPIs and requirements across multiple companies.

---

## 1. Handling "Fortress" Sites (Anti-Bot Workarounds)

Many job boards (LinkedIn, Indeed, Glassdoor) use aggressive anti-bot tech. If the AI returns a `DATA SOURCE ERROR`, use these alternatives:

1. **Print to PDF:** Open the job post, hit `Ctrl+P` (or `Cmd+P`), and "Save as PDF." Upload the PDF directly to the AI.
2. **Select All & Copy:** Manually highlight the entire page (`Ctrl+A`), copy, and paste the raw text into the prompt.
3. **Screenshot OCR:** Take a screenshot of the full description. Most modern AIs can read the text directly from the image.
4. **Clean View:** Use "Reader Mode" in your browser to strip away ads and pop-ups before copying the text.

---

## 2. Quick Start Workflow

### Step 1: Prepare Inputs
Gather these details to ensure the filename and archive stay organized:
- **Source Type:** (e.g., URL, PDF, Raw Text, Screenshot)
- **Source Location:** (e.g., LinkedIn, Company Career Page)
- **Capture Date:** Today's date.
- **Status Check:** Is the post "Stale"? (Check if it's been up >30 days).

### Step 2: Run Engine
1. Paste the **Job Posting Snapshot Engine (v1.20)** prompt into your AI.
2. Provide your inputs and the job description text.
3. Review the **Strategic Decoder** for immediate "vibe" insights.

### Step 3: Save & Archive
1. Copy **Codeblock 1** for the filename.
2. Copy **Codeblock 2** into a `.md` file.
3. **Save as Immutable:** Do not edit the tags or remove `[NOT LISTED]` entries. This is your "Legal Record."

---

## 3. The Strategic Decoder & Interview Kit

This engine goes beyond data entry. Use the new v1.20 sections to prep your strategy:

- **The Subtext Translation:** If the engine tags `[SUBTEXT] Disorganized`, prepare questions for the recruiter about their project management tools.
- **The Red Flag Check:** If it flags `[RED FLAG] Vague Pay`, make salary transparency your first priority in the screening call.
- **The KPI Hunt:** Look for `[KPI]` tags. These are the specific achievements you must highlight in your resume and interview to prove you can do the job.
- **The Readiness Kit:** Practice the 3 generated questions. They are the "Must-Pass" hurdles of the technical or behavioral interview.

---

## 4. Metadata Indexing (The Master List)

Keep a central CSV or Markdown table to track your archive:

| Company | Role | Main KPI | Red Flags? | Capture Date | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Acme Corp | Sr. PM | 15% Churn Reduction | Vague Salary | 2026-03-01 | Applied |
| Globex | Lead Dev | Cloud Migration | Stale Post | 2026-03-10 | Researching |

---

## 5. "Do Not" Rules

- **Do not edit `[VERBATIM]` bullets.** If they are messy, leave them. They are the proof of what was asked.
- **Do not delete `[NOT STATED]` sections.** Knowing what a company *didn't* mention is often as important as what they did.
- **Do not mix external research into the "Job Snapshot."** Keep the company's claims separate from your outside research (found in Section 5 of the report).

---

## 6. Resume Optimization Workflow

1. Collect 5 Snapshots for similar roles.
2. Identify common **[VERBATIM]** skills and **[KPI]** metrics.
3. Align your resume bullets to these exact phrases where truthful.
4. Use the **[SUBTEXT]** findings to tailor your Cover Letter tone (e.g., if the vibe is "Aggressive/Competitive," use high-energy language).

---

**End of Operations Manual**