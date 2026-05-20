# TITLE: LinkedIn Headhunter Magnet
# VERSION: 1.2.3 (SEMANTIC ENGINE & COGNITIVE GUARDRAIL REFRESH)
# AUTHOR: Scott M. / Lucy’s "Lazy Smart" Logic
# LAST UPDATED: 2026-05-20

# CHANGELOG
v1.2.2: Added SKILL VALIDATION GATE, HUMAN POLISH PROTOCOL, SAGE SEO Fix, and 3-role Problem Statement limit.
v1.2.3: Hardened 50-skill limit against hallucination loops, isolated the 2-line limit to narrative paragraphs, and split the master export into modular code blocks to prevent token truncation.

============================================================
SUPPORTED AI ENGINES: Grok 4 | GPT-5 | Claude 3.5
============================================================

# SECTION 1 — THE INPUT
[REQUIRED]
SOURCE OF TRUTH: (Paste Resume or Skills Doc)
TARGET ROLE: (The title you want to be headhunted for)
TARGET INDUSTRY: (The specific sector)
TARGET SENIORITY: (Entry / Mid / Senior / Lead / Principal)
LOCATION: (Current or desired work location)

# SECTION 2 — THE PASSIVE AUDIT (LUCY + SCOTT LOGIC)
1. THE MARKET-TITLE ALIGNMENT: Convert internal titles to recruiter-facing standards.
2. THE INDUSTRY ANCHOR: Force TARGET INDUSTRY into Headline + About to fix auto-tagging.
3. THE SEMANTIC ENGINE: Inject Top 5 Keywords + their "Semantic Neighbors" (e.g., if 'Python' is used, include 'Django' or 'FastAPI' to validate Topic DNA).
4. THE 50-SKILL SATURATION: Extract up to 50 Hard Skills maximum. Do not invent, duplicate, or split skills if the source text contains fewer than 50 valid entries.
5. THE MOBILE HOOKS (2026 REFRESH):
   - HEADLINE: Primary value must appear in the first 70 characters.
   - ABOUT: Top metric must appear in the first 140 characters (before the 'See More' cut).

# SECTION 3 — THE WRITING RULES (ANTI-AI & HIGH DISTRACTION)
- RHYTHM & FLOW: Use varied sentence lengths. No "AI-voice" (e.g., "In today's fast-paced world").
- HUMAN POLISH: Use standard sentence casing and proper grammar. 
- THE 2-LINE LIMIT: Appears only in the narrative blocks of the ABOUT section. No paragraph longer than two lines.
- THE 1:1 METRIC RULE: Every bullet in the experience section must include a number ($, %, time, or scale).
- PROBLEM STATEMENT FORMAT: Apply to experience bullets. Business pain + system + impact (≤15 words per bullet).
- BANNED WORD KILL-SWITCH: No Orchestrated, Spearheaded, Passionate, Synergize.
- USE PLAIN VERBS: Built, Fixed, Ran, Reduced, Automated.

# SECTION 4 — REALITY & VALIDATION (ANTI-HALLUCINATION)
- SKILL VALIDATION GATE: Every skill suggested MUST be linked to a specific fact in the SOURCE OF TRUTH.
- NO FABRICATION: If a metric is missing, use [X%] or [X] as a placeholder. Do not guess numbers.
- LOGIC MAP: Explain exactly WHY a change was made to hit recruiter filters.

# SECTION 5 — THE OUTPUT WORKFLOW
1. SEO DIAGNOSIS: Score (1–10) + Saliency Gap + Semantic Neighbor terms used.
2. THE RECRUITER LOGIC MAP: 3-5 bullet points explaining the "why" behind the strategy.
3. THE 50-SKILL DUMP: Categorized list (copy-paste ready).
4. THE SURGERY: Headline, About, and Experience rewrites.
   - NOTE: Apply "Problem Statement" format ONLY to the 3 most recent roles.
5. THE LAZY VISIBILITY SYSTEM: 100-Touch Tactic + 3 Content Prompts + Recruiter DM.

# SECTION 6 — THE MASTER EXPORT
[A] ANALYSIS & LOGIC (NORMAL TEXT)
- SEO Score, Logic Map, and Visibility System.

[B] FINAL LINKEDIN PROFILE (MODULAR CODE BLOCKS ONLY)
- Output the clean, ready-to-paste text using sequential markdown code blocks for each section below to prevent output truncation:
  - Code Block 1: Headline & About Section
  - Code Block 2: Experience Section (Top 3 roles formatted, remaining roles preserved with clean text)
  - Code Block 3: Skills Catalog & Certifications
============================================================
END OF PROMPT