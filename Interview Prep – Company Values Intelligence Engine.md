# Interview Prep: Company Values Intelligence Engine – v1.9.1
- Author: Scott M.
- Logic: Market Friction + WARN Tracking + Jargon Translation + Employee Voice Intelligence
- Last Updated: 2026-06-08

============================================================
CHANGELOG
============================================================
· v1.9.1: Added Retention Risk Signals analysis; generalized employee feedback collection beyond specific review platforms; added confidence reduction requirements when employee feedback is unavailable; improved source resilience across AI platforms.
· v1.9.0: Added Employee Voice Intelligence analysis; added interview process intelligence; added confidence weighting for employee sentiment; prioritized recent employee feedback; expanded final report structure.
· v1.8.7: Added a standardized report header format inside the final report block; bumped version.
· v1.8.6: Fixed output logic by merging Phase 4 and Output Format; flipped order to display the filename block before the main report block; removed literal brackets from the filename template.
· v1.8.5: Added logic to generate the final report in a markdown codeblock for easy saving; updated text to standard sentence case.
· v1.8.1: Added Step 4 for savable output in specific filename format within a codeblock.
· v1.8: Integrated WARN tracker & market pressure (layoffs/funding); added "glassdoor reality gap" (reddit/cached sentiment); added "ai pivot" impact score.
· v1.7: Added leadership dna; proof-of-value reverse questions.

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
- Recent organizational focus

Examples:

- Profitability
- AI transformation
- Operational efficiency
- Growth acceleration
- Market expansion
- Cost reduction

Determine:

"What appears to matter most to leadership right now?"

---

### 2. Market Pressure (WARN Check)

Analyze:

- WARN notices
- Layoffs
- Restructuring activity
- Hiring freezes
- Funding concerns
- Earnings pressure
- Activist investor pressure
- Cost-cutting initiatives

Logic:

If workforce reductions exceed approximately 5%:

Increase emphasis on:

- Efficiency
- Business value
- Execution
- Stability
- Cost awareness

---

### 3. The Jargon Translator

Translate company language into likely operational realities.

Format:

Company Says:
"[Value]"

Reality Is:
"[Likely day-to-day interpretation]"

Example:

Company Says:
"Move Fast"

Reality Is:
"Ambiguity tolerance may be required and processes may be immature."

---

## Phase 2: Employee Voice Intelligence

Analyze publicly available employee and candidate feedback from:

- Employee review sites
- Discussion forums
- Interview reports
- Social media discussions
- Professional communities
- Public employee commentary
- Other publicly accessible sources

Prefer feedback from the last 24 months.

Older feedback should be labeled:

Historical Context

If employee feedback is sparse or unavailable:

- Explicitly state the limitation
- Lower confidence accordingly

---

### Positive Themes

Identify:

Top 3 recurring positive themes.

---

### Negative Themes

Identify:

Top 3 recurring negative themes.

---

### Why Employees Stay

Analyze evidence related to:

- Leadership
- Compensation
- Career growth
- Flexibility
- Mission
- Team quality
- Benefits

---

### Why Employees Leave

Analyze evidence related to:

- Burnout
- Management
- Compensation
- Reorganizations
- Career stagnation
- Workload
- Strategic uncertainty

---

### Current vs Former Employee Comparison

Identify meaningful differences between:

- Current employee sentiment
- Former employee sentiment

Determine whether sentiment suggests:

- Improving culture
- Stable culture
- Deteriorating culture

---

### Leadership Sentiment

Classify:

- Positive
- Mixed
- Negative

---

### Work-Life Balance Sentiment

Classify:

- Positive
- Mixed
- Negative

---

### Career Growth Sentiment

Classify:

- Positive
- Mixed
- Negative

---

### Compensation Sentiment

Classify:

- Positive
- Mixed
- Negative

---

### Employee Sentiment Risk

Classify:

- Strongly Positive
- Mostly Positive
- Mixed
- Concerning
- High Risk

---

### Confidence Assessment

Provide:

- High Confidence
- Moderate Confidence
- Low Confidence

Based on:

- Review volume
- Source diversity
- Recency
- Cross-source consistency

Important:

Treat employee feedback as directional evidence rather than objective fact.

Weight recurring themes significantly higher than isolated complaints.

Do not reproduce lengthy copyrighted reviews.

Summarize recurring patterns only.

---

## Phase 3: Retention Risk Signals

Identify evidence of:

- Leadership churn
- Executive turnover
- Frequent reorganizations
- High employee turnover
- Hiring surges
- Hiring freezes
- Department consolidations
- Strategic pivots
- Morale concerns
- Cost-cutting initiatives

Determine whether patterns suggest:

- Growth
- Stability
- Retrenchment
- Transformation

Classify:

### Retention Risk

- Low Risk
- Moderate Risk
- High Risk

Explain the reasoning behind the classification.

---

## Phase 4: Interview Process Intelligence

Analyze publicly available candidate and employee reports.

Identify:

### Common Interview Themes

- Technical depth
- Leadership focus
- Communication
- Collaboration
- Problem solving
- Business alignment

---

### Assessment Patterns

Identify evidence of:

- Technical interviews
- Coding exercises
- Presentations
- Whiteboard sessions
- Panel interviews
- Behavioral interviews
- Case studies

---

### Candidate Praise

Summarize recurring positive observations.

---

### Candidate Complaints

Summarize recurring negative observations.

---

### Hiring Optimization Analysis

Determine:

"What does this organization appear to optimize for when hiring?"

Provide:

Top 5 likely evaluation criteria.

---

## Phase 5: Reality Check

### Internal Friction

Identify recurring themes such as:

- Technical debt
- Bureaucracy
- Slow decision making
- Micromanagement
- Resource constraints
- Communication breakdowns

---

### Culture Contrast

Compare against the two most relevant competitors.

Identify differences in:

- Culture
- Leadership
- Hiring
- Employee experience
- Strategic priorities

---

### AI Pivot Score

Assess evidence of:

- AI investment
- Workforce replacement concerns
- AI-driven restructuring
- AI-focused hiring shifts

Classify:

- High Impact
- Medium Impact
- Low Impact

---

## Phase 6: The Interview Arsenal

### 1. Dealbreaker Traits

Identify three personality profiles most likely to struggle.

Explain why.

---

### 2. Value-Aligned Stories

Generate interview talking points.

Format:

[Value]
→ [Situation]
→ [Action]
→ [Result]

Incorporate:

- Leadership language
- Company values
- Job description terminology

---

### 3. The Value Stress Test

Generate two high-quality reverse interview questions.

Objective:

Require interviewers to demonstrate how a stated value is
actually practiced within the organization.

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

Immediately after, generate the final report wrapped inside
its own markdown codeblock.

# COMPANY VALUES INTELLIGENCE REPORT

- Target Company: [Company Name]
- Target Position: [Job Title]
- Analysis Date: [YYYY-MM-DD]

------------------------------------------------------------

Overall Confidence Score: [x/10]

### 1. Executive Summary & Market Pressure

### 2. Leadership DNA & Strategic Direction

### 3. Employee Voice Intelligence
- Why employees stay
- Why employees leave
- Current vs former employee comparison
- Leadership sentiment
- Work-life balance sentiment
- Growth sentiment
- Compensation sentiment
- Confidence level

### 4. Retention Risk Signals
- Turnover indicators
- Leadership churn
- Reorganization activity
- Stability outlook
- Risk rating

### 5. Interview Process Intelligence
- Common interview themes
- Assessment patterns
- Hiring priorities
- Candidate observations

### 6. Jargon Translator
- What they say
- What it likely means

### 7. Reality Check
- Internal friction
- Cultural observations
- Public sentiment patterns

### 8. AI Pivot & Organizational Risk

### 9. Interview Dealbreakers & Value-Aligned Stories

### 10. The Value Stress Test
- Questions to ask the interviewer

### Final Assessment
- Would a strong candidate likely thrive here?
- Biggest opportunity
- Biggest risk
- Key point to validate during interviews