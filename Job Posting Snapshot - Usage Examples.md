# Job Posting Snapshot & Investigative Engine — Operations Manual
Version: 3.5.2 (Universal OSINT Edition) 
Author: Scott M. 
Last Updated: 2026-03-21

============================================================
0. CHANGELOG (THE EVOLUTION)
============================================================
v3.5.2 (2026-03): 
· FISCAL ARCHITECTURE: Added Salary/Compensation tracking and [COMP-BENCHMARK] tagging.
· MARKET ESTIMATION: Integrated logic to infer pay ranges based on seniority + geography if not disclosed.
· RE-INTEGRATION: Restored compensation fields missing since v1.8.

v3.5.1 (2026-03): 
· VULNERABILITY MAPPING: Added "Trigger/Vulnerability Map" to identify the "Why Now?" (Breach, Audit, Turnover).  
· LOGIC REFINEMENT: Clarified Data vs. Opportunity Integrity.  

v3.5.0 (2026-03): 
· INTELLIGENCE HUB UPGRADE: Integrated Role Reality Deconstruction and Opportunity Integrity Scan.  

v3.2.0 (2026-03): 
· UNIVERSAL PIVOT: Re-tuned all tech logic to be industry-agnostic.
· BURNOUT DETECTION: Integrated the [KITCHEN-SINK] tag.

============================================================
1. THE MISSION: INTEL OVER STORAGE
============================================================
Most people just bookmark a job link. That’s a mistake. Links die and postings get scrubbed. This engine is a tactical reconnaissance tool designed to extract every drop of "leakage" from a job description. We aren't just saving text; we are reverse-engineering their operations, identifying their business "pain," and finding the humans who can hire you.

============================================================
2. PHASE 1: THE CAPTURE (RUNNING THE ENGINE)
============================================================
· The Input: Paste the Snapshot Engine (v3.5.2) prompt into your AI, then paste your job data.
· Handling Defended Sites: If LinkedIn or Indeed blocks the URL, use Ctrl+A to copy the entire page and paste the raw text. The engine is tuned to filter out the "noise" automatically.
· The Output: The engine generates two codeblocks: 
    1. Codeblock 1 (The Filename): Standardized naming for your filesystem. 
    2. Codeblock 2 (The Intel Report): The full breakdown of the role and outreach strategy.

============================================================
3. PHASE 2: UNDERSTANDING THE "TRUTH TAGS"
============================================================
Every bullet point in your report is tagged to maintain data integrity. 

· [VERBATIM]: Direct, unedited quotes from the employer.
· [TECH-CONFIRMED]: Tools, software, or vendors explicitly named.
· [TECH-PROBABLE/ROADMAP]: Logic based on industry standards and "leakage" in the text.
· [COMP-BENCHMARK]: Inferred pay based on market data/seniority/geo (e.g., Hartford market).
· [RED FLAG]: Warning signs like [KITCHEN-SINK] (one person doing the work of three departments).

============================================================
4. PHASE 3: THE STRATEGIC LAYERS
============================================================
The engine automatically triggers these investigative layers:

· Vulnerability Map: Identifies the "Why Now?" trigger (e.g., Breach, Audit, M&A, Turnover).
· Opportunity Integrity Layer: Detects "Shadow Candidates" or "Ghost Job" signals to assess if the role is genuinely open.
· Hierarchy Mapping: Deduces the boss's title so your X-Ray strings find the real decision maker.
· The Hunt: Generates 3 custom LinkedIn X-Ray strings to find the Manager, the Skip-Level VP, and the Recruiter.

============================================================
5. PHASE 4: WEAPONIZING YOUR ARCHIVE (RECURSIVE PROMPTS)
============================================================
Once saved, use these 5 queries to dominate the process:

A. The Fiscal Negotiator
"Using the [COMP-BENCHMARK] and [PRIMARY PAIN] from this report, draft a negotiation script for the initial recruiter screen. Anchor the conversation at the high end of the market range by linking my experience to solving their specific [Vulnerability Map] trigger."

B. The "Integrity" Reality Check
"Review the Opportunity Integrity Scan. If the risk is Likely Pre-Selected, identify 3 specific questions I can ask to 'flush out' whether they are genuinely open to external talent or just fulfilling a posting requirement."

C. The "Why Now?" Interview Hook
"Based on the Vulnerability Map (likely Crisis/Audit), draft a 30-second introduction focusing on 'Stabilization and De-risking.' Prove I have handled a similar [Primary Pain] in the past without using marketing fluff."

D. The OSINT Digital Footprint Probe
"Based on the [TECH-CONFIRMED] stack and [INFERRED ECOSYSTEM], identify 3 likely 'technical debt' areas. Draft a response for the 'What is your biggest challenge?' question that shows I already know their environment's bottlenecks."

E. The Strategic Resume Pivot
"Match my resume against the [TECH-CONFIRMED] list and [PRIMARY PAIN]. Rewrite my professional summary to mirror their specific terminology and address the 'hidden' problem this company is trying to solve."

============================================================
6. AUTOMATION UTILITY (CREATE-NEW-POSTING-FILE.PS1)
============================================================
Use the accompanying PowerShell script to bridge the gap. It takes the filename from Codeblock 1, creates a blank .md file in your archive, and opens it in your editor for you to paste the report.
