# TITLE: Master Skills & Experience Summary Generator
# VERSION: 2.2.0
# AUTHOR: Scott M
# LAST UPDATED: 2026-05-21

============================================================
CHANGELOG
============================================================
v2.2.0 (2026-05-21)
· Added: Guardrails for Trend Drift by strictly anchoring allowed research sources.
· Added: Chain-of-Verification (CoV) system to prevent skill inflation and hallucinated STAR proof.
· Fixed: Hardened formatting cages to prevent layout drift across future model weight updates.

============================================================
PROMPT IMPLEMENTATION CODE
============================================================
# Prompt Name: Master Skills & Experience Summary Generator

## Goal
Create a polished, ATS-optimized markdown document summarizing skills, experience, and achievements tailored to the user's target role/industry. Include a Top 10 market-demand skills matrix (researched), honest skill mapping, gap plan, role-tagged bullets, LinkedIn summary, recruiter email template, and optional interview prep addendum. This markdown file serves as the master record for building resume revisions, job evaluations, performance reviews, and career progression tracking—ensuring consistency across all professional artifacts.

## Audience
Professionals in tech, cybersecurity, IT, or related fields updating resumes, LinkedIn profiles, or preparing for interviews. Tone is professional, encouraging, and lightly geeky (with a single fun sci-fi close).

## Guardrails & Verification Logic (Internal Processing)
Execute these steps internally before generating any response text to prevent AI drift:
1. Verification Step: Review the provided USER INPUT data. For every skill placed in the Top 10 Matrix, verify that the user's raw input contains explicit evidence for it. If no explicit evidence exists, the skill level MUST be marked "Partial" or "No" and sent to the Gap Plan. Never invent dates, tools, or metrics.
2. Source Filtering: When executing web searches for skills trends, discard generic blog posts or content aggregator sites. Restrict focus to trusted platforms: LinkedIn Economic Graph, Indeed Hiring Lab, Glassdoor, O*NET, BLS, and Levels.fyi.

## Formatting Rules
· Bullet Characters: ALWAYS use the middle dot ( · ) for all vertical lists and bullet points. No standard hyphens or asterisks for bullets.
· Eye-Tracking Metrics: Identify all quantitative results, percentages, and dollar amounts. Convert them to Unicode Sans-Serif Bold characters (e.g., 𝟓𝟎%, 𝟏𝟎𝟓,𝟎𝟎𝟎) to guide the reader's eye directly to metrics.
· Layout Cage: The entire generated response output must be housed within a single, continuous markdown codeblock wrapper.

## Output Structure
Show the full generated document inside a single codeblock using this exact sequence:

# [USER NAME] – Master Skills & Experience Summary

*Last Updated: [CURRENT DATE & TIME EST] – **PATCH v[YYYY-MM-DD-HHMM]** applied*  
*Latest Revision: [CURRENT DATE & TIME EST]*

## Goal
Target role/industry: [USER JOB GOAL]  
Focus: Goal-first optimization for ATS, recruiter scans, and interview storytelling. Honest mapping of user evidence only—no fabrication. Use as master record for resume revisions, job evaluations, and career tracking.

## Professional Overview
[1-paragraph bio: years exp, companies, top 3 wins **tied to job goal**, key tools, location/remote preference.]

## Areas of Expertise
[Group technical categories here by job goal relevance using middle dot lists]

## Top 10 Market-Demand Skills Matrix & Key Accomplishments
[Generate a markdown table mapping the top 10 verified skills discovered via the filtered research process. Columns: #, Skill, Level (Expert/Strong/Partial/No), STAR Proof / Note (Apply Unicode Bold to Metrics), ATS Keywords]

## Skill Gap Action Plan
*Review & strengthen these to close the gap (limit to top 3–4 gaps):*
· **[Skill X] (Partial/No)** → _Suggested proof: [realistic tool/project/date idea]_  
  _→ Add story/tool/date to strengthen?_
· **[Skill Y] (Partial/No)** → _Fast-track: [free/low-cost resource – Coursera, freeCodeCamp, YouTube, vendor trial, etc.]_

## Core Expertise Areas – Role-Tagged (GROUP BY JOB GOAL RELEVANCE)
### [Most Relevant Section Title]
· [Bullet with Unicode bold metric + date]  
  **Role:** [Role → Role – Company, Date Range]

[Repeat sections, ordered by descending goal fit]

## Early Career Highlights
· [Bullet with Unicode bold metric]  
  **Role:** [Early Role – Company, Date Range]

## Technical Competencies
· **Category**: Tools/Skills (highlight goal-related)

## Education
· [Degree / School / Year]

## Certifications
· [Cert / Issuer / Year]

## Security Clearance
· [Status / Level / Date if applicable]

## One-Click LinkedIn Summary ([~1400 chars])
[Open with job goal hook, weave in keywords, end with call-to-action]

## Recruiter Email Template
Subject: [USER NAME] – Your Next [JOB GOAL TITLE] ([LOCATION/Remote])  
Hi [Name],  
[3-line hook tied to goal + 1 strong Unicode bold metric]  
Best regards,  
[USER NAME]  
[Phone] | [LinkedIn URL]

## Usage Notes
Master reference document. **[YEARS]** years of experience = interview superpower.  
Skills & trends sourced from live job postings and reports on [LinkedIn, Indeed, Glassdoor, Levels.fyi, O*NET] as of [CURRENT DATE EST].  
PATCH v[YYYY-MM-DD-HHMM] applied.

## Changelog
· 2026-05-21: Upgraded baseline to v2.2.0; injected anti-drift guardrails, source filtering targets, and Chain-of-Verification steps to maintain data integrity.
· 2026-05-21: Upgraded layout for structural hierarchy, forced markdown output into an explicit single codeblock wrapper, applied middle dot list mandates, and integrated Unicode eye-tracking metrics.
· 2026-02-04: Added Recommended AI Engines section; enhanced Goal to emphasize master record usage.
· 2026-01-20: Initial baseline release.

OPTIONAL MODE – INTERVIEW PREP ADDENDUM  
If user says “interview style”, “prep mode”, “add interview section”, or similar, **append** this after Skill Gap Action Plan:

## Interview Prep – Behavioral & Technical Flashcards
**Top 8 Anticipated Questions for [JOB GOAL]** (based on recent Glassdoor, Levels.fyi, Reddit r/cscareerquestions trends)

1. **Question:** [Common behavioral/technical question tied to Top Skill #1 or job goal]  
   **Your STAR Answer:** [Pull from matrix STAR Proof or user input; if weak/absent: “Need story? Suggest adding example of [related project/tool]”]  
   **Tip:** Quantify impact with eye-tracking bold metrics, tie to business outcome, practice aloud.

[Repeat for 8 questions total – mix behavioral, technical, system design as relevant to role]

**Quick Interview Tips:**
· Always STAR method
· Lead with results when possible
· Prepare 2–3 questions for them

**FUN SCI-FI CLOSE**  
(add ONLY at the very end of the full output, one random non-inspirational quote, never repeat in session):  
_“[Geeky/absurd quote, e.g., 'These aren't the droids you're looking for.']”_

RULES:
· Role-tag every bullet
· Honest & humble – NEVER invent experience
· Goal-first, ATS gold
· Friendly, professional tone
· All markdown tables
· CURRENT DATE/TIME: [INSERT TODAY'S DATE & TIME EST]