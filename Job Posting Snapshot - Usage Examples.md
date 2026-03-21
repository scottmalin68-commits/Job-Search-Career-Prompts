# Job Posting Snapshot & Investigative Engine — Operations Manual

**Version:** 3.10 (OSINT Integrated)
**Author:** Scott M.
**Last Updated:** 2026-03-21

---

## 0. The Mission: Intel Over Storage
Most people just bookmark a job link. That’s a mistake. Links die and postings get scrubbed. This engine is a **tactical reconnaissance tool** designed to extract every drop of "leakage" from a job description. We aren't just saving text; we are reverse-engineering their tech stack, identifying their business "pain," and finding the humans who can hire you.

---

## 1. Phase 1: The Capture (Running the Engine)
The engine is your primary prompt. It’s built to handle messy data and turn it into a structured, high-fidelity report.

* **The Input:** Paste the prompt, then paste your data. It handles direct URLs, `Ctrl+A` copy-pastes from defended sites (LinkedIn/Glassdoor), or even OCR text from screenshots.
* **The Output:** The engine generates two specific codeblocks:
    * **Codeblock 1 (The Filename):** A standardized string for your filesystem. Never guess what a file is again.
    * **Codeblock 2 (The Intel Report):** The full breakdown of the role, the tech, and the outreach strategy.

---

## 2. Phase 2: Understanding the "Truth Tags" (Data Integrity)
When you look at your saved markdown file, every bullet point is tagged. We prioritize **integrity** so you know exactly what the company said vs. what the AI figured out.

* **[VERBATIM]:** The raw, unedited truth from the employer.
* **[TECH-CONFIRMED]:** Tools and vendors they explicitly named.
* **[INFERRED/SUBTEXT]:** High-probability logic based on industry standards and "leakage" in the text.
* **[TECH-ROADMAP]:** The "preferred" skills that reveal where their budget is moving.

---

## 3. Phase 3: Investigation vs. Preservation
We don’t just archive; we investigate. The engine automatically triggers these layers:
* **Tech Stack OSINT:** We map their backend architecture based on the tools they ask for.
* **Strategic Decoder:** We identify the *real* problem they are trying to solve (the "Primary Pain").
* **The Hunt:** We generate X-Ray strings to bypass the "black hole" of portals and find the manager directly.

---

## 4. Phase 4: Weaponizing Your Archive (Recursive Prompts)
Once you’ve saved your report, it becomes a **superior data source** for follow-up prompts. Because it’s already structured and "cleaned," you can feed it back into an AI for elite-level prep that far exceeds standard job-board text.

### A. The "Evidence-Based" Interview Prep
> "Using the **[VERBATIM]** and **[KPI]** sections from this archive, give me 3 technical questions I’ll likely face. Use the **[SUBTEXT]** to help me craft an answer that solves their 'hidden' problem."

### B. The Strategic Resume Pivot
> "Match my resume against the **[TECH-CONFIRMED]** list in this file. Rewrite my summary to mirror their specific technical language and address the **[PRIMARY PAIN]** identified in the report."

### C. The "No-Oriented" Outreach
> "Take the **[DIRECT LEAD]** string and the **[TECH-ROADMAP]** info. Draft a 3-sentence email that asks if they are looking for help with [Roadmap Tech] specifically."

### D. The Architectural Audit (Deep-Tech Prep)
> "Act as a Senior Architect. Based on the **[TECH-CONFIRMED]** stack and **[INFERRED ECOSYSTEM]**, identify 3 likely 'technical debt' areas this team is struggling with. Draft a 60-second response for the 'What is your biggest technical challenge?' question that shows I already know their environment's specific friction points."

### E. The High-Leverage Closing (Value-Based)
> "Review the **[PRIMARY PAIN]** and **[KPI]** sections. Draft a closing statement for the final interview that moves the conversation from 'Why should we hire you?' to 'How fast can we solve [Primary Pain] together?' Use the **[TECH-ROADMAP]** to prove I am the long-term solution for their 12-month goals."

---

## 5. Automation Utility (`Create-New-Posting-File.ps1`)
Use this script to bridge the gap. It takes the filename from **Codeblock 1**, creates the file, and lets you dump the intel from **Codeblock 2** inside. It’s the final step in building a searchable, permanent lead database.

---
**End of Operations Manual**