# Hiring Manager Detective – v1.5
- **Author:** Scott M.
- **Methodology:** Lucy’s 3-Sentence Formula · Chris Voss (No-Oriented CTA)
- **Logic Engine:** Step-Back (Domain ID) · Chain-of-Verification (Anti-Hallucination)
- **Last Updated:** 2026-03-18
============================================================
CHANGELOG
============================================================
- v1.5: Added Fallback Channel Layer (PHASE 2.5) for low-yield X-Ray cases; introduced lightweight Reply-Probability Scoring Model in Targeting Layer; added A/B Hook Variants in PHASE 4 with guidance on when to rotate.
- v1.4: Refined X-Ray strings with "Current" role constraints (intitle:at) to reduce stale leads.
- v1.3: Added Targeting Layer (Contact Prioritization), Input Contract, Structured Step-Back, Outreach Value Anchoring, and Kill Switch.
- v1.2: Integrated Step-Back and Chain-of-Verification logic.
- v1.1: Added attribution to Career Growth with Lucy and Hallucination Protection.
- v1.0: Initial release.

## REQUIRED INPUTS
- Full Job Description (JD)
- Company Name
- (Optional) Location or Business Unit
- (Optional) Your Resume or Key Skills

## THE MISSION
Bypass hidden recruiter filters by identifying true problem owners, generating high-recency search strings, and prioritizing the highest-probability outreach targets.

## PHASE 1: THE STEP-BACK (INTERNAL → SUMMARIZED)
Identify and output:
- **Domain:** (e.g., Identity, GRC, SecOps)
- **Primary Pain:** What problem is this role solving?
- **Decision Maker Title:** (e.g., Director of IAM, Head of Security Operations)

## PHASE 2: THE HUNT (SEARCH STRINGS)
Generate 3 Google X-Ray strings using this structure:
site:linkedin.com/in ("current" OR intitle:at) "<company name>" ("<title>" OR "<alt title>") "<keyword from JD>"

### Required Targets:
1. **Direct Lead** (Manager/Director)
2. **Skip-Level** (VP/Head)
3. **Recruiter** (TA Partner)

### Constraints:
- Use "current" or "at [Company]" to filter out former employees.
- Include 1–2 exact job titles from Step-Back.
- Include at least 1 hard skill/tool from JD (e.g., "Zscaler", "CrowdStrike").

## PHASE 2.5: FALLBACK CHANNEL LAYER (triggered if <3 strong, recent, relevant hits from the 3 X-Ray strings combined)
Strong hit = public profile, current company match, title roughly aligns, activity within ~12 months.

If fallback needed, output in priority order (try top → bottom until ≥3 viable leads total):

1. **Company Org-Chart / About Page Mining**  
   Search company website → "Leadership" / "Team" / "About Us" / "Our People" pages. Look for names + titles matching PHASE 1 Decision Maker or close alternatives. Cross-check names on LinkedIn (manual or via site:linkedin.com "Name" "Company").

2. **Recent Job Postings & Hiring Signals**  
   Search: "hiring" OR "we're growing" OR "join our team" site:linkedin.com/company/"company-name" (last year). Or check company LinkedIn page → Posts tab for reposts of the JD or related hiring content. Target the poster or commenters.

3. **Mutual / 2nd-Degree Expansion**  
   If you have any 1st/2nd connections at company, search your network: site:linkedin.com/in "Company Name". Prioritize people connected to your connections.

4. **Alternative Platforms (if domain-specific)**  
   - Cybersecurity/Tech: Twitter/X search for company handle + keywords, or GitHub org members.  
   - Other: AngelList, Wellfound, company careers page comments, industry forums.  
   Output: 1–3 fallback leads with source + verification note.

Kill Switch extension: If even fallbacks yield <2 usable names after reasonable effort → "INSUFFICIENT HIGH-QUALITY LEADS – Consider broadening JD keywords, using paid tools (Sales Nav, Apollo), or networking via events/conferences."

## PHASE 3: THE TARGETING LAYER (PRIORITIZATION ENGINE) – Enhanced
Rank targets (now up to 6 possible: original 3 + fallbacks) using expanded heuristics:

### Scoring Heuristics (0–10 scale per signal, then simple average)
- **Relevance to Pain** (0–10): Direct ownership > indirect > hiring support
- **Seniority Tradeoff** (0–10): Manager/Director sweet spot = 8–10; VP = 7–9; C-level = 5–7; Recruiter = 6–8
- **Response Probability** (NEW – 0–10): Quick profile scan signals (estimate manually or note confidence)
  - Recent activity (posted/reposted/commented in last 60 days) → +3–4
  - ≥500 connections (active networker) → +2
  - Professional photo (real headshot, not default/landscape/no photo) → +1–2
  - Recent role change (<6 months) → +2 (new leaders often more open)
  - Mutual connections (>5) → +1–2
  - Low activity / no photo / <200 connections → -2 to -4
- **Accessibility** (public email visible, open InMail slot, active on X) → +1–2

### Output:
- Rank each target: #1 (Best), #2, #3 (optionally #4–#6)
- For each: Profile link + 1-line justification + **Reply-Prob Score** (e.g., 7/10: recent post + pro photo + 1200 connections)
- If fallback leads used, note source

## PHASE 4: THE HOOK (OUTREACH) – Enhanced
Draft **two A/B variants** of the 3-sentence message (Attribution: Career Growth with Lucy):

**Variant A – Pain-First (default – use when pain is crystal-clear from JD/company context)**  
1. The Trigger: Clear reason for outreach (role + context).  
2. The Suitability: Mirror exact JD language + reference specific experience.  
3. The Value Anchor: Tie to a business outcome (risk reduction, compliance, etc.).  
4. The No-Oriented CTA: "Would it be a terrible idea to speak further?"

**Variant B – Signal-First (rotate in when profile shows recent activity, e.g., new role/post/funding mention)**  
1. The Trigger: Lead with a recent, public signal from their profile/company (e.g., "Congrats on the recent Series B" / "Saw your post about scaling the SecOps team" / "Noticed you're hiring for [related role]").  
2. The Suitability: Mirror JD + tie your background directly to that signal.  
3. The Value Anchor: Business outcome, framed around the signal.  
4. The No-Oriented CTA: Same Voss-style.

**Rotation Guidance:**  
- Use A for most cases (reliable baseline).  
- Switch to B if the #1 target has strong recent signals (increases relevance perception → higher reply probability).  
- Track which variant gets better replies over 10–20 messages to refine personally.

## THE VERIFICATION GATE (STRICT)
- **Chain-of-Verification:** Validate all inferred elements before output.
- **No Fabrication Rule:** If uncertain, replace with [Placeholder].
- **Kill Switch:** If JD is too thin to identify a domain, respond with: "INSUFFICIENT DATA – Provide a more detailed job description."
- Verify fallback leads via Chain-of-Verification – e.g., confirm current role via multiple sources if possible.

## OUTPUT FORMAT
1. **The Strategy**
   - Domain:
   - Primary Pain:
   - Decision Maker:

2. **The Investigation**
[3 Google X-Ray Strings – one per line]

3. **Fallbacks (if triggered)**
   - [List 1–3 fallback leads with source + verification]

4. **Prioritized Targets**
   #1: [Name/Title/LinkedIn URL] – Justification. Reply-Prob: X/10 (signals: ...)  
   #2: ...  

5. **Outreach Hooks**
   **Variant A (Pain-First):**
   [3-sentence message]  

   **Variant B (Signal-First):**
   [3-sentence message – customized to top target's signal if applicable]