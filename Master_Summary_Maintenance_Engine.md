# Role: Master_Summary_Maintenance_Engine.md
# Author: Scott M.
# Version: 1.7

## Phase 1: The Master Audit 📊
Scan the provided markdown file and provide a high-level summary:
1. **Quick Stats**: Word count, total STAR stories, and total count of AI prompts.
2. **Structural Health**: Identify inconsistent headers or broken lists.
3. **Keyword Density**: List the top 5 technical keywords (e.g., PowerShell, EDR, Firewall).
4. **Duplication Detector**: Flag only EXACT overlapping stories or repeat prompts for merging.

## Phase 2: The Reorganization & Governance 🛠️
1. **Author Tag**: "Author: Scott M." at the top.
2. **Purpose Entry**: Add a section explaining this is the "Source of Truth" for resume tailoring and interview prep.
3. **Formal Changelog**: 
    - Create a ## Changelog section if it doesn't exist.
    - Extract ALL dated entries in reverse-chronological order.
    - **MANDATORY**: Add a new entry for today's date: "Master_Summary_Maintenance_Engine ran: Full audit, reorganization, and prompt library reconciliation."
4. **Data Preservation Rule**: DO NOT delete unique content. Every STAR story, every specific prompt name, and every technical detail must be preserved. Only merge identical duplicates.
5. **Logical Flow**: Bio -> Purpose -> Changelog -> STAR Stories -> Skills Matrix -> Full AI Prompt Library -> Interests.
6. **Scrubbing**: Zero tolerance for internal metadata, tags, source markers, or citations (e.g.,).

## Phase 3: The Full Export & Post-Cleanup Report 📝
1. Generate the ENTIRE reorganized file inside a single codeblock.
2. Ensure the "AI Prompt Library" includes every single prompt name from the source.
3. **Post-Cleanup Report**: Immediately following the codeblock, provide a table with the following:
    - **Data Integrity**: Confirmation that 100% of prompts and stories were preserved.
    - **Scrubbing Status**: Confirmation that all metadata/citations were removed.
    - **Efficiency Gains**: Note on what was merged or simplified (e.g., Interests or GRC notes).
    - **Final Stats**: Final word count and total unique prompt count.