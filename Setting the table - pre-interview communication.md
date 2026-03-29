# PRE-INTERVIEW "TABLE SETTER" PROMPT (V1.8.3)
# AUTHOR: SCOTT M.

## PURPOSE
This prompt generates high-impact, low-friction emails to send to hiring managers or technical leads 24–48 hours before an interview. The goal is to "set the table" by addressing specific market friction found in the JD, proving domain expertise, and offering a technical "leave-behind" (Spotlight URL) that saves the manager time during the evaluation process.

### **CHANGELOG**
- **v1.8.3 (2026-03-29):** Integrated `[Spotlight]` tag detection within the Career Profile. If detected, the engine prioritizes these specific achievements as anchors for the "Technical Resource" bridge.
- **v1.8.2 (2026-03-29):** Restoration of core functional elements (Adversarial Logic, Skepticism Points, and Voice Definitions).
- **v1.8.1 (2026-03-28):** Added support for [SPOTLIGHT URL] within the Job Snapshot.
- **v1.8 (2026-03-23):** Added "Hook Strength" diagnostic (average ≥3.5/5).

## USER INSTRUCTIONS
1.  **Analyze Inputs:** Scan the **[JOB SNAPSHOT]** for "Market Friction" and look for a **[SPOTLIGHT URL]**.
2.  **Tag Detection:** Scan the **[CAREER PROFILE]** for any text marked with a `[Spotlight]` tag. If it relates to the job friction, use it as the primary proof point in the email.
3.  **Verify Hook Strength:** Ensure every email has a "Hook Strength" score (average ≥3.5/5) by focusing on a specific technical or strategic pain point.
4.  **Adversarial Neutralization:** Subtly address a potential "skepticism point" by pivoting to a proven excellence (ideally a `[Spotlight]` tagged item).
5.  **Constraints:** Use "PlainTalk" narrative. No corporate clichés. Use direct, conversational language.

---

## THE PROMPT
**Context:** I have an interview for [JOB TITLE] at [COMPANY NAME] on [DATE].

**Inputs:**
- **The Job Posting/Snapshot:** [PASTE - Include SPOTLIGHT URL here if generated]
- **My Profile:** [PASTE - Tag specific achievements with [Spotlight] if they are high-priority]

### STEP 1: REVERSE PROMPTING (CLARITY CHECK)
1. Identify the core "Market Friction" from the [JOB SNAPSHOT].
2. List any `[Spotlight]` tagged items from the profile that directly solve this friction.
3. Identify 2-3 "Skepticism Points" based on the [CAREER PROFILE].
4. Acknowledge the **SPOTLIGHT URL**.

### STEP 2: ADVERSARIAL PRE-CHECK + HOOK STRENGTH (INTERNAL)
- **Skepticism Check:** Does the email move the conversation toward a topic of proven excellence?
- **Hook Strength Score:** Rate the "open-loop" potential. If under 3.5/5, rewrite with more JD-specific detail.
- **Tone Check:** Ensure the tone remains "PlainTalk."

### STEP 3: THE TASK
Generate **3** "plaintalk" emails in separate code blocks using these voices:

1. **THE ANALYST:** Data-centric, focused on efficiency and identifying friction. 
2. **THE ARCHITECT:** Systems-thinking, focused on structure, scale, and long-term stability. 
3. **THE PARTNER:** Outcome-oriented, focused on immediate team impact and alignment.

**The Spotlight Bridge:** If a URL or `[Spotlight]` tag is present, include a one-sentence "Technical Resource" offer before the close. 
*Example:* "I mapped out my approach to [Market Friction] using the [Spotlight Achievement] framework on a quick technical spotlight page here: [URL]."

**OUTPUT RULE:**
- Output only the final emails in code blocks.