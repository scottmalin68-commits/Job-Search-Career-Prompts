# TITLE: LinkedIn Mirror (Extraction & Structure)
# VERSION: 1.2 (NINJA EDITION)
# AUTHOR: Scott M.
# LAST UPDATED: 2026-03-15
============================================================
SUPPORTED AI ENGINES
============================================================
1. Gemini 1.5 Pro / Flash – Best for image processing & large skill dumps.
2. GPT-4o – Strong OCR but can be picky with multiple attachments.
============================================================
CHANGELOG
============================================================
- v1.2 2026-03-15: Added Date Normalization, Continuity Rules, and Description Preservation.
- v1.1 2026-03-15: Added Section Parsing and Multi-Role Handling.
============================================================
SECTION 1 — THE GOAL
============================================================
Extract and structure messy LinkedIn data into a "Canonical Markdown Mirror." This is a data-capture mission. Maintain 100% fidelity to the original text.

============================================================
SECTION 2 — EXTRACTION & CONTINUITY RULES
============================================================
- SCREENSHOT CONTINUITY: Assume captures are sequential. Merge text seamlessly across breaks. Do not create duplicate profiles for repeated sections.
- DESCRIPTION PRESERVATION: Preserve job descriptions EXACTLY as written. No summaries. No rewrites. Maintain all original bullet formatting.
- DATE NORMALIZATION: Convert all dates to YYYY-MM. If only year is present, use YYYY.
- SKILL EXTRACTION: Capture names only. Normalize capitalization. Remove duplicates. Note if a skill is "Endorsed" (Yes/No), but ignore counts and names of endorsers.
- UI CLEANUP: Remove all "See more," "Connect," "Follow," ads, and suggestion boxes.

============================================================
SECTION 3 — EXPERIENCE & COMPANY OBJECTS
============================================================
- MULTI-ROLE HANDLING: If one company has multiple roles, nest them under a single Company Object in chronological order.
- DEDUPLICATION: Verify that companies in Experience match those referenced elsewhere. Education institutions must appear only once.

============================================================
SECTION 4 — THE VACUUM CHECK
============================================================
If a section is not visible in the provided data:
- Mark as: [SECTION NAME] - "status": "not_captured"
- Explicitly prompt the user to capture this missing section.

============================================================
SECTION 5 — THE MIRROR STRUCTURE
============================================================
- # PROFILE MIRROR: [Name]
- ## INTRO_CARD (Headline, Location)
- ## ABOUT_SECTION (Exact text)
- ## EXPERIENCE_SECTION (Nested company/roles)
- ## SKILLS_CATALOG (Categorized: Technical, Tools, Soft)
- ## EDUCATION & CERTS
- ## PROJECTS & VOLUNTEER
- ## VACUUM_REPORT (List of not_captured sections)

============================================================
SECTION 6 — OUTPUT RULES
============================================================
- Output in a single code block. No fluff. 
- Use the middle dot ( · ) for bullets.
============================================================
END OF PROMPT