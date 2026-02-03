## Resume Customization Prompt – MAXIMUM INTEGRITY VERSION (Generic)

### Documentation / Meta Information

**Goal**  
Tailor the resume and cover letter to honestly reflect only what's verifiable in the central Skills Summary file. Maximize truthful alignment with the job without exaggeration, stretching facts, or fabrication. Integrity is non-negotiable; ATS optimization is secondary and must never compromise accuracy.

**Intended Audience**  
- Primarily: Hiring managers, recruiters, and ATS systems  
- Secondary: The job applicant themselves (to maintain personal ownership, honesty, and confidence in what is submitted)

**Author**  
Scott M

**Changelog** (reverse chronological – most recent first)  
- 2026-XX-XX: Added Documentation section (Goal, Audience, Author, Changelog, AI Engine Ranking); simplified author reference to "Scott M"  
- 2026-XX-XX: Added explicit ATS parsing check in output – AI must review proposed resume for common parsing risks and flag them to user  
- 2025-XX-XX: Refined ATS section with 2025–2026 best practices (single-column, exact keyword mirroring, no tables/graphics, front-loading)  
- Earlier: Established single markdown file as sole source of truth; restricted output to changed content in code blocks; enforced strict integrity rules

**Best to Worst AI Engines for Running This Prompt (subjective ranking as of early 2026)**  
1. Grok (xAI) – Best at strict integrity, natural language, and refusing to fabricate or stretch claims  
2. Claude (Anthropic) – Excellent rule-following and honesty; very strong second choice  
3. GPT-4o / o1 family (OpenAI) – Capable but needs heavy prompting to avoid over-optimization or hallucination  
4. Gemini (Google) – Compliant but can be overly cautious or creatively rephrase beyond source  
5. Others – Variable; many prioritize "looking good" over strict source fidelity

### Customization Instructions – Clear & Strict

Use this prompt exactly as written when asking an AI to tailor your resume/cover letter.  
Replace only the bracketed placeholders with your specific details. Do not alter the rules, integrity constraints, or output format unless you intentionally want a custom variant.

Key principles (repeated for clarity):  
- **Single source of truth**: Your central Skills Summary file (e.g., `My_Skills_Summary.md`) is the ONLY thing that matters.  
- Anything not explicitly in that file is removed — no exceptions, no hints, no creative wording to imply it.  
- You may reword, reorder, shorten, combine, or emphasize real entries from the file.  
- You may incorporate exact keywords/phrases from the job description ONLY where they match real experience in the file.  
- Never add, guess, imply, or stretch anything. If it's not there, it's out.  
- Prefer an honest "good fit" over a falsely impressive one.

Hey, here's the job I'm targeting:  
[Insert job URL here / paste the full job description]

Please customize my attached/current resume for this role, strictly following these rules:

1. **Single source of truth** = [My_Skills_Summary.md / name of your central skills file] (in workspace / attached / etc.)  
   Backup link (if needed): [Insert Dropbox/Google Drive/etc. link here]

2. The old/attached resume is only for general layout inspiration and phrasing style.  
   Any bullet, tool, project, responsibility, date, cert, or achievement in the old version but **NOT** in the current Skills Summary file → remove it completely. No exceptions.

**INTEGRITY RULES – NON-NEGOTIABLE:**
- The Skills Summary file alone determines what can be claimed.  
- Delete anything not explicitly supported — no additions, no guesses, no implications.  
- Reword/reorder/shorten/combine/emphasize only real entries from the file.  
- Match job keywords exactly where supported, but preserve original meaning and scope 100%.  
- If the job requires something absent from the file, omit it. No partial matches.

**ATS-Friendly Tips (2025–2026 best practices, 100% honest):**
- Extract exact keywords/phrases from the job description (skills, tools, certs, acronyms + spelled-out).  
- Mirror job language naturally in context when supported.  
- Integrate strategically:  
  - Front-load strongest matches in Professional Summary.  
  - List exact terms in a Skills / Technical Skills section.  
  - Show real usage in experience bullets (not just possession).  
- Formatting rules (critical for parsing):  
  - Single-column layout only  
  - Standard headings (e.g., “Professional Summary”, “Skills”, “Professional Experience”, “Education”, “Certifications”)  
  - Fonts: Arial, Calibri, Times New Roman, Garamond (10–12 pt)  
  - No tables, columns, text boxes, graphics, icons, images, headers/footers for key info, special characters/symbols  
  - Standard bullets (• or -)  
  - Consistent date format (e.g., MM/YYYY or Month YYYY throughout)  
  - Reverse-chronological or hybrid format  
  - Save as .docx (preferred for best parsing) or simple searchable PDF  
- Avoid keyword stuffing — keep language professional, varied, and human.

**Core facts that must appear (only if present in Skills Summary):**
- [List any must-includes here, e.g., total years, key certs, major tools. Delete this section if not needed.]

**Output Format – Clear & Structured:**
Process section by section.

For each major section:  
- Show the original (plain text, full section)  
- Summarize changes  
- Show final version:  
  - Header (plain text, outside block)  
  - Unchanged elements (roles, dates, companies) in plain text outside block  
  - Only changed/revised content (bullets, sentences, skills) inside ```plaintext code block  
- Explain each change briefly, citing exact line/entry from Skills Summary.

For Experience: One role at a time — title/dates/company outside; revised bullets only inside block.  
For Early Career: Combine as needed (e.g., “Early Career Roles”) — header outside, bullets inside block.

Write in natural, professional, human-sounding language.

**Additional ATS Parsing Check (mandatory in output):**  
After presenting the full revised resume, add a dedicated section titled **ATS Parsing Risk Review**.  
In plain text (no code block), clearly list and explain any potential ATS parsing issues in the proposed resume, such as:  
- Use of tables/columns/multi-column layouts  
- Headers/footers with key info  
- Graphics/icons/images  
- Special characters or non-standard symbols  
- Inconsistent date formats  
- Non-standard section headings  
- Text boxes or other complex elements  
- Any other 2025–2026 common parsing risks (e.g., unusual fonts, embedded objects)  
If none are present, state clearly: "No major ATS parsing risks detected – resume uses single-column, standard headings, consistent dates, and plain text formatting compatible with most modern ATS systems (Workday, iCIMS, Greenhouse, etc.)."  
Point out fixes if needed, but do not alter the resume content unless it violates integrity rules.

After resume + ATS check: Write cover letter using ONLY Skills Summary content. Full letter in ```plaintext block with header:  
[Full Name]  
[City, State ZIP] | [Phone] | [Email] | [LinkedIn or other profile]

If ATS-heavy job: End with plain bulleted list of exactly six matching skills from Summary that appear in JD.

Log the application:  
- Job title:  
- Company:  
- URL:  
- Date: [today’s date]  
- Status: Applied

Use • bullets.

**Bottom line**: Integrity first. Always.
