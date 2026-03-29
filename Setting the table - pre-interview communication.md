# PRE-INTERVIEW "TABLE SETTER" PROMPT (V1.8.2)
# AUTHOR: SCOTT M.

## PURPOSE
This prompt generates high-impact, low-friction emails to send to hiring managers or technical leads 24–48 hours before an interview. The goal is to "set the table" by addressing specific market friction found in the JD, proving domain expertise, and offering a technical "leave-behind" (Spotlight URL) that saves the manager time during the evaluation process.

### **CHANGELOG**
- **v1.8.2 (2026-03-29):** Restoration of core functional elements (Adversarial Logic, Skepticism Points, and Voice Definitions) previously omitted.
- **v1.8.1 (2026-03-28):** Added support for [SPOTLIGHT URL] within the Job Snapshot as a "Technical Resource" bridge.
- **v1.8 (2026-03-23):** Added "Hook Strength" diagnostic (average ≥3.5/5) and mandatory JD-specific details.

## USER INSTRUCTIONS
1.  **Analyze Inputs:** Scan the **[JOB SNAPSHOT]** for "Market Friction" and look for a **[SPOTLIGHT URL]**.
2.  **Verify Hook Strength:** Ensure every email has a "Hook Strength" score (average ≥3.5/5) by focusing on a specific technical or strategic pain point.
3.  **Adversarial Neutralization:** Subtly address a potential "skepticism point" (e.g., lack of specific industry exp, gap in a toolset) by pivoting to a proven excellence.
4.  **Constraints:** Use "PlainTalk" narrative. No corporate clichés. Use direct, conversational language.

---

## THE PROMPT
**Context:** I have an interview for [JOB TITLE] at [COMPANY NAME] on [DATE].

**Inputs:**
- **The Job Posting/Snapshot:** [PASTE - Include SPOTLIGHT URL here if generated]
- **My Profile:** [PASTE]

### STEP 1: REVERSE PROMPTING (CLARITY CHECK)
1. Identify the core "Market Friction" from the [JOB SNAPSHOT].
2. Identify 2-3 "Skepticism Points" (reasons a recruiter might hesitate) based on the [CAREER PROFILE].
3. Acknowledge the **SPOTLIGHT URL**. If present, confirm it will be used as a "Technical Resource" bridge in the emails.

### STEP 2: ADVERSARIAL PRE-CHECK + HOOK STRENGTH (INTERNAL)
- **Skepticism Check:** Does the email move the conversation toward a topic of proven excellence?
- **Hook Strength Score:** Rate the "open-loop" potential of the email. If the score is under 3.5/5 (too generic), rewrite it to be more JD-specific.
- **Tone Check:** Ensure the tone remains "PlainTalk" (no sales-driven or "pitch" language).

### STEP 3: THE TASK
Generate **3** "plaintalk" emails in separate code blocks using these voices:

1. **THE ANALYST:** Data-centric, focused on efficiency and identifying friction. Sounds like a problem-solver who values metrics and precision.
2. **THE ARCHITECT:** Systems-thinking, focused on structure, scale, and long-term stability. Sounds like a builder who understands how parts fit into the whole.
3. **THE PARTNER:** Outcome-oriented, focused on immediate team impact and alignment with company goals. Sounds like a collaborator who gets the "why" behind the "what."

**The Spotlight Bridge:** If a URL is present, include a one-sentence "Technical Resource" offer before the close. 
*Example:* "I mapped out my approach to [Market Friction] on a quick technical spotlight page here to save us some time on the call: [URL]."

**OUTPUT RULE:**
- Output only the final emails in code blocks.