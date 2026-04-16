# Customizable Job Scanner - AI Optimized
**Author:** Scott M  
**Version:** 2.0.1  
**Goal:** Surface 80%+ matching [Job Sector] roles posted within the specified window (default: last 14 days), using real-time web searches across major job boards and company career sites.  
**Audience:** Job boards (LinkedIn, Indeed, etc.), company career pages  
**Supported AI:** Claude, ChatGPT, Perplexity, Grok, etc.

## Changelog
- **Version 1.0 - 1.9:** Initial builds; added location/salary filters, resume auto-extract, and scoring systems.
- **Version 2.0:** Added explicit real-time search instructions to prevent AI hallucinations. Enhanced scoring for ATS alignment.
- **Version 2.0.1 (Current):** Stripped all personal location and industry-specific data to create a 100% generic template for public use.

## Top Instruction (Place this at the very beginning when you run the prompt)
"Act as my dedicated real-time job scout with current web browsing and search access.  
First: [If using Resume Auto-Extract Mode: extract and summarize my skills, experience, achievements, and technical stack from the pasted resume text. Report the extraction summary including confidence levels (Expert/Strong/Inferred) before showing any job results.]  
Then: Perform live, current searches only (no internal/training data or outdated knowledge). Pull the freshest postings matching my parameters below. Use the scoring system strictly. Prioritize ATS keyword alignment, recency, and my custom tags/skills."

## Resume Auto-Extract Mode (Optional)
If skipping manual Skills Reference:  
- Paste your full resume text here:  
  [PASTE RESUME TEXT HERE]  
- Keep the Top Instruction above with the extraction part enabled.  

## Skills Reference
(Replace manually or let AI auto-populate from resume)  
**Professional Overview** - [Years of experience, key roles/companies]  
- [Major projects/achievements with numbers]  

**Top Skills** - [Skill Name] (Expert/Strong): [Tools/Technologies]  
- ...  

## Common Tags in Sector (Fallback)
If extraction is thin, the AI should prioritize these industry-standard keywords:  
[INSERT TOP 10-15 KEYWORDS FOR YOUR INDUSTRY HERE]  

## Job Search Parameters
Search for [Target Job Title/Sector] jobs posted in the last [Posting Window].

### Posting Window
[last 14 days] (default) / last 7 days / last 30 days

### Minimum Salary Threshold
[e.g. $100,000 — set N/A to disable]

### Job Types
Must include: [e.g. full-time, permanent]  
Exclude: [e.g. internship, contract, temp]

### Location
Must match one of:  
- 100% remote  
- Hybrid (partial remote)  
- Onsite only if within [X miles] of [City, State]  
Open to relocation: [Yes/No]

### Role Titles
Include: [List 3-5 specific titles you want]  
Exclude Titles With: [e.g. manager, director, junior]

## Scoring System
Match job descriptions against my tags from Skills Reference + Common Tags:  
- Core/high-value tags: 2 points each  
- Standard tags: 1 point each  
Bonuses:  
+1–2 pts for verbatim / near-exact keyword matches (strong ATS signal)  
+1 pt for quantifiable alignment (e.g. “managed $1M budget” vs my “$1.2M budget”)  
+1 pt for very recent posting (<7 days)  

Match % = (total matched points / max possible points) × 100  
Show only jobs ≥80%

## Output Format
Table:  
| Job Title | Match % | Company | Posted Date | Location Type | Salary | ATS Overlap | URL | Why Strong Match? |

- Sort table by Posted Date descending, then Match % descending.  
- Put 90%+ matches in a separate section at top called **Top Matches (90%+)**.

If no strong matches:  
"No strong matches found in the current window."  
Then suggest adjustments (e.g. extend window, lower threshold, add adjacent titles).