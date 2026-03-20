# Job Posting Snapshot & Preservation Engine – Operations Manual

**Version:** 2.50  
**Author:** Scott M  
**Last Updated:** 2026-03  

---

## 0. Mission & Objective
The goal of this engine is **strategic intelligence**, not just storage. Standard job boards are ephemeral and often scrubbed of context. This process creates a permanent, high-fidelity archive that combines **[VERBATIM]** posting data with deep-dive research into company financials, leadership vibes, and cultural red flags. The resulting file is a "living document" that protects the applicant from toxic environments and provides a roadmap for a "must-hire" interview.

---

## 1. Data Capture: Standard vs. "Fortress" Sites
Most sites work with a simple URL. Start there first.

· **Standard Method:** Paste the URL into the AI. The engine fetches and processes the data instantly.
· **Defended Sites:** Sites like **Glassdoor**, **LinkedIn**, and **Indeed** often use anti-bot shields.
· **Workarounds:**
  · **Select All & Copy:** Use `Ctrl+A` on the job page and paste the text directly.
  · **Print to PDF:** Save the page as a PDF and upload it.
  · **Screenshot OCR:** Upload an image of the post for the AI to read.

---

## 2. Quick Start Workflow
1. **Capture:** Try the URL first. Fall back to copy-paste or PDF if blocked.
2. **Select Logic (Optional):** Choose a logic module if you need a deeper dive (e.g., "Use Logic 06 to red-team this").
3. **Run Engine:** Paste the **Snapshot Engine (v2.50)** prompt and your data into the AI.
4. **Generate Filename:** Copy the clean string from **Codeblock 1**.
5. **Create File:** Run the `Create-New-Posting-File.ps1` utility and paste the filename.
6. **Save:** Paste the report from **Codeblock 2** into your editor and save.

---

## 3. Advanced Analysis: Logic Toggles & Culture Radar
v2.50 introduces **Logic Toggles** to overclock the AI's reasoning. Call these out when starting the engine:

· **[05] Step-Back:** Identifies the "real" business problem they are hiring for.
· **[06] Adversarial:** Red-teams the post for toxic "always-on" culture or hidden traps.
· **[13] Verification:** Forces the AI to cross-reference every claim against the verbatim text.
· **Culture Radar:** Checks for leadership presence, employee tenure, and "growth vs. grind" signals based on the healthy culture infographic.

---

## 4. High-Fidelity Execution: Using Your Archive
To ensure you don't waste the high-quality data you've captured, use these specific "recursive" queries. 

### A. The "Evidence-Based" Interview Prep
> "Act as a specialized interviewer for this role. Based ONLY on the [VERBATIM] requirements and the [KPI] success metrics in this archive, identify the 3 most likely technical 'gatekeeper' questions. Then, use the [SUBTEXT] section to draft a 30-second 'hook' for my self-introduction that proves I understand their internal problems."

### B. The Strategic Resume Pivot
> "Review my resume against the [VERBATIM] skills and [KPI] sections of this snapshot. Rewrite my professional summary to mirror their specific terminology. Use the [SUBTEXT] findings to add one bullet point to my most recent role that addresses the 'hidden' problem this company is trying to solve."

### C. The Culture "Acid Test"
> "Look at the [CULTURE RADAR] and [RED FLAG] sections. Generate 3 polite but pointed questions for the Hiring Manager that will force them to reveal the truth about the 'always-on' or 'tenure' issues identified in the snapshot. Do not use generic questions."

---

## 5. Automation Utility (`Create-New-Posting-File.ps1`)
Use this PowerShell script to bridge the gap between AI output and your archive.

· **How it works:** It prompts for a filename, creates a blank `.md` file, and opens it in your preferred editor.
· **Safety Features:** It displays file metadata if a duplicate name is found and requires "y/n" confirmation.
· **Configuration:** Set your `$EditorPath` (e.g., to Notepad++) within the script logic.

---

## 6. Archival Rules
· **Preserve Purity:** Never edit **[VERBATIM]** text. This is your official record.
· **Respect the Tags:** Keep **[NOT LISTED]** entries; they signal what the company *is not* focusing on.
· **Version Control:** If a job post is updated, save a new file. Do not overwrite original captures.

---
**End of Operations Manual**