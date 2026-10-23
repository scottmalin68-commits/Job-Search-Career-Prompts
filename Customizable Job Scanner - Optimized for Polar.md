# Job Scanner - Unattended Run (Polar)

**Author:** Scott Malin, CISSP  
**Version:** 3.0 (adapted from v2.0.3)  
**Goal:** Surface 80%+ matching roles posted within the specified window, using live browsing of job boards and company career pages, with no user present.

## Changelog

- **Version 3.0:** Rewritten for unattended runs in Polar. Added decision rules, seen-jobs memory, score worksheet, run log, and draft-only delivery. Removed jailbreak, gibberish and state-decay guardrails.
- **Version 2.0.3:** Added LLM adaptation note.
- **Version 2.0.2:** Added anti-drift locks and edge case handling.
- **Version 2.0.1:** Stripped personal data to make a generic template.
- **Version 2.0:** Added real-time search instructions and ATS scoring.

## Mission

Find roles that match my profile at 80%+ and were posted within the window below. Use the live browser to open real postings. Never rely on memory or training data for any job detail.

This runs with no user present. **Never ask questions.** Follow the decision rules below and keep going.

## Inputs (Fill In Before Scheduling)

### Posting Window

Last <<14>> days. Today's date is the run date.

### Target Roles

- **Include titles:** <<Title 1>>, <<Title 2>>, <<Title 3>>, <<Title 4>>
- **Exclude titles containing:** <<manager, director, junior, intern>>

### Filters

- **Minimum salary:** <<$100,000 or N/A>>
- **Job types:** include <<full-time, permanent>>; exclude <<internship, contract, temp>>
- **Location:** 100% remote, or hybrid, or onsite only within <<X>> miles of <<City, State>>
- **Open to relocation:** <<Yes/No>>

### Profile (Locked, Do Not Re-Extract)

- **Professional overview:** <<years of experience, key roles/companies>>
- **Achievements:** <<project with numbers>>; <<project with numbers>>
- **Core tags (2 pts each):** <<tag, tag, tag, ...>>
- **Standard tags (1 pt each):** <<tag, tag, tag, ...>>

### Sources (In This Order)

1. LinkedIn Jobs (use my signed-in session)
2. Indeed
3. <<Dice / other board>>
4. Career pages for: <<Company 1, Company 2, Company 3, ...>>

## Procedure

1. Read `seen_jobs.csv` (columns: URL, title, company, date first reported). Create it if missing. Skip any posting whose URL or company+title is already listed.
2. For each source, search each target title with the filters applied. Review up to <<25>> postings per source, and spend at most <<15>> minutes per source.
3. Open each candidate posting. Confirm it is live, and record the posted date, location type, salary, and full description. Only report postings you opened.
4. Drop it if it fails any filter (title exclusion, job type, location, salary below floor, outside window).
5. Score it using the formula below. Save the points breakdown for every scored posting to `score_worksheet.csv`.
6. Dedupe reposts across boards by company + title. Keep the earliest posted date and the best URL.
7. Keep postings scoring 80% or higher, and add them to `seen_jobs.csv`.
8. Build the output and deliver it as described below.

## Scoring System (Strict Math)

- **Core tag found in description:** 2 points each
- **Standard tag found in description:** 1 point each

**Bonuses:**

- +1 to +2 for verbatim or near-exact keyword matches (ATS signal)
- +1 for quantifiable alignment
- +1 for a posting under 7 days old

**Math:**

- Max possible points = (2 x number of core tags) + (1 x number of standard tags) + 2 + 1 + 1
- Match % = total points / max possible points x 100, rounded to a whole number
- Compute in a script or spreadsheet when possible. Do not do the arithmetic mentally.

## Decision Rules (Never Ask, Always Decide)

- **CAPTCHA, login wall, or block:** skip that source, log it, continue.
- **Page fails or times out:** retry once, then skip the posting or source and log it.
- **Salary not listed:** keep the role, show "Not listed," no score penalty.
- **Posted date unclear or "reposted":** mark the date "Unverified." Include only if the score is 85% or higher.
- **Location type unclear:** include with a "Verify location" flag.
- **Already in `seen_jobs.csv`:** skip silently.
- **Anything unexpected:** choose the most conservative option (skip and log) and continue.
- **Never** apply to jobs, send messages, submit forms, or change account settings.

## Output Format

### Section 1: Matches

Show **Top Matches (90%+)** first, then **Strong Matches (80-89%)**, using this table:

| Job Title | Match % | Company | Posted Date | Location Type | Salary | ATS Overlap | URL | Why Strong Match? |
|---|---|---|---|---|---|---|---|---|

Sort by Posted Date descending, then Match % descending.

If nothing scores 80%+, write: "No strong matches found in the current window." Then list the 5 closest near-misses in the same table format, and suggest one or two parameter changes.

### Section 2: Run Log

- Sources checked and the result of each (OK / skipped, with the reason)
- Postings reviewed, dropped (with the top reasons), and reported
- Flags needing my attention (Verify location, Unverified date, blocked sources)

A short summary line above the tables is fine.

## Delivery

- Save the report as `job_scan_<<YYYY-MM-DD>>.md`.
- Create a Gmail draft to myself with the tables and run log. **Do not send it.**
- Update `seen_jobs.csv` last, only after the report is saved.

## Success Criteria

The run succeeded if the report and draft exist, every listed URL was opened and verified, and the run log is complete. If every source failed, still produce the report, with the run log explaining why.
