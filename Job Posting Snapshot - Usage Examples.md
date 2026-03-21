# Job Posting Snapshot & Investigative Engine — Operations Manual

**Version:** 3.20 (Universal OSINT Edition)
**Author:** Scott M.
**Last Updated:** 2026-03-21

---

## 0. Changelog (The Evolution)
* **v3.2 (2026-03):** · **Universal Pivot:** Re-tuned all tech logic to be industry-agnostic (works for Healthcare, Sales, Admin, etc.).
    · **Hiring Manager Detective:** Added deductive logic to identify likely Decision Maker titles based on role seniority.
    · **Burnout Detection:** Integrated the `[KITCHEN-SINK]` tag to flag unrealistic job scopes.
    · **Tactical Toolkit:** Expanded Section 4 to include 5 specialized recursive prompts.
* **v3.1 (2025-12):** · **OSINT Integration:** Added X-Ray search strings and "Tech Leakage" mapping.
    · **Truth Tags:** Standardized `[VERBATIM]`, `[INFERRED]`, and `[TECH-ROADMAP]`.

---

## 1. The Mission: Intel Over Storage
Most people just bookmark a job link. That’s a mistake. Links die and postings get scrubbed. This engine is a **tactical reconnaissance tool** designed to extract every drop of "leakage" from a job description. We aren't just saving text; we are reverse-engineering their operations, identifying their business "pain," and finding the humans who can hire you.

---

## 2. Phase 1: The Capture (Running the Engine)
* **The Input:** Paste the **Snapshot Engine (v3.2)** prompt into your AI, then paste your job data. 
* **Handling Defended Sites:** If LinkedIn or Indeed blocks the URL, use `Ctrl+A` to copy the entire page and paste the raw text. The engine is tuned to filter out the "noise" (headers, footers, and ads) automatically.
* **The Output:** The engine generates two codeblocks:
    · **Codeblock 1 (The Filename):** Standardized naming for your filesystem.
    · **Codeblock 2 (The Intel Report):** The full breakdown of the role and outreach strategy.

---

## 3. Phase 2: Understanding the "Truth Tags"
Every bullet point in your report is tagged to maintain **data integrity**. This ensures you know exactly what the company said vs. what the AI deduced.
* **[VERBATIM]:** Direct, unedited quotes from the employer.
* **[TECH-CONFIRMED]:** Tools, software, or vendors explicitly named.
* **[INFERRED/SUBTEXT]:** Logic based on industry standards and "leakage" in the text.
* **[RED FLAG]:** Warning signs like `[KITCHEN-SINK]` (one person doing the work of three departments).

---

## 4. Phase 3: The Universal Detective (OSINT)
The engine automatically triggers these investigative layers regardless of the industry:
* **Operational Fingerprinting:** Maps the toolset (e.g., "Salesforce" for Sales, "Epic" for Nursing, "Azure" for IT).
* **Hierarchy Mapping:** Deduces the boss's title so your X-Ray strings find the *real* decision maker.
* **The Hunt:** Generates 3 custom LinkedIn X-Ray strings to find the Manager, the Skip-Level VP, and the Recruiter.

---

## 5. Phase 4: Weaponizing Your Archive (Recursive Prompts)
Once you’ve saved your report, it becomes a **superior data source**. Feed your `.md` file back into an AI and use these 5 queries to dominate the process:

#### A. The "Evidence-Based" Interview Prep
> "Using the **[VERBATIM]** requirements from this archive, identify the 3 most likely technical 'gatekeeper' questions. Then, use the **[SUBTEXT]** section to draft a 30-second 'hook' for my self-introduction that proves I understand their internal problems."

#### B. The OSINT Digital Footprint Probe
> "Based on the **[TECH-CONFIRMED]** stack and **[INFERRED ECOSYSTEM]**, identify 3 likely 'technical debt' or 'operational friction' areas this team is struggling with. Draft a response for the 'What is your biggest challenge?' question that shows I already know their environment's specific bottlenecks."

#### C. The Strategic Resume Pivot
> "Match my resume against the **[TECH-CONFIRMED]** list and **[PRIMARY PAIN]** identified in this report. Rewrite my professional summary to mirror their specific terminology and address the 'hidden' problem this company is trying to solve."

#### D. The "No-Oriented" Networking Hook
> "Take the **[DIRECT LEAD]** string and the **[TECH-ROADMAP]** info. Draft a 3-sentence outreach message using a Chris Voss 'No-Oriented' CTA (e.g., 'Would it be a bad idea to...'). It should sound like a peer-to-peer consultation regarding their upcoming shift to [Roadmap Tech]."

#### E. The High-Leverage Closing (Value-Based)
> "Review the **[PRIMARY PAIN]** and **[KPI]** sections. Draft a closing statement for the final interview that moves the conversation from 'Why should we hire you?' to 'How fast can we solve [Primary Pain] together?' Use the **[TECH-ROADMAP]** to prove I am the long-term solution."

---

## 6. Automation Utility (`Create-New-Posting-File.ps1`)
Use the accompanying PowerShell script to bridge the gap. It takes the filename from **Codeblock 1**, creates a blank `.md` file in your archive, and opens it in your editor for you to paste the report.

---
**End of Operations Manual**