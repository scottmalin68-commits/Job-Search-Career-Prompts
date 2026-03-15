# Job Posting Snapshot & Preservation Engine – Operations Manual

**Version:** 2.4  
**Author:** Scott M  
**Last Updated:** 2026-03  

---

## 1. Data Capture: Standard vs. "Fortress" Sites

Most sites work with a simple URL. Start there first.

* **Standard Method:** Paste the URL into the AI. The engine fetches and processes the data instantly for most job boards.
* **Defended Sites:** Sites like **Glassdoor**, **LinkedIn**, and **Indeed** often use anti-bot shields.
* **Workarounds:** * **Select All & Copy:** Use `Ctrl+A` on the job page and paste the text directly.
    * **Print to PDF:** Save the page as a PDF and upload it.
    * **Screenshot OCR:** Upload an image of the post for the AI to read.

---

## 2. Quick Start Workflow

1.  **Capture:** Try the URL first. Fall back to copy-paste or PDF if blocked.
2.  **Run Engine:** Paste the **Snapshot Engine (v1.20)** prompt and your data into the AI.
3.  **Generate Filename:** Copy the clean string from **Codeblock 1**.
4.  **Create File:** Run the `Create-New-Posting-File.ps1` utility and paste the filename.
5.  **Save:** Paste the report from **Codeblock 2** into your editor and save.

---

## 3. Automation Utility (`Create-New-Posting-File.ps1`)

Use this PowerShell script (available on Scott M’s GitHub) to bridge the gap between AI output and your archive.

* **How it works:** It prompts for a filename, creates a blank `.md` file, and opens it in your preferred editor (Notepad++, etc.).
* **Safety Features:** It displays file metadata (size, last modified) if a duplicate name is found and requires a "y/n" confirmation before overwriting.
* **Configuration:** You can set your `$EditorPath` (e.g., to Notepad++) within the script logic.

---

## 4. Strategic Briefing & Interview Prep

Don't just archive the data—read the **Strategic Decoder** and **Interview Kit** results:

* **[SUBTEXT]:** Identifies unspoken culture or hidden demands (e.g., "wear many hats" = lean team).
* **[RED FLAG]:** Spots risks like vague compensation, high-churn language, or stale postings.
* **[KPI]:** Highlights the actual metrics the company values. Use these to tailor your resume.
* **Interview Kit:** Generates the 3 most likely "Must-Pass" questions based on **[VERBATIM]** requirements.

---

## 5. Troubleshooting: Identifying "The Block"

If the URL method fails, look for these signs to know when to switch to a workaround:

* **"DATA SOURCE ERROR":** Usually means a 403 (Forbidden) or 401 (Unauthorized) response.
* **"CAPTCHA detected":** The site is challenging the AI to prove it is human.
* **"Empty Output / No Job Detected":** Likely due to Javascript-heavy pages. If the report is all `NOT LISTED`, the AI didn't "see" the content.
* **"Access Denied":** Direct confirmation that the bot-blocker is active.

---

## 6. Archival Rules

* **Preserve Purity:** Never edit **[VERBATIM]** text. This is your official, legal record.
* **Respect the Tags:** Keep **[NOT LISTED]** entries; they signal what the company *is not* focusing on.
* **Version Control:** If a job post is updated later, save a new file. Do not overwrite your original capture.

---
**End of Operations Manual**