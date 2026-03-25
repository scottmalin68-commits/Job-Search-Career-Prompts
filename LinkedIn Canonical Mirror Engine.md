# TITLE: LinkedIn Canonical Mirror Engine
# VERSION: 1.61 (FINAL FORENSIC)
# FILENAME_TARGET: YYYY-MM-DD_LinkedIn_Canonical_Mirror_Scott_M.md
# AUTHOR: Scott M.

============================================================
PROMPT CHANGELOG:
· v1.6: Initial Forensic logic / Vacuum Report integration.
· v1.61: Added middle dot ( · ) formatting, strict 
        truncation rules, and sequence ordering.
============================================================

GOAL: Create an exact, structured Markdown replica of a 
LinkedIn profile from visual screenshots. 
============================================================

SECTION 1 — EXTRACTION RULES
1. NO SUMMARIES: Every bullet must be transcribed 1:1.
2. NO HALLUCINATION: If text is blurry, cut off, or hidden under 
   a "see more" link, mark as [UNREADABLE/TRUNCATED]. No guessing.
3. UI CLEANUP: Remove all platform interface elements (buttons, ads, 
   suggested profiles, reaction counts).
4. BULLET STYLE: Use middle dots ( · ) for all list items and bullets.
5. SEQUENCE: Process images in chronological order to maintain 
   the profile's original flow.

SECTION 2 — CANONICAL STRUCTURE
Output the data in the following hierarchy:
· ## MIRROR_CAPTURE_DETAILS (Date and capture version)
· ## INTRO_CARD (Name, Headline, Location, Connections)
· ## CONTACT_INFO (Profile URL, Email, Website, Birthday)
· ## ABOUT_SECTION (Full text)
· ## EXPERIENCE_SECTION (Company, Title, Dates, Location, Every Bullet)
· ## LICENSES_AND_CERTIFICATIONS (Name, Issuer, ID, Associated Skills)
· ## SKILLS_CATALOG (Categorized as seen on LinkedIn)
· ## HONORS_AND_AWARDS
· ## INTERESTS_AND_GROUPS (Companies, Schools, Groups, Newsletters)

SECTION 3 — THE VACUUM REPORT
At the end of the mirror, provide a "Vacuum Report" list:
1. "status": "captured" or "not_captured" for every major section.
2. "truncation_list": Specific lines where data was hidden by the UI.
3. "hallucination_check": Flag any dates or names that seem inconsistent.

============================================================
EXECUTION: Parse the attached images and generate the Mirror.
============================================================