# OSINT JSON → NotebookLM Source Pack Renderer
# VERSION: 1.0.0
# AUTHOR: Scott Malin, CISSP
# LAST UPDATED: 2026-08-12

============================================================
CHANGELOG
============================================================
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
· FALLBACK RULE: If data is missing, write "[Data Not Available]" so NotebookLM does not guess during Audio Overviews.

============================================================
OUTPUT FORMAT (STRICT)
============================================================
Output MUST begin on line 1 with ```markdown (Codeblock 1). No conversational intro or outro.

Return exactly three markdown code blocks:

Codeblock 1 – Filename manifest (3 raw strings, one per line):
[Company]-[Role]-01-RoleIntelligence.txt
[Company]-[Role]-02-CandidateAlignment.txt
[Company]-[Role]-03-InterviewPrepBrief.md

Codeblock 2 – Source Document 1: Role & Company Intelligence
(Plain text file optimized for NotebookLM context reading)

Codeblock 3 – Source Document 2: Candidate Alignment & Stories
(Plain text file mapping experience to role needs)

============================================================
SOURCE DOCUMENT 1 STRUCTURE (Role Intelligence)
============================================================

# ROLE & COMPANY INTELLIGENCE: [Company] - [Role]
Generated: [Date]

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

## 3. High-Value Questions to Ask
- Question 1 (Technical/Operational): [Question text]
- Question 2 (Culture/Team): [Question text]

============================================================
INPUT
============================================================
[OSINT_JSON_REPORT]
[CANDIDATE_PROFILE]