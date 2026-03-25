# TITLE: Network Contacts Intelligence Engine
# VERSION: 2.1
# AUTHOR: Scott M.
# LAST UPDATED: 2026-03-22

# CHANGELOG:
- v2.1:
  - Added Reference Tracking (Professional vs. Personal)
  - Added "Vouch Level" scoring dimension
  - Integrated "Reference Readiness" into classification
  - Updated Auto-Message rules for reference requests
- v2.0:
  - Added Contact Scoring System (Warm / Cold / High-Value)
  - Added Outreach Prioritization Layer
  - Added Auto-Message Drafting Engine
  - Added Strategic Network Insights
- v1.0:
  - Initial Contact Intelligence Auditor (gap analysis + enrichment)

# PURPOSE:
Transform a raw list of contacts into a structured, prioritized, and actionable networking system, specifically identifying and qualifying professional and personal references.

---

## INPUT:
A list of contacts with partial or complete information.

---

## TASK:

### STEP 1: CONTACT SCHEMA
Assume an ideal contact record includes:
- Full Name
- Current Role/Title
- Company
- Location
- Email / LinkedIn URL
- Relationship Context (How you met / worked together)
- Reference Type: (Professional / Personal / N/A)
- Last Interaction Date
- Notes (Influence, relevance, context)

---

### STEP 2: GAP ANALYSIS & QUALITY FLAGS
For EACH contact, identify missing fields and flag:
- Outdated roles/companies
- No clear relationship context
- Missing contact method
- Reference Gap: (If marked as a reference but no "Vouch Level" or recent interaction)

---

### STEP 3: CONTACT SCORING (1–5 scale)

**1. Relationship Strength**
- 1 = No real relationship / 5 = Strong direct rapport

**2. Strategic Value**
- 1 = Low relevance / 5 = Direct alignment (hiring manager, target team)

**3. Vouch Level (Reference Potential)**
- 1 = Unknown / Unreliable
- 3 = Willing to provide a standard reference
- 5 = Enthusiastic "Champion" (will go above and beyond)

---

### STEP 4: CONTACT CLASSIFICATION

Based on scores, assign:
- **Tier 1 Reference:** High Strength + High Vouch (Professional)
- **Character Reference:** High Strength + High Vouch (Personal)
- **High-Value Lead:** High Strategic Value (Warm or Cold)
- **Standard Network:** Moderate scores across the board

---

### STEP 5: OUTREACH PRIORITIZATION

1. **Priority 1:** Tier 1 References (Verify current info & availability)
2. **Priority 2:** High-Value / Warm Leads
3. **Priority 3:** Character References
4. **Priority 4:** High-Value / Cold Leads

---

### STEP 6: AUTO-MESSAGE GENERATION

Generate tailored outreach based on classification:

#### Message Type Rules:
- **Reference Request:** Clear, appreciative, and provides an "out" (low-pressure).
- **Warm Lead:** Casual, relationship-based.
- **Cold Lead:** Concise, value-driven.

#### Output:
- Subject line
- Message body
- Tone: Professional, direct, low-friction.

---

## OUTPUT FORMAT:

### CONTACT BREAKDOWN
#### Contact: [Name]
- **Category:** [Tier 1 Ref / Character Ref / Lead]
- **Current Data:** [Summary]
- **Gaps/Flags:** [List]
- **Scores:** [Rel: X, Strat: X, Vouch: X]
- **Action:** [Enrichment steps]

---

### PRIORITIZED OUTREACH LIST
1. [Name] — [Classification] — [Reason]
2. [Name] — [Classification] — [Reason]

---

### OUTREACH MESSAGES
#### Contact: [Name] (Reference Request / Lead)
**Subject:** [Text]
**Message:** [Text]

---

### FINAL SUMMARY
**Network Health Score (1–10):** [Assessment]
**Reference Strength:** [Total count of Tier 1 vs Character refs]
**Execution Plan:** [Next 3 steps]