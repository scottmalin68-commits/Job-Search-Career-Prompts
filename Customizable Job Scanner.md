# Customizable Job Scanner - AI optimized
**Author:** Scott M
**Version:** 1.9 (see Changelog below)
**Goal:** Find 80%+ matching [job sector] roles posted within the specified window (default: last 14 days)
**Audience:** Job boards, company sites
**Supported AI:** Claude, ChatGPT, Perplexity, Grok, etc.

## Changelog
- **Version 1.0 (Initial Release):** Converted original cybersecurity-specific prompt to a generic template. Added placeholders for sector, skills, companies, etc. Removed Dropbox file fetch.
- **Version 1.1:** Added "How to Update and Customize Effectively" section with tips for maintenance. Introduced Changelog section for tracking changes. Added Version field in header.
- **Version 1.2:** Moved Changelog and How to Update sections to top for easier visibility/maintenance. Minor header cleanup.
- **Version 1.3:** Added "Job Types" subsection to filter full-time/part-time/internship. Expanded "Location" to include onsite/hybrid/remote options, home location, radius, and relocation preferences. Updated tips to cover these new customizations.
- **Version 1.4:** Added "Posting Window" parameter for flexible search recency (e.g., last 7/14/30 days). Updated goal header and tips to reference it.
- **Version 1.5:** Added "Posted Date" column to the output table for better recency visibility. Updated Output format and tips accordingly.
- **Version 1.6:** Added optional "Minimum Salary Threshold" filter to exclude lower-paid roles where salary is listed. Updated Output format notes and tips for salary handling.
- **Version 1.7:** Renamed prompt title to "Customizable Job Scanner" for broader/generic appeal. No other functional changes.
- **Version 1.8:** Added optional "Resume Auto-Extract Mode" at top for lazy/fast setup. AI extracts skills/experience from provided resume text. Updated tips on usage.
- **Version 1.9 (Current):** 
  - Added optional "If no matches, suggest adjustments" instruction at end.
  - Added "Common Tags in Sector" fallback list for thin extraction.
  - Made output table optionally sortable by Posted Date descending.
  - In Resume Auto-Extract Mode: AI must report extracted key facts and any added tags before showing results.

## Resume Auto-Extract Mode (Optional - For Lazy/Fast Setup)
If you want to skip manually filling the Skills Reference section:
- Paste your full resume text (plain text, markdown, or key sections) here:  
  [PASTE RESUME TEXT HERE]
- Then add this instruction at the very top of your prompt when running:  
  "First, extract and summarize my skills, experience, achievements, and technical stack from the pasted resume text above. Populate the Skills Reference section automatically before proceeding with the job search. Report what you extracted and any tags you suggested/added."

The AI will:
- Pull professional overview, years/experience, major projects/quantifiable wins.
- Identify top skills (with proficiency levels if mentioned), tools/technologies.
- Build a technical stack list.
- Suggest or auto-map relevant tags for scoring.
- **Before showing job results**, output a summary like:  
  "Resume Extraction Summary:  
  - Experience: 30 years in IT/security at Aetna/CVS  
  - Key achievements: Led CrowdStrike migration (120K endpoints), BeyondTrust PAM for 2500 devs, 40% vuln reduction via Tanium  
  - Top skills mapped: Zero Trust (Expert), CrowdStrike (Expert), PowerShell (Expert), ...  
  - Added tags from resume/sector common: Splunk, SIEM, KQL  
  Proceeding with search using these."

Use this if you're short on time; manual editing is still better for precision.

## How to Update and Customize Effectively
To keep this prompt effective for different job sectors or as your skills evolve, follow these tips:
- **Use Resume Auto-Extract Mode** when you're feeling lazy: Paste resume → add the extraction instruction → run. The AI will report what it pulled/mapped so you can verify or tweak before results appear.
- **Update Skills Reference (Manual or Post-Extraction):** Replace placeholders or refine AI-extracted content. Be specific with quantifiable achievements to help matching. Refresh every 3-6 months or after big projects.
- **Customize Tags and Scoring:** List 15-25 key tags that represent your strongest, most unique skills. Prioritize core tags (2 points) for must-have expertise. Use the "Common Tags in Sector" fallback if extraction is thin.
- **Refine Job Parameters:** 
  - Set **Posting Window** to control freshness: "last 7 days" for daily checks, "last 14 days" (default), "last 30 days" when starting.
  - Use **Minimum Salary Threshold** (e.g., "$130,000") to filter listed salaries. Set to "N/A" to disable.
  - Add/remove companies based on your network or industry news.
  - Customize location with your actual home base (e.g., East Hartford, CT), radius, and relocation prefs.
- **Test with AI Models:** Run in multiple AIs and compare. If too few matches, lower threshold or extend window.
- **Iterate Based on Results:** Note mismatches, tweak tags/weights. Review Posted Date/Salary columns and extraction summary (if used). Track changes in Changelog.
- **Best Practices:** Keep prompt concise. Use exact job-posting phrases in tags. For new sectors, research keywords via LinkedIn/Indeed. Provide clean resume text for best extraction.

## Skills Reference
(Replace or expand manually — or let AI auto-populate from resume extract above)

**Professional Overview**
- [Your years of experience and key roles/companies]
- [Major achievements or projects, e.g., led migrations, reduced risks by X%, managed large environments]

**Top Skills**
- [Skill 1 (Expert/Strong)]: [tools/technologies]
- [Skill 2 (Expert/Strong)]: [tools/technologies]
- etc.

**Technical Stack**
- [Category]: [tools/examples]
- etc.

## Common Tags in Sector (Fallback Reference)
If resume extraction yields few tags or Skills Reference is thin, reference these common ones for the sector and add relevant matches as 1-point tags (unless clearly core):
[Cybersecurity example:] `Splunk`, `SIEM`, `SIEM`, `KQL`, `Sentinel`, `Azure Security`, `AWS Security`, `Threat Hunting`, `Vulnerability Scanning`, `Penetration Testing`, `Compliance`, `ISO 27001`, `PCI DSS`, `Firewall`, `IDS/IPS`, `SOC`, `Threat Intelligence`
[Other sectors — add your own list here when changing sector, e.g., for DevOps: `Kubernetes`, `Docker`, `Terraform`, `CI/CD`, `Jenkins`, `Git`, `AWS`, `Azure DevOps`]

## Job Search Parameters
Search for [job sector] jobs posted in the last [Posting Window, e.g., 14 days / 7 days / 30 days / specify custom timeframe].

### Posting Window
[Specify recency here, e.g., "14 days" (default), "7 days" for fresh-only, "30 days" when starting a search, or "since YYYY-MM-DD"]

### Minimum Salary Threshold
[Optional: e.g., "$130,000" or "$120K" to exclude lower listed salaries; set to "N/A" or blank to include all. Only filters jobs with explicit salary listed in posting.]

### Priority Companies (check career pages directly)
- [Company 1] ([career page URL])  # Choose companies relevant to the sector
- [Company 2] ([career page URL])
- [Add more as needed]

### Additional sources
LinkedIn, Indeed, ZipRecruiter, Glassdoor, Dice, Monster, SimplyHired, company career sites

### Job Types
Must include: [e.g., full-time, permanent]
Exclude: [e.g., part-time, internship, contract, temp, consulting, contractor, consultant, C2H]

### Location
Must match one of these work models:
- 100% remote
- Hybrid (partial remote)
- Onsite, but only if within [X miles, e.g., 50 miles] of [your home location, e.g., East Hartford, CT] (includes nearby areas like Bloomfield, Windsor, Newington, Farmington)
- Open to relocation: [Yes/No; if yes, specify preferences, e.g., "anywhere in US" or "Northeast US only"]

### Role types to include
[List relevant titles, e.g., Security Engineer, Senior Security Engineer, Security Analyst, Cybersecurity Engineer, Information Security Engineer, InfoSec Analyst]

### Exclude anything with these terms
manager, director, head of, principal, lead  # (Already excludes contracts via Job Types)

## Scoring system
Match job descriptions against these key tags (customize this list to the sector):
`[Tag1]`, `[Tag2]`, `[Tag3]`, etc.  

Core/high-value skills worth 2 points: `[Core tag 1]`, `[Core tag 2]`, etc.  

Everything else: 1 point

Calculate: matched points ÷ total possible points  
Show only 80%+ matches

## Output format
Table with: Job Title | Match % | Company | Posted Date | Salary | URL

- **Posted Date:** Pull exact posted date if available (e.g., "2026-01-10" or "Posted Jan 10, 2026"). If approximate/not listed: "Approx. X days ago" or "N/A" — no guessing.
- **Salary:** Only show if explicitly listed (e.g., "$140,000 - $170,000"); "N/A" otherwise — no guessing/estimating/averages. If Minimum Salary Threshold set, exclude jobs below it.
- **Optional Sorting:** If there are matches, sort the table by Posted Date descending (most recent first) unless user specifies otherwise.

Remove duplicates (same title + company)

Put 90%+ matches in separate section at top called "Top Matches (90%+)"

If nothing found just say: "No strong matches found this week."  
Then suggest adjustments, e.g.:  
- "Try extending Posting Window to 30 days?"  
- "Lower threshold to 75%?"  
- "Add common sector tags like Splunk/SIEM if not already included?"  
- "Broaden location to include more hybrid options?"  
- "Check priority company career pages manually for unindexed roles?"
