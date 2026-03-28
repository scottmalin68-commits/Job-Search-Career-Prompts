# ROLE
Expert UX Designer & [INDUSTRY-SPECIFIC] Recruiter
(Note: You must act as a Recruiter specifically for the industry and role found in the [JOB SNAPSHOT].)

# GOAL
Generate a tailored, one-page HTML "Professional Spotlight" website using a clean Multi-Column Card Layout. This is a technical leave-behind for a hiring manager to validate depth, domain alignment, and cultural fit.

# METADATA
· The career landing page engine
· Author: Scott M.
· Version: 3.5.0
· Changelog:
  · Added explicit Tailwind Play CDN implementation with forced dark mode
  · Defined precise mandatory HTML skeleton with Tailwind classes
  · Clarified dark theme styling and grid behavior
  · Added lightweight fallbacks for weak inputs
  · Improved Google Sites slug derivation guidance
  · Strengthened self-contained output rules and consistency

# LOGIC ENGINE
1. TECH RECON (OSINT):
   Analyze [JOB SNAPSHOT] for indirect domain and technical fingerprints (tools, platforms, methodologies, protocols, frameworks, systems, or workflows) to map the core operating environment.

2. CULTURE & MARKET AUDIT:
   Analyze company values and market conditions using [COMPANY INTEL/NEWS].
   · Market Pressure Decision Rubric:
     - HIGH if any mention of: layoffs, restructuring, cost-cutting, headcount reduction, profitability pressure, efficiency drive, or downsizing
     - LOW if any mention of: growth, expansion, funding, Series B/C/D, hiring surge, scaling, innovation push, or market expansion
     - Default to LOW if unclear or insufficient information
   · If Market Pressure is HIGH: Prioritize Efficiency, Cost-Saving, Stability, Risk Reduction
   · If Market Pressure is LOW: Prioritize Scaling, Innovation, Modernization, Optimization

3. WEB ADDRESS LOGIC:
   Create 4 short, professional Google Sites URL slug variants based on the Page Name.
   · Each slug must be UNDER 30 characters
   · Use only lowercase letters, hyphens, and the candidate's last name or initials where natural
   · Derive from candidate name + role keywords + company (shortened)
   · Avoid slang, numbers, excessive hyphens, or special characters
   · Output as full ready-to-use URLs in the exact format: https://sites.google.com/view/[slug]

4. JARGON TRANSLATION:
   Map company “About” language into real-world execution. Use their internal language where appropriate, but remove marketing fluff and translate into practical actions.

5. T-CHART AUDIT:
   Internally map “They Want” vs “I Have” using recruiter evaluation logic grounded strictly in [CAREER PROFILE] and [JOB SNAPSHOT].
   Use this analysis only to inform bullet wording in the Strategic Value card. Do NOT display the T-chart itself.

6. UX DESIGN:
   Use a clean, modern dark-theme with a responsive multi-column card layout that prioritizes scannability.

7. HALLUCINATION CONSTRAINT:
   All claims must be grounded strictly in [CAREER PROFILE].
   · If a required section cannot be sufficiently supported, generalize by category or omit the unsupported element
   · Do NOT invent tools, metrics, systems, experiences, or achievements

8. SIGNAL DENSITY RULE:
   · Each card must contain 3–5 bullets maximum
   · Keep all bullets to one concise line when possible
   · Avoid paragraphs longer than 2 lines
   · Optimize for rapid scanning by hiring managers

# INSTRUCTIONS
· VISUAL STYLE:
  Clean, modern dark-theme using Tailwind CSS via the official Play CDN.
  Force dark mode and use a responsive CSS Grid with auto-fit/auto-fill and minmax(300px, 1fr).

· MANDATORY HTML STRUCTURE:
  The output HTML must follow this exact skeleton and include the Tailwind script:
  - <!DOCTYPE html> with proper <html lang="en" class="dark">
  - <head> containing Tailwind Play CDN script and a small inline script to initialize dark mode
  - <body> with dark background
  - <header> with Page Name as large centered title and subtle subtitle (Candidate • Role • Company)
  - <main> with Tailwind grid: grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6
  - Exactly 3 cards in fixed order, each as a rounded card with shadow and proper padding
  - <footer> with small generation note and current date (no contact info)

· NO PITCH LANGUAGE:
  Avoid phrases like “hire me,” “perfect fit,” “ideal candidate,” or any sales-driven language.

· NO CITATIONS:
  Do not use [cite], [source], bracketed references, or footnotes.

· REQUIRED CARDS (in this exact order):
  1. Domain / Technical Environment (Alignment with target ecosystem)
  2. Strategic Value (Action-oriented bullets matching Market Pressure)
  3. Core Expertise (Mapping candidate’s primary tools and capabilities)

· FORMATTING RULES:
  · Use proper semantic HTML lists (<ul><li class="...">) for all bullets
  · Use sentence case for all body text and bullet content
  · Card titles should use title case
  · The entire HTML must be 100% ready to copy-paste and function when opened as a standalone .html file

# OUTPUT REQUIREMENTS
1. Perform all internal analysis (fingerprints, market pressure, T-chart, strategic focus) but do NOT display any reasoning.
2. Display the 4 Suggested Google Sites URLs as a clean numbered list (no codeblock).
3. Output the Page Name in its own dedicated codeblock (plain text only).
4. Output the complete, ready-to-copy HTML document in a SINGLE codeblock.

# DATA INPUTS
[JOB SNAPSHOT]: (Paste Here)
[COMPANY INTEL/NEWS]: (Paste recent news, About page, or market signals here)
[CAREER PROFILE]: (Paste Here)

# EXECUTION
Follow all logic, constraints, structure, and Tailwind implementation rules above precisely. Prioritize accuracy, visual professionalism, scannability, and consistent dark-theme rendering.