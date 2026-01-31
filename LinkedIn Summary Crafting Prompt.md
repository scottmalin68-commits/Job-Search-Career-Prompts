# LinkedIn Summary Crafting Prompt

## Author
Scott M.

## Goal
The goal of this prompt is to guide an AI in creating a personalized, authentic LinkedIn "About" section (summary) that effectively highlights a user's unique value proposition, aligns with targeted job roles and industries, and attracts potential employers or recruiters. It aims to produce output that feels human-written, avoids AI-generated clichés, and incorporates best practices for LinkedIn in 2025–2026, such as concise hooks, quantifiable achievements, and subtle calls-to-action. Enhanced to intelligently use attached files (resumes, skills lists) for auto-filling details where relevant.

## Audience
This prompt is designed for job seekers, professionals transitioning careers, or anyone updating their LinkedIn profile to improve visibility and job prospects. It's particularly useful for mid-to-senior level roles where personalization and storytelling can differentiate candidates in competitive markets like tech, finance, or manufacturing.

## Changelog
- Version 1.0: Initial prompt with basic placeholders for job title, industry, and reference summaries.
- Version 1.1: Converted to interview-style format for better customization; added instructions to avoid AI-sounding language and incorporate modern LinkedIn best practices.
- Version 1.2: Added documentation elements (goal, audience); included changelog and author; added supported AI engines list.
- Version 1.3: Minor hardening — added subtle blending instruction for references, explicit keyword nudge, tightened anti-cliché list based on 2025–2026 red flags.
- Version 1.4: Added support for attached files (PDF resumes, Markdown skills, etc.); instruct AI to search attachments first and propose answers to relevant questions (#3–5 especially) before asking user to confirm.

## Supported AI Engines (Best to Worst)
- Best: Grok 4 (optimized for truthful, non-moralizing responses, strong file/document search via attachment_search tool), GPT-4o (strong in creative writing and personalization).
- Good: Claude 3.5 Sonnet (excellent for structured, human-like prose), GPT-4 (reliable for detailed outputs).
- Fair: Llama 3 70B (capable but may require fine-tuning for nuance), Gemini 1.5 Pro (good for multimodal but less consistent in tone).
- Worst: GPT-3.5 Turbo (prone to generic, buzzword-heavy responses), smaller models like GPT-2 or basic open-source LLMs (limited context handling and creativity).

## Prompt Text

I want you to help me write a strong LinkedIn "About" section (summary) that's aimed at landing a [specific job title you're targeting, e.g., Senior Full-Stack Engineer / Marketing Director / etc.] role in the [specific industry, e.g., SaaS tech, manufacturing, healthcare, etc.].

Make it feel like something I actually wrote myself—conversational, direct, with some personality. Absolutely no over-the-top corporate buzzwords (avoid "synergy", "leverage", "passionate thought leader", "proven track record", "detail-oriented", "game-changer", etc.), no unnecessary em-dashes, no "It's not X, it's Y" structures, no "In today's world…" openers, and keep sentences varied in length like real people write. Blend any reference styles subtly—don't copy phrasing directly. Include relevant keywords naturally (pull from typical job descriptions in your target role if helpful). Aim for 4–7 short paragraphs that hook fast in the first 2–3 lines (since that's what shows before "See more").

**Important: If the user has attached any files (resume PDF, skills Markdown, text doc, etc.), first search them intelligently for relevant details (experience, roles, achievements, years, wins, skills) and use that to propose or auto-fill answers to questions below where possible. Then ask for confirmation or missing info—don't assume everything is 100% accurate without user input.**

To make this spot-on, answer these questions first so you can tailor it perfectly (reference attachments where they apply):

1. What's the exact job title (or 1–2 close variations) you're going after right now?

2. Which industry or type of company are you targeting (e.g., fintech startups, established manufacturing, enterprise software)?

3. What's your current/most recent role, and roughly how many years of experience do you have in this space? (If attachments cover this, propose what you found first.)

4. What are 2–3 things that make you different or really valuable? (e.g., "I cut deployment time 60% by automating pipelines", "I turned around underperforming teams twice", "I speak fluent Spanish and have led LATAM expansions", or even a quirk like "I geek out on optimizing messy legacy code") — Pull strong examples from attachments if present.

5. Any big, specific wins or results you're proud of? Numbers help a ton (revenue impact, % improvements, team size led, projects shipped). — Extract quantifiable achievements from resume/attachments first if available.

6. What's your tone/personality vibe? (e.g., straightforward and no-BS, dry humor, warm/approachable, technical nerd, builder/entrepreneur energy)

7. Are you actively job hunting and want to include a subtle/open call-to-action (like "Open to new opportunities in X" or "DM me if you're building cool stuff in Y")?

8. Paste 2–4 LinkedIn About sections here (from people in similar roles/industries) that you like the style of—or even ones you don't like, so I can avoid those pitfalls.

Once I have your answers (and any clarifications from attachments), I'll draft 2 versions: one shorter (~150–250 words) and one fuller (~400–500 words). You can mix and match from them.