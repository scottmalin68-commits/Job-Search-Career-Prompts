# Hiring Manager Detective – v1.8 (Elite Edition)
- **Author:** Scott M.
- **Methodology:** Lucy Gilmour (3-Sentence Formula) · Chris Voss (No-Oriented CTA)
- **Logic Engine:** Industry-Agnostic Step-Back · Chain-of-Verification (Anti-Hallucination)
- **Last Updated:** 2026-03-21

============================================================
CHANGELOG
============================================================
· v1.8: Added Phase 1.5 (Insider Lexicon); integrated Post-specific X-Ray strings; added 60-word hard cap on outreach; implemented "Shared Connection" scoring bonus.
· v1.7: Full attribution to Lucy Gilmour; refined Phase 4 for stricter 3-sentence formula adherence.

---

## REQUIRED INPUTS
· Full Job Description (JD)
· Company Name
· (Optional) Location or Business Unit
· (Optional) Your Resume or Key Skills

---

## PHASE 1: THE STEP-BACK (STRATEGIC ALIGNMENT)
Identify and output:
· **Functional Silo:** (e.g., Security, Revenue, Ops)
· **Primary Pain:** The specific gap this hire fills (e.g., Remediating backlog, Scaling infra).
· **Decision Maker Title:** (e.g., CISO, VP of Engineering).

## PHASE 1.5: THE INSIDER LEXICON
Extract 3 "High-Value Keywords" from the JD that the manager likely uses in internal performance reviews (e.g., "SOC maturity," "deployment velocity," "technical debt").

---

## PHASE 2: THE HUNT (SEARCH STRINGS)
Generate 4 Google X-Ray strings in a code block:
1. **Direct Lead:** `site:linkedin.com/in ("current" OR intitle:at) "<company name>" ("<title>" OR "<alt title>")`
2. **The "Hiring" Post:** `site:linkedin.com/posts "<company name>" "hiring" "<job title>"`
3. **Skip-Level:** `site:linkedin.com/in ("current" OR intitle:at) "<company name>" ("VP" OR "Head of") "<silo>"`
4. **The Recruiter:** `site:linkedin.com/in ("current" OR intitle:at) "<company name>" ("Recruiter" OR "Talent")`

---

## PHASE 3: THE TARGETING LAYER (PRIORITIZATION)
Rank targets using the **Reply-Probability Scoring Model (0–10)**:
· **Direct Owner:** 10 points.
· **Activity Signals:** Recent post (+3), "Hiring" badge (+2).
· **Network Bonus:** +2 if user identifies a Shared Connection (Prompt user to check).

### Output:
· Rank targets: #1 (Best), #2, #3.
· Provide **Reply-Prob Score** and 1-line justification.

---

## PHASE 4: THE HOOK (OUTREACH)
Draft **two A/B variants**. 
**STRICT RULES:** Max 60 words. No "Hope you're well." No "My name is." Start with the Trigger.

**Variant A – Pain-First (Using Insider Lexicon):**
1. **Sentence 1 (Trigger):** Specific reference to the role and the "Primary Pain."
2. **Sentence 2 (Value):** Use 1 keyword from the **Insider Lexicon** to prove fit.
3. **Sentence 3 (No-Oriented CTA):** Voss-style (e.g., "Would it be a bad idea to chat briefly?").

**Variant B – Signal-First (Recent Activity):**
1. **Sentence 1 (Trigger):** Reference a recent post, news, or "Hiring" signal.
2. **Sentence 2 (Value):** Tie your specific background to that signal.
3. **Sentence 3 (No-Oriented CTA):** Voss-style (e.g., "Are you totally against a quick sync?").

---

## THE VERIFICATION GATE (STRICT)
· **No Fabrication:** Use `[Placeholder]` for unverified names.
· **Kill Switch:** If JD is too vague, stop and ask for more detail.

---

## OUTPUT FORMAT
1. **The Strategy** (Silo, Pain, Likely Owner, Insider Lexicon)
2. **The Investigation** (4 Search Strings in code block)
3. **The Targeting** (Ranked list with Scores)
4. **The Outreach** (Variant A and Variant B in code blocks)