# Job Posting Intelligence Engine — Operations Manual
Version: 4.8.5 (Section 13 X-Ray Expansion Edition) 
Author: Scott M., CISSP
Last Updated: 2026-05-20

============================================================
0. CHANGELOG (THE EVOLUTION)
============================================================
v4.8.5 (2026-05): 
· AUTO-HUNT PROTOCOL: Upgraded Section 13 to a 6-string X-Ray blueprint, adding targeted Team Peers and Company Alumni lookup logic.
· SYNTAX PROTECTION: Enforced a strict pre-processing rule to resolve all bracketed variables inside codeblocks before rendering.

v4.8.4 (2026-05): 
· RENDER PROTECTION: Banned inline source tags inside Part A's code block to prevent corruption during copy-paste workflows.

v4.8.3 (2026-05): 
· BASELINE PROFILING: Added automated fallback to an industry-standard Senior/Principal Cybersecurity & Enterprise Automation Engineer baseline profile if candidate data is missing.
· PLATFORM FINGERPRINTING: Implemented signature text marker tracking to identify target platform backends (Workday, Greenhouse, etc.) when URLs are missing.

v4.8.0 to v4.8.2 (2026-05): 
· DETERMINISTIC WORKFLOW: Hardened the 19-section (0-18) numeric output framework.
· THE FIVE PILLARS: Codified Max Verbosity, Triangulation, Zero Fluff, Delta Logic, and Edge-Case Guardrails.

============================================================
1. THE MISSION: ENGINEERING INTELLIGENCE
============================================================
Most job trackers just bookmark a link. That is an operational failure. Links break and postings get scrubbed. This engine treats every job description as an exhaustive engineering brief. We are here to reverse-engineer departmental economics, surface hidden technical debt, isolate operational landmines via the Risk Surface, and extract resolved OSINT targets to bypass standard recruiting layers.

============================================================
2. PHASE 1: COMPILATION & OUTPUT WORKFLOW
============================================================
· The Ingestion: Drop the Engine (v4.8.5) core logic into memory, populate the three runtime data variables (`[CANDIDATE_PROFILE]`, `[JOB_DESCRIPTION_OR_BASELINE]`, `[DELTA_INTELLIGENCE]`), and let it compile.
· The Output Sequence: The engine executes a strict three-step delivery pipeline:
  · Step 1: Displays Section 0: Executive Fit Summary standalone as a quick preview.
  · Step 2: Generates Codeblock 1 containing only the standard file naming structure: `Posting-Company-Position-ID-YYYYMMDD.md`.
  · Step 3: Generates Codeblock 2 containing the full 19-section engineering report.

============================================================
3. PHASE 2: EVIDENCE TRIANGULATION & RE-EVALUATION
============================================================
To maintain absolute data integrity and combat mid-report laziness, the engine enforces strict sourcing and live update tracking rules:

· Source Anchors: Every standalone claim and paragraph across all 18 major sections must append trailing anchors (e.g., `Source: [JD]`, `Source: [Profile]`, or `Source: [Delta]`).
· Inferred Inferences: If hard facts are missing, the engine performs deep best-practice inferences based on company scale and logs them explicitly as `[INFERRED]`.
· Runtime Delta Cascades: When fresh data or recruiter feedback is dropped into `[DELTA_INTELLIGENCE]`, the engine triggers a dependency cascade. It automatically rewrites downstream sections (Strategic Decoder, Risk Surface, and Interview Pressure Questions) and flags the changes with an `[UPDATED]` tag.

============================================================
4. PHASE 3: EXECUTION OF THE HUNT (SECTION 13)
============================================================
The Auto-Hunt Protocol has been expanded from a basic footprint check into a tactical 6-string X-Ray blueprint. Before outputting, the engine runs a mandatory pre-processing step to completely resolve all bracketed template variables into clear text strings. 

The standalone, copy-ready codeblock yields:
1. Direct Lead: Penetrates the target silo to isolate the true hiring manager.
2. The "Hiring" Post: Uncovers active updates and commentary from inside the immediate team.
3. Skip-Level: Targets the division head or VP driving the high-level budget.
4. The Recruiter: Tracks down the specific talent acquisition gatekeeper.
5. Team Peers: Isolates future colleagues to facilitate peer-level intelligence gathering.
6. Company Alumni: Surfaces warm connections who previously worked at your past companies.

This blueprint is directly backed by the Target Matrix, ranking the top 3 situational personas based on a strict Reply-Probability Scoring Model (0-10).

============================================================
5. PHASE 4: RECURSIVE ARCHIVE PROMPTS (WEAPONIZING THE DATA)
============================================================
Once a report is saved to your local vault, use these specialized queries to run downstream execution tasks:

A. The Vulnerability Exploiter
"Analyze Section 7 (Strategic Decoder) and Section 11 (Risk Surface) from this report. Draft a direct 30-second introductory narrative for a technical call that focuses on stabilization and risk reduction. Link my background directly to solving their active architectural crisis without using any corporate fluff."

B. The Tech Stack Auditor
"Review the Tech Stack matrix and the missing dependencies text block. Identify the top 3 technical debt bottlenecks likely present in this infrastructure. Formulate an answer for the 'Tell me about a time you handled a legacy migration' question that targets these specific friction points."

C. The Kill Criteria Counter-Measure
"Review Section 12 (Kill Criteria) and Section 17 (Data Integrity). Build a list of 4 tactical clarifying questions I must ask during the loop to flush out their internal architecture ambiguity and reverse-verify if this role faces a high burnout vector."

D. The Resume Realignment Engine
"Using the exact keywords isolated in Section 6 (Taxonomy) and the requirements established in Section 9 (Alignment Vector), optimize my professional summary block. Ensure it mirrors their engineering-grade domain context exactly."

============================================================
6. AUTOMATION UTILITY (CREATE-NEW-POSTING-FILE.PS1)
============================================================
Keep using your core local PowerShell script to bridge the gap. It captures the raw text output from Codeblock 1, instantly creates the matching `.md` file structure in your local archive directory, and spins it up in your editor so you can dump the full report from Codeblock 2 straight in.