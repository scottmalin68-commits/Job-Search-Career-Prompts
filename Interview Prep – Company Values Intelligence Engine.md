# Interview Prep: Company Values Intelligence Engine – v1.9.0

* **Author:** Scott M.
* **Logic:** Market Friction + WARN Tracking + Jargon Translation + Employee Voice Intelligence
* **Last Updated:** 2026-06-08

============================================================
CHANGELOG
=========

· v1.9.0: Added Employee Voice Intelligence analysis; added interview process intelligence; added confidence weighting for employee sentiment; prioritized recent employee feedback; expanded final report structure.
· v1.8.7: Added a standardized report header format inside the final report block; bumped version.
· v1.8.6: Fixed output logic by merging Phase 4 and Output Format; flipped order to display the filename block before the main report block; removed literal brackets from the filename template.
· v1.8.5: Added logic to generate the final report in a markdown codeblock for easy saving; updated text to standard sentence case.
· v1.8.1: Added Step 4 for savable output in specific filename format within a codeblock.
· v1.8: Integrated WARN tracker & market pressure (layoffs/funding); added "glassdoor reality gap" (reddit/cached sentiment); added "ai pivot" impact score.
· v1.7: Added leadership dna; proof-of-value reverse questions.

---

## Step 0: Data sufficiency (hard stop)

If only a company name is provided: stop.

Request:

"i need a job description, 'about' page link, or a recent news article to ensure 100% accuracy."

---

## Phase 1: The cold reality (intelligence)

### 1. Leadership dna

Identify executive priorities and current public messaging.

Examples:

* profitability
* growth
* ai transformation
* operational efficiency
* customer obsession

Determine:

"What appears to matter most to leadership right now?"

### 2. Market pressure (warn check)

Scan for:

* layoffs
* restructuring
* hiring freezes
* earnings pressure
* activist investor activity
* major funding changes

Logic:

If layoffs exceed approximately 5% of workforce, prioritize:

* efficiency
* stability
* execution
* measurable business value

### 3. The jargon translator

Translate company values into likely operational realities.

Format:

Company says:
"[Value]"

Reality is:
"[Likely day-to-day interpretation]"

---

## Phase 2: Employee voice intelligence

Analyze employee feedback from public sources including:

* Current employees
* Former employees
* Recent departures (last 12–24 months preferred)
* Public discussion forums
* Interview experience reports

Prioritize feedback from the most recent 24 months.

Older feedback should be labeled as historical context.

Identify:

### Positive themes

* Top 3 recurring positive themes

### Negative themes

* Top 3 recurring negative themes

### Why employees stay

* Career growth
* Compensation
* Leadership
* Flexibility
* Mission

### Why employees leave

* Burnout
* Management
* Compensation
* Reorganization
* Career stagnation

### Leadership sentiment

Classify:

* Positive
* Mixed
* Negative

### Work-life balance sentiment

Classify:

* Positive
* Mixed
* Negative

### Career growth sentiment

Classify:

* Positive
* Mixed
* Negative

### Compensation sentiment

Classify:

* Positive
* Mixed
* Negative

### Employee sentiment risk

Determine:

* Strongly Positive
* Mostly Positive
* Mixed
* Concerning
* High Risk

Important:

Treat employee reviews as directional signals rather than objective truth.

Weight recurring themes significantly higher than isolated complaints.

Provide confidence levels:

* High Confidence
* Moderate Confidence
* Low Confidence

Based on:

* Review volume
* Recency
* Cross-source consistency

Do not reproduce lengthy copyrighted reviews.

Summarize recurring themes only.

---

## Phase 3: Interview process intelligence

Analyze publicly available candidate and employee reports.

Identify:

### Common interview themes

* Technical depth
* Leadership focus
* Communication skills
* Culture fit
* Problem solving

### Assessment patterns

* Coding
* Whiteboard
* Case study
* Presentation
* Panel interview

### Candidate praise

Common positive observations.

### Candidate complaints

Common negative observations.

Determine:

"What does this organization appear to optimize for when hiring?"

Provide:

### Predicted interviewer priorities

Rank the top five likely evaluation criteria.

---

## Phase 4: The glassdoor reality gap

### Internal friction

Identify recurring complaints such as:

* Technical debt
* Bureaucracy
* Slow decision making
* Micromanagement
* Resource constraints

### Culture contrast

Compare the company against its two most relevant competitors.

Identify:

* Cultural differences
* Hiring differences
* Leadership differences

### AI pivot score

Determine whether there is evidence of:

* AI investment
* Workforce replacement concerns
* AI-driven restructuring

Classify:

* High Impact
* Medium Impact
* Low Impact

---

## Phase 5: The interview arsenal

### 1. Dealbreaker traits

Identify three personality profiles most likely to struggle or fail in this environment.

Explain why.

### 2. Value-aligned stories

Generate interview talking points.

Format:

[Value]
→ [Situation]
→ [Action]
→ [Result]

Use terminology from:

* Job description
* Company values
* Leadership messaging

### 3. The value stress test

Generate two high-quality reverse interview questions.

Goal:

Require the interviewer to provide evidence that a stated company value is genuinely practiced.

---

## Phase 6: Savable output & format

You must output two separate blocks in this exact order:

### 1. Filename Block

Output a markdown codeblock containing only:

Values-CompanyName-Position-YYYYMMDD.md

### 2. Report Block

Immediately after, generate the final report wrapped inside its own markdown codeblock.

# COMPANY VALUES INTELLIGENCE REPORT

* **Target Company:** [Company Name]
* **Target Position:** [Job Title]
* **Analysis Date:** [YYYY-MM-DD]

---

**Overall Confidence Score:** [x/10]

### 1. Executive Summary & Market Pressure

### 2. Leadership DNA & Strategic Direction

### 3. Employee Voice Intelligence

* Why employees stay
* Why employees leave
* Leadership sentiment
* Work-life balance sentiment
* Growth sentiment
* Compensation sentiment
* Confidence level

### 4. Interview Process Intelligence

* Common interview themes
* Assessment patterns
* Hiring priorities
* Candidate observations

### 5. Jargon Translator

(What they say vs. what it likely means)

### 6. Reality Check

(Glassdoor, Reddit, public sentiment, recurring friction points)

### 7. AI Pivot & Organizational Risk

### 8. Interview Dealbreakers & Value-Aligned Stories

### 9. The Value Stress Test

(Questions to ask them)
