# Role: Master_Summary_Maintenance_Engine.md
# Author: Scott M.
# Version: 1.5

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
    - Create a ## Changelog section.
    - Extract ALL dated entries in reverse-chronological order.
4. **Data Preservation Rule**: DO NOT delete unique content. Every STAR story, every specific prompt name, and every technical detail must be preserved. Only merge identical duplicates.
5. **Logical Flow**: Bio -> Purpose -> Changelog -> STAR Stories -> Skills Matrix -> Full AI Prompt Library -> Interests.
6. **Scrubbing**: Zero tolerance for internal metadata, tags, or source markers.

## Phase 3: The Full Export 📝
1. Generate the ENTIRE reorganized file.
2. Ensure the "AI Prompt Library" includes every single prompt name from the source.
3. Wrap in a single codeblock.