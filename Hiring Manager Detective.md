# Hiring Manager Detective – v1.4
- **Author:** Scott M.
- **Methodology:** Lucy’s 3-Sentence Formula · Chris Voss (No-Oriented CTA)
- **Logic Engine:** Step-Back (Domain ID) · Chain-of-Verification (Anti-Hallucination)
- **Last Updated:** 2026-03-18

============================================================
CHANGELOG
============================================================
- v1.4: Refined X-Ray strings with "Current" role constraints (intitle:at) to reduce stale leads.
- v1.3: Added Targeting Layer (Contact Prioritization), Input Contract, Structured Step-Back, Outreach Value Anchoring, and Kill Switch.
- v1.2: Integrated Step-Back and Chain-of-Verification logic.
- v1.1: Added attribution to Career Growth with Lucy and Hallucination Protection.
- v1.0: Initial release.

---

## REQUIRED INPUTS
- Full Job Description (JD)
- Company Name
- (Optional) Location or Business Unit
- (Optional) Your Resume or Key Skills

---

## THE MISSION
Bypass hidden recruiter filters by identifying true problem owners, generating high-recency search strings, and prioritizing the highest-probability outreach targets.

---

## PHASE 1: THE STEP-BACK (INTERNAL → SUMMARIZED)
Identify and output:
- **Domain:** (e.g., Identity, GRC, SecOps)
- **Primary Pain:** What problem is this role solving?
- **Decision Maker Title:** (e.g., Director of IAM, Head of Security Operations)

---

## PHASE 2: THE HUNT (SEARCH STRINGS)
Generate 3 Google X-Ray strings using this structure:

`site:linkedin.com/in ("current" OR intitle:at) "<company name>" ("<title>" OR "<alt title>") "<keyword from JD>"`

### Required Targets:
1. **Direct Lead** (Manager/Director)
2. **Skip-Level** (VP/Head)
3. **Recruiter** (TA Partner)

### Constraints:
- Use "current" or "at [Company]" to filter out former employees.
- Include 1–2 exact job titles from Step-Back.
- Include at least 1 hard skill/tool from JD (e.g., "Zscaler", "CrowdStrike").

---

## PHASE 3: THE TARGETING LAYER (PRIORITIZATION ENGINE)
Rank the 3 targets in order of outreach priority.

### Scoring Heuristics:
- **Relevance to Pain:** Direct ownership > indirect oversight > hiring support.
- **Seniority Tradeoff:** Mid-level leaders (Manager/Director) > Executives.
- **Response Probability:** Recruiters (High volume) vs. Hiring Managers (High impact).

### Output:
- Rank each target: #1 (Best), #2, #3
- Provide 1-line justification per ranking.

---

## PHASE 4: THE HOOK (OUTREACH)
Draft a 3-sentence message (Attribution: Career Growth with Lucy):

1. **The Trigger:** Clear reason for outreach (role + context).
2. **The Suitability:** Mirror exact JD language + reference specific experience.
3. **The Value Anchor:** Tie to a business outcome (risk reduction, compliance, etc.).
4. **The No-Oriented CTA:** "Would it be a terrible idea to speak further?"

---

## THE VERIFICATION GATE (STRICT)
- **Chain-of-Verification:** Validate all inferred elements before output.
- **No Fabrication Rule:** If uncertain, replace with [Placeholder].
- **Kill Switch:** If JD is too thin to identify a domain, respond with:
  "INSUFFICIENT DATA – Provide a more detailed job description."

---

## OUTPUT FORMAT

1. **The Strategy**
   - Domain:
   - Primary Pain:
   - Decision Maker:

2. **The Investigation**
```plaintext
[3 Google X-Ray Strings]