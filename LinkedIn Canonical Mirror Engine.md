# TITLE: LinkedIn Canonical Mirror Engine
# VERSION: 1.6.2 (FORENSIC HARDENED)
# FILENAME_TARGET: YYYY-MM-DD_LinkedIn_Canonical_Mirror_Scott_M.md
# AUTHOR: Scott M.

============================================================
PROMPT CHANGELOG:
· v1.6: Initial Forensic logic / Vacuum Report integration.
· v1.6.1: Added middle dot ( · ) formatting, strict truncation rules, and sequence ordering.
· v1.6.2: Hardened image processing flow, added truncation ID tracking, and fixed stacked company role structures.
============================================================

GOAL: Create an exact, structured Markdown replica of a LinkedIn profile from visual screenshots. 
============================================================

SECTION 1 — EXTRACTION RULES
1. NO SUMMARIES: Every bullet must be transcribed 1:1.
2. NO HALLUCINATION: If text is blurry, cut off, or hidden under a "see more" link, mark it inline with a unique identifier like [TRUNCATION_ID_XX]. No guessing.
3. UI CLEANUP: Remove all platform interface elements (buttons, ads, suggested profiles, reaction counts).
4. BULLET STYLE: Use middle dots ( · ) for all list items and bullets.
5. PARSING FLOW: Process images sequentially matching the top-to-bottom layout of the physical LinkedIn profile page, regardless of historical dates.

SECTION 2 — CANONICAL STRUCTURE
Output the data in the following hierarchy:
· ## MIRROR_CAPTURE_DETAILS (Date and capture version)
· ## INTRO_CARD (Name, Headline, Location, Connections)
· ## CONTACT_INFO (Profile URL, Email, Website, Birthday)
· ## ABOUT_SECTION (Full text)
· ## EXPERIENCE_SECTION 
     · For single roles: Company, Title, Dates, Location, Every Bullet.
     · For nested roles (same company): Company Name -> Sub-roles listed sequentially with respective Title, Dates, Location, and Bullets.
· ## LICENSES_AND_CERTIFICATIONS (Name, Issuer, ID, Associated Skills)
· ## SKILLS_CATALOG (Categorized as seen on LinkedIn)
· ## HONORS_AND_AWARDS
· ## INTERESTS_AND_GROUPS (Companies, Schools, Groups, Newsletters)

SECTION 3 — THE VACUUM REPORT
At the end of the mirror, provide a "Vacuum Report" list:
1. "status": "captured" or "not_captured" for every major section.
2. "truncation_list": Map each unique [TRUNCATION_ID_XX] used inline to a specific description of what data was hidden by the UI.
3. "hallucination_check": Flag any dates or names that seem inconsistent or require human verification.

============================================================
EXECUTION: Parse the attached images and generate the Mirror.
============================================================