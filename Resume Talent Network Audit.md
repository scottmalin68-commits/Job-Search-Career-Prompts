# Resume Talent Network Audit
**Goal:** This prompt audits and tunes your resume specifically for talent network uploads (like company career portals where you upload once and they match you to multiple roles over time). This is NOT for applying to a specific job posting — it's for making sure your resume works well in automated matching systems and stays findable over months.
**Author:** Scott M
**Supported AIs:** Claude, ChatGPT, Gemini, Grok
**Changelog:**
- v1.0 (2025-02-16): Initial version
- v1.1 (2026 tweaks): Added emphasis on prominent Skills section, quantifiable impact in bullets, minor job title searchability, and note on modern parsing favoring context.
**How to use:**
Paste the prompt below into your AI, then paste your resume text right after it. Works best with plain text, not PDF uploads.
**Note:** AI can make mistakes on spelling/grammar and may suggest overly conservative changes. Use your judgment, especially on industry-specific terms and job titles.
---
PROMPT:
You are a resume reviewer. Audit the resume below for a talent network upload.
Check everything in this list and give me specific fixes, not general advice.
Before you start: If you're unsure about whether something is an error (especially technical terms, industry jargon, or job titles), flag it as "verify this" instead of calling it wrong.
Modern talent systems (2025+) handle context better than old ATS, so favor natural keyword use in bullets/summary over pure lists, but still ensure clean extraction for skills/tools.

1. ATS FORMATTING
- Any tables, columns, text boxes, or headers/footers? Flag them as potential parsing issues.
- Is it one clean column of text?
- Any unusual fonts, symbols, or graphics that might not parse?
- Are section headers standard? (Experience, Education, Skills — not creative names)
- Quote the actual text when you flag formatting issues so I can find them.

2. KEYWORDS & JOB TITLES
- Are job titles recognizable and searchable? Flag anything that looks internal/company-specific. Suggest minor rephrasing only if it matches common searchable terms without changing meaning (e.g., 'Senior Widget Wrangler' → 'Senior Software Engineer – Widgets').
- Is there a dedicated Skills section with hard skills listed? Prioritize a prominent, comprehensive Skills/Technical Proficiencies section (bulleted, comma-separated, or simple list). Extract and list all hard skills, tools, technologies, languages, certifications from the experience bullets/summary. Suggest expanding it if evidence exists but it's buried.
- Don't invent keywords — only suggest ones you see evidence for in their actual experience.

3. CONTACT INFO
- Is there an email, phone, and LinkedIn URL?
- Does anything look missing or malformed?
- Quote what you see so I can verify.

4. CONSISTENCY & DATES
- Are all dates formatted the same way? Show examples of inconsistencies.
- Are there any unexplained gaps longer than 3 months?
- Do job titles and company names look complete?

5. SPELLING & GRAMMAR
- Flag potential spelling errors and typos with the exact text.
- Mark technical terms or acronyms as "verify if this is correct terminology" rather than wrong.
- Be specific: quote the text and show what section it's in.

6. COMPLETENESS
- Is there a summary or objective at the top?
- Does each role have bullet points with measurable results, not just duties? Flag bullets that are pure task lists vs. those with impact/metrics (e.g., 'Led team' vs. 'Led 8-person team to deliver project 20% under budget'). Suggest converting weak ones where numbers/context exist in original.
- Are there any sections that look empty or too brief?

7. TALENT NETWORK SPECIFIC
- Is the email address using a professional format (avoid nicknames, numbers, or informal handles)?
- Are there any special characters that could break parsing (bullets formatted as •, —, or other symbols)?
- Would a recruiter scanning this in 10 seconds know exactly what this person does and what level they're at?

For each issue: tell me what the problem is, quote the specific text, show where it is, and suggest what to change it to. If you're uncertain, say "verify this" instead of treating it as definite.

Structure your response as numbered sections matching this checklist (1. ATS FORMATTING, etc.), with sub-bullets for each issue.
