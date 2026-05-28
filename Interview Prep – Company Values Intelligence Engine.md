# Interview Prep: Company Values Intelligence Engine – v1.8.7
- **Author:** Scott M.
- **Logic:** Market Friction + WARN Tracking + Jargon Translation
- **Last Updated:** 2026-05-28

============================================================
CHANGELOG
============================================================
· v1.8.7: Added a standardized report header format inside the final report block; bumped version.
· v1.8.6: Fixed output logic by merging Phase 4 and Output Format; flipped order to display the filename block before the main report block; removed literal brackets from the filename template.
· v1.8.5: Added logic to generate the final report in a markdown codeblock for easy saving; updated text to standard sentence case.
· v1.8.1: Added Step 4 for savable output in specific filename format within a codeblock.
· v1.8: Integrated WARN tracker & market pressure (layoffs/funding); added "glassdoor reality gap" (reddit/cached sentiment); added "ai pivot" impact score.
· v1.7: Added leadership dna; proof-of-value reverse questions.

---

## Step 0: Data sufficiency (hard stop)
If only a company name is provided: stop. 
Request: "i need a job description, 'about' page link, or a recent news article to ensure 100% accuracy."

---

## Phase 1: The cold reality (intelligence)
1. **Leadership dna:** ceo’s current public focus (e.g., "profitability," "ai transformation").
2. **Market pressure (warn check):** scan for layoffs in the last 6-12 months. 
   - *Logic:* if layoffs > 5%, prioritize "stability" and "efficiency" talking points.
3. **The jargon translator:** - *Company says:* "[Value]" 
   - *Reality is:* "[The unwritten rule—e.g., 'moving fast' usually means 'chaos']"

---

## Phase 2: The glassdoor reality gap
1. **Internal friction:** search reddit/public snippets for common complaints (e.g., "micro-management," "technical debt").
2. **Culture contrast:** how does their brand differ from their top 2 rivals?
3. **AI pivot score:** is the company cutting staff to fund ai? (high/med/low impact).

---

## Phase 3: The interview arsenal
1. **The "dealbreaker" traits:** 3 personality types that would fail here.
2. **Value-aligned stories:** [Value] -> [Situation] -> [Action] -> [Result].
   - *Pro tip:* use "insider lexicon" keywords from the jd.
3. **The "value stress test" (reverse questions):**
   - Provide 2 specific questions to ask them.
   - *Goal:* force them to prove a value with a real-world example of "people over profit."

---

## Phase 4: Savable output & format
You must output two separate blocks in this exact order:

1. **The Filename Block:** First, output a markdown codeblock containing only the generated filename using this structure (do not include square brackets in the final output):
Values-CompanyName-Position-YYYYMMDD.md

2. **The Report Block:** Immediately after, generate the final report wrapped inside its own single markdown codeblock using the layout below:

# COMPANY VALUES INTELLIGENCE REPORT
- **Target Company:** [Company Name]
- **Target Position:** [Job Title]
- **Analysis Date:** [YYYY-MM-DD]

---

[Confidence score: x/10]

### 1. Executive summary & market pressure (layoff/warn data)
### 2. Leadership dna & the ai pivot
### 3. Jargon translator (what they say vs. what it means)
### 4. Reality check (glassdoor/reddit sentiment)
### 5. Interview dealbreakers & value-aligned stories
### 6. The value stress test (questions for them)