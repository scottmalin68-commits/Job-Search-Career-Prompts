# TITLE: Network Intelligence Engine
# VERSION: 2.0
# AUTHOR: Scott M.
# LAST UPDATED: 2026-03-22

# CHANGELOG:
- v2.0:
  - Added Contact Scoring System (Warm / Cold / High-Value)
  - Added Outreach Prioritization Layer
  - Added Auto-Message Drafting Engine
  - Added Strategic Network Insights
- v1.0:
  - Initial Contact Intelligence Auditor (gap analysis + enrichment)

# PURPOSE:
Transform a raw list of professional contacts into a structured, prioritized, and actionable networking system. This includes identifying data gaps, enriching records, scoring relationship value, prioritizing outreach, and generating ready-to-send messages.

---

## INPUT:
A list of professional contacts with partial or complete information.

---

## TASK:

### STEP 1: CONTACT SCHEMA
Assume an ideal contact record includes:
- Full Name
- Current Role/Title
- Company
- Location
- Email
- LinkedIn URL
- Relationship Context
- Last Interaction Date
- Notes (influence, relevance, context)

---

### STEP 2: GAP ANALYSIS
For EACH contact:
- Identify missing fields
- Identify weak fields (outdated, vague, incomplete)

---

### STEP 3: DATA QUALITY FLAGS
Flag:
- Outdated roles/companies
- No clear relationship context
- Missing contact method (email or LinkedIn)
- Low strategic value (unclear relevance)

---

### STEP 4: ENRICHMENT PLAN
For EACH gap:
Suggest how to fill it:
- LinkedIn lookup
- Company website
- Email pattern tools
- Internal notes/email history
- Mutual connections

---

### STEP 5: CONTACT SCORING

Score EACH contact across 3 dimensions (1–5 scale):

**1. Relationship Strength**
- 1 = No real relationship
- 3 = Weak familiarity
- 5 = Strong relationship / direct rapport

**2. Strategic Value**
- 1 = Low relevance
- 3 = Some relevance
- 5 = Direct alignment (hiring manager, target team, etc.)

**3. Accessibility**
- 1 = No contact method
- 3 = Indirect (LinkedIn only)
- 5 = Direct (email / active communication)

---

### STEP 6: CONTACT CLASSIFICATION

Based on scores, assign:

- **High-Value / Warm**
- **High-Value / Cold**
- **Low-Value / Warm**
- **Low-Value / Cold**

---

### STEP 7: OUTREACH PRIORITIZATION

Create a ranked list:

**Priority 1:**
- High-Value / Warm

**Priority 2:**
- High-Value / Cold

**Priority 3:**
- Low-Value / Warm

**Priority 4:**
- Low-Value / Cold

---

### STEP 8: AUTO-MESSAGE GENERATION

For top priority contacts, generate tailored outreach:

#### Message Type Rules:
- Warm → casual, relationship-based
- Cold → concise, value-driven

#### Output:
- Subject line (if email)
- Message body
- Tone: professional, direct, low-friction

---

## OUTPUT FORMAT:

### CONTACT BREAKDOWN

#### Contact: [Name]

**Current Data:**
- Role:
- Company:
- Email:
- LinkedIn:
- Notes:

**Missing / Weak Fields:**
- [List]

**Data Quality Flags:**
- [List]

**Enrichment Actions:**
- [Steps]

**Scores:**
- Relationship Strength:
- Strategic Value:
- Accessibility:

**Classification:**
- [Category]

---

### PRIORITIZED OUTREACH LIST

1. [Name] — [Classification]
2. [Name] — [Classification]
3. ...

---

### OUTREACH MESSAGES

#### Contact: [Name]
**Subject:**
[Text]

**Message:**
[Text]

---

### FINAL SUMMARY

**Network Health Score (1–10):**
[Assessment]

**Top Gaps Across Dataset:**
- [Patterns]

**Biggest Leverage Opportunities:**
- [Insights]

**Execution Plan:**
- Step 1:
- Step 2:
- Step 3: