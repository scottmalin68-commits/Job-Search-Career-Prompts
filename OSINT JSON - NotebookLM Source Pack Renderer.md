# OSINT JSON → NotebookLM Source Pack Renderer
# VERSION: 1.1.0
# AUTHOR: Scott Malin, CISSP
# LAST UPDATED: 2026-08-12
============================================================
CHANGELOG
============================================================
v1.1.0 (2026-08-12)
· Fully defined the third source document (Interview Prep Brief).
· Added Missing Data & Error Handling rules.
· Added explicit Evidence Grade decision criteria.
· Added soft length / density targets for NotebookLM quality.
· Standardized date format (YYYY-MM-DD) and required Data Gaps surface at top of documents when material.
· Expanded output to four clean code blocks (manifest + three source documents).
· Minor heading and density refinements for better Audio Overview chaptering and citation grounding.

v1.0.0 (2026-08-12)
· Initial release tailored specifically for NotebookLM source loading.
· Generates two distinct, hyper-grounded source documents: Role Intelligence & Candidate Fit.
· Formatted to maximize NotebookLM features (Audio Overview, Chat Grounding, Briefing Docs).
· Strictly eliminates complex markdown styling that confuses NotebookLM parsing.
============================================================
PURPOSE
============================================================
Convert structured OSINT JSON + candidate profile into clean, highly readable source documents built specifically to be uploaded into Google NotebookLM.
Goal: Create a dedicated NotebookLM notebook for a specific job application that powers clean Audio Overviews (podcasts), Q&A chat, and study guides without hallucination or context loss.
============================================================
REQUIRED INPUTS
============================================================
1. OSINT_JSON_REPORT
   - Full JSON output from the Unified Posting Investigation Engine (v1.3.0+)
2. CANDIDATE_PROFILE
   - Career Profile, Master Skills Summary, or Resume text
============================================================
CORE RULES FOR NOTEBOOKLM OPTIMIZATION
============================================================
· NotebookLM needs plain, direct, clean context. Avoid complex nesting, tables, or excessive symbols.
· Keep facts tightly linked to headings so NotebookLM citations point to exact context.
· DO NOT invent facts. NotebookLM's primary strength is grounded retrieval; feeding it made-up data ruins its chat accuracy.
· Prefer short, declarative headings. Repeat critical proper nouns (company name, role title, key tools) near the top of sections to strengthen retrieval anchors.
· Soft length targets (prioritize density over exhaustiveness):
  - Role & Company Intelligence: 800–1,800 words
  - Candidate Alignment & Stories: 600–1,400 words
  - Interview Prep Brief: 400–900 words
· FALLBACK RULE: If data is missing, write "[Data Not Available]" so NotebookLM does not guess during Audio Overviews.

MISSING DATA & ERROR HANDLING
· If any required top-level key in the OSINT JSON is missing, null, or empty, continue processing and mark affected fields as "[Data Not Available]".
· Do not halt or invent values.
· If a document contains three or more significant "[Data Not Available]" entries in core sections, add a short "Data Gaps" note at the very top of that document (after the title) listing the missing areas.
· Date format is always YYYY-MM-DD. Use the current date unless a specific generation date is supplied in the input.

EVIDENCE GRADE DECISION CRITERIA
· Strong = Direct metric + tool/technology + clear outcome present in CANDIDATE_PROFILE
· Moderate = Tool/technology + outcome present, or strong thematic match with supporting detail
· Weak-Inferred = Only thematic or inferred match; no concrete metric or named tool from the profile
============================================================
OUTPUT FORMAT (STRICT)
============================================================
Output MUST begin on line 1 with ```markdown (Codeblock 1). No conversational intro or outro.
Return exactly four markdown code blocks:

Codeblock 1 – Filename manifest (3 raw strings, one per line):
[Company]-[Role]-01-RoleIntelligence.txt
[Company]-[Role]-02-CandidateAlignment.txt
[Company]-[Role]-03-InterviewPrepBrief.md

Codeblock 2 – Source Document 1: Role & Company Intelligence
(Plain text file optimized for NotebookLM context reading)

Codeblock 3 – Source Document 2: Candidate Alignment & Stories
(Plain text file mapping experience to role needs)

Codeblock 4 – Source Document 3: Interview Prep Brief
(Concise rapid-recall document for last-minute review and Audio Overview)
============================================================
SOURCE DOCUMENT 1 STRUCTURE (Role Intelligence)
============================================================
# ROLE & COMPANY INTELLIGENCE: [Company] - [Role]
Generated: [YYYY-MM-DD]

[Optional Data Gaps note if applicable]

## 1. Executive Summary & Hiring Intent
- Decision Recommendation: [Apply / Light Apply / Skip]
- Role Opportunity Score: [X/10]
- Candidate Fit Score: [Y/10]
- Primary Reason: [1-2 sentences]
- Real Hiring Intent: [Why this role exists, ghost job risk, urgency]

## 2. Company Culture & Work Pressure
- Management Style & Expectations: [Bullets from JSON]
- Known Red Flags or Wasted Time Risks: [Bullets from JSON]
- Cultural Pressure Points: [Bullets from JSON]

## 3. Core Technical & Operational Pains
- Primary Problem To Solve 1: [Details]
- Primary Problem To Solve 2: [Details]
- Primary Problem To Solve 3: [Details]

## 4. Stakeholder Dynamics
- Recruiter Focus: [What they care about]
- Hiring Manager Focus: [What they care about]
- Skip-Level / Executive Focus: [What they care about]
============================================================
SOURCE DOCUMENT 2 STRUCTURE (Candidate Alignment)
============================================================
# CANDIDATE ALIGNMENT & INTERVIEW STORIES: [Candidate Name] -> [Company]
Generated: [YYYY-MM-DD]

[Optional Data Gaps note if applicable]

## 1. Primary Positioning Strategy
- Core Narrative Angle: [One sentence on how candidate frames themselves]
- Top Strengths to Lead With: [2-3 items with concrete metrics/tools strictly from CANDIDATE_PROFILE]
- Topics/Weaknesses to Avoid: [1-2 items to deflect]

## 2. Prioritized Interview Stories
Story 1: [Story Title]
- Story Type: [Technical / Leadership / Problem Solving]
- Problem Statement: [Role pain point this solves]
- Candidate Evidence Hook: [Specific metric, tool, outcome from CANDIDATE_PROFILE]
- Evidence Grade: [Strong / Moderate / Weak-Inferred]

Story 2: [Story Title]
- Story Type: [Technical / Leadership / Problem Solving]
- Problem Statement: [Role pain point this solves]
- Candidate Evidence Hook: [Specific metric, tool, outcome from CANDIDATE_PROFILE]
- Evidence Grade: [Strong / Moderate / Weak-Inferred]

Story 3: [Story Title] (optional if strong evidence exists)
- Story Type: [Technical / Leadership / Problem Solving]
- Problem Statement: [Role pain point this solves]
- Candidate Evidence Hook: [Specific metric, tool, outcome from CANDIDATE_PROFILE]
- Evidence Grade: [Strong / Moderate / Weak-Inferred]

## 3. High-Value Questions to Ask
- Question 1 (Technical/Operational): [Question text]
- Question 2 (Culture/Team): [Question text]
- Question 3 (Role Success / 90-Day): [Question text]
============================================================
SOURCE DOCUMENT 3 STRUCTURE (Interview Prep Brief)
============================================================
# INTERVIEW PREP BRIEF: [Company] - [Role]
Generated: [YYYY-MM-DD]

[Optional Data Gaps note if applicable]

## 1. 30-Second Positioning
[One tight paragraph the candidate can say or adapt]

## 2. Must-Hit Stories (Ranked)
1. [Story Title] – [One-sentence hook + Evidence Grade]
2. [Story Title] – [One-sentence hook + Evidence Grade]
3. [Story Title] – [One-sentence hook + Evidence Grade] (if available)

## 3. Critical Questions to Ask
- [Question 1]
- [Question 2]
- [Question 3]

## 4. Red Flags & Deflection Points
- [Red flag or sensitive topic + suggested deflection]

## 5. Final Reminders
- [2-4 ultra-short bullets: energy, metrics to emphasize, things to avoid]
============================================================
INPUT
============================================================
[OSINT_JSON_REPORT]
[CANDIDATE_PROFILE]