# Interview Prep: Company Values Intelligence Engine – v1.9.2
- Author: Scott M.
- Logic: Market Friction + WARN Tracking + Jargon Translation + Employee Voice Intelligence + Confidence Penalty Rules
- Last Updated: 2026-06-08

============================================================
CHANGELOG
============================================================
· v1.9.2: Reconciled structural gaps between analytical phases and final report block; enforced hard upper bounds for the confidence score penalty when data is sparse; explicitly mapped competitor contrast and value-aligned story sub-formats into the output template to prevent content drops.
· v1.9.1: Added Retention Risk Signals analysis; generalized employee feedback collection beyond specific review platforms; added confidence reduction requirements when employee feedback is unavailable; improved source resilience across AI platforms.
· v1.9.0: Added Employee Voice Intelligence analysis; added interview process intelligence; added confidence weighting for employee sentiment; prioritized recent employee feedback; expanded final report structure.
· v1.8.6: Fixed output logic by merging Phase 4 and Output Format; flipped order to display the filename block before the main report block; removed literal brackets from the filename template.
· v1.8.5: Added logic to generate the final report in a markdown codeblock for easy saving; updated text to standard sentence case.

============================================================
PURPOSE
============================================================

Help job seekers understand the reality behind company values,
leadership messaging, employee experiences, interview practices,
organizational stability, and hiring priorities.

This analysis is intended to reveal potential alignment,
misalignment, risks, opportunities, and cultural indicators
that may not be obvious from the job description alone.

---

## Step 0: Data Sufficiency (Hard Stop)

If only a company name is provided: stop.

Request:

"I need a job description, company careers page, about page,
or recent news article to ensure sufficient context."

---

## Phase 1: The Cold Reality (Intelligence)

### 1. Leadership DNA
Identify:
- Executive priorities
- Public leadership messaging
- Strategic initiatives
- Recent organizational focus (e.g., Profitability, AI transformation, Operational efficiency, Growth acceleration, Market expansion, Cost reduction)

Determine: "What appears to matter most to leadership right now?"

### 2. Market Pressure (WARN Check)
Analyze:
- WARN notices, layoffs, restructuring activity, hiring freezes, funding concerns, earnings pressure, activist investor pressure, cost-cutting initiatives.

Logic:
If workforce reductions exceed approximately 5%, increase emphasis on: Efficiency, Business value, Execution, Stability, Cost awareness.

### 3. The Jargon Translator
Translate company language into likely operational realities.
Format:
Company Says: "[Value]"
Reality Is: "[Likely day-to-day interpretation]"

---

## Phase 2: Employee Voice Intelligence

Analyze publicly available employee and candidate feedback from employee review sites, discussion forums, interview reports, social media discussions, professional communities, and public employee commentary.

- Prefer feedback from the last 24 months. Older feedback should be labeled: Historical Context.
- Treat employee feedback as directional evidence rather than objective fact. Weight recurring themes significantly higher than isolated complaints. Do not reproduce lengthy copyrighted reviews; summarize recurring patterns only.

### Confidence Reduction & Penalty Rules:
If employee feedback is sparse or unavailable:
- Explicitly state the limitation in the report.
- Reduce confidence scores significantly. Enforce a hard cap: Overall Confidence Score cannot exceed 4/10 if primary sentiment sources are missing or sparse.

---

## Phase 3: Retention Risk Signals

Identify evidence of:
- Leadership churn, executive turnover, frequent reorganizations, high employee turnover, hiring surges/freezes, department consolidations, strategic pivots, morale concerns, or cost-cutting initiatives.

Determine whether patterns suggest: Growth, Stability, Retrenchment, or Transformation.
Classify Retention Risk: Low Risk, Moderate Risk, or High Risk. Explain the reasoning.

---

## Phase 4: Interview Process Intelligence

Analyze publicly available candidate and employee reports.
Identify:
- Common Interview Themes (Technical depth, leadership focus, communication, collaboration, problem solving, business alignment).
- Assessment Patterns (Coding exercises, presentations, panel interviews, behavioral interviews, etc.).
- Candidate Praise & Complaints (Summarize recurring observations).
- Hiring Optimization Analysis: Determine what the organization optimizes for and provide the Top 5 likely evaluation criteria.

---

## Phase 5: Reality Check

### 1. Internal Friction
Identify recurring themes: Technical debt, bureaucracy, slow decision making, micromanagement, resource constraints, communication breakdowns.

### 2. Culture Contrast
Compare against the two most relevant competitors. Identify meaningful differences in culture, leadership, hiring, employee experience, and strategic priorities.

### 3. AI Pivot Score
Assess evidence of AI investment, workforce replacement concerns, AI-driven restructuring, or AI-focused hiring shifts. Classify: High Impact, Medium Impact, or Low Impact.

---

## Phase 6: The Interview Arsenal

### 1. Dealbreaker Traits
Identify three personality profiles most likely to struggle within this environment. Explain why.

### 2. Value-Aligned Stories
Generate interview talking points mapped to the target role.
Format:
[Value] → [Situation] → [Action] → [Result]
Incorporate leadership language, company values, and job description terminology.

### 3. The Value Stress Test
Generate two high-quality reverse interview questions designed to require interviewers to demonstrate how a stated value is actually practiced within the organization.

---

## Phase 7: Savable Output & Format

You must output two separate blocks in this exact order.

------------------------------------------------------------
1. Filename Block
------------------------------------------------------------
Output a markdown codeblock containing only:
Values-CompanyName-Position-YYYYMMDD.md

------------------------------------------------------------
2. Report Block
------------------------------------------------------------
Immediately after, generate the final report wrapped inside its own markdown codeblock.

# COMPANY VALUES INTELLIGENCE REPORT

- Target Company: [Company Name]
- Target Position: [Job Title]
- Analysis Date: [YYYY-MM-DD]

------------------------------------------------------------

Overall Confidence Score: [x/10] (Note: Enforce a hard ceiling of 4/10 if employee feedback data is sparse/unavailable)

### 1. Executive Summary & Market Pressure
- Current macroeconomic standing, earnings pressures, or funding status
- WARN tracking and recent layoff/restructuring activity adjustments

### 2. Leadership DNA & Strategic Direction
- Core executive priorities and current operational focus points

### 3. Employee Voice Intelligence
- Top 3 recurring positive themes
- Top 3 recurring negative themes
- Why employees stay vs. why employees leave
- Current vs. former employee sentiment comparison (Improving, Stable, or Deteriorating)
- Attribute Ratings: Leadership Sentiment [Positive/Mixed/Negative], WLB Sentiment [Positive/Mixed/Negative], Growth Sentiment [Positive/Mixed/Negative], Compensation Sentiment [Positive/Mixed/Negative]
- Sentiment Risk Classification: [Strongly Positive / Mostly Positive / Mixed / Concerning / High Risk]
- Data limitations, source diversity, and recency notes

### 4. Retention Risk Signals
- Turnover indicators, leadership churn, and reorganization activity
- Stability outlook and Risk Rating: [Low Risk / Moderate Risk / High Risk] + Core reasoning

### 5. Interview Process Intelligence
- Common interview themes and assessment patterns
- Candidate praise and complaints summary
- Hiring Optimization: Top 5 core evaluation criteria applied during candidate screening

### 6. Jargon Translator
- Company Says: "[Value]" → Reality Is: "[Likely day-to-day interpretation]"

### 7. Reality Check
- Internal friction, bottlenecks, and technical debt indicators
- Competitor Culture Contrast: Distinct landscape differences vs. the top 2 industry competitors

### 8. AI Pivot Analysis
- AI Pivot Score: [High Impact / Medium Impact / Low Impact]
- Evidence of AI-driven restructuring, investments, or workforce shifting shifts

### 9. Interview Dealbreakers & Value-Aligned Stories
- 3 Dealbreaker personality profiles (Who struggles here and why)
- Value-Aligned Stories parsed exactly as: [Value] → [Situation] → [Action] → [Result]

### 10. The Value Stress Test
- Two high-quality reverse interview questions to validate stated culture

### Final Assessment
- Evaluation: Would a strong candidate likely thrive here?
- Biggest opportunity
- Biggest risk
- Key point to validate during the interview process