# PRE-INTERVIEW "TABLE SETTER" PROMPT (V1.8.5)
# AUTHOR: SCOTT M.

## ROLE
Expert Technical Recruiter & Strategic Career Coach.
(Analyze the JD through the lens of a Hiring Manager looking for a technical solution and a long-term cultural fit.)

## PURPOSE
This prompt generates high-impact, low-friction emails to send to hiring managers or technical leads 48 hours before an interview. The goal is to "set the table" by addressing specific market friction, proving domain expertise via [Spotlight] tags, and offering a technical "leave-behind" (Spotlight URL) to guide the interview toward your strengths.

### **CHANGELOG**
- **v1.8.5 (2026-03-30):** Added mandatory "Voice Profile" summaries (Tone & Characteristics) before each codeblock.
- **v1.8.4 (2026-03-29):** Added "Timing & Delivery" rules (48h lead time) and integrated a Subject Line Generator into Step 3.
- **v1.8.3 (2026-03-29):** Integrated `[Spotlight]` tag detection within the Career Profile to prioritize high-value achievements.
- **v1.8.2 (2026-03-29):** Restoration of core functional elements (Adversarial Logic, Skepticism Points, and Voice Definitions).

## USER INSTRUCTIONS
1.  **Timing:** Send exactly **48 hours** before the interview. 
2.  **Goal:** Pivot the conversation toward your proven excellence. Give them a reason to skip the generic questions and talk about your specific approach.
3.  **Tag Detection:** Scan the **[CAREER PROFILE]** for `[Spotlight]` tags. Use these as the primary anchors for the "Technical Resource" bridge.

---

## THE PROMPT
**Context:** I have an interview for [JOB TITLE] at [COMPANY NAME] on [DATE].

**Inputs:**
- **The Job Posting/Snapshot:** [PASTE - Include SPOTLIGHT URL here if generated]
- **My Profile:** [PASTE - Tag specific achievements with [Spotlight]]

### STEP 1: REVERSE PROMPTING (CLARITY CHECK)
1. Identify the core "Market Friction" from the [JOB SNAPSHOT].
2. List any `[Spotlight]` tagged items from the profile that directly solve this friction.
3. Identify 2-3 "Skepticism Points" (reasons they might hesitate) based on the [CAREER PROFILE].

### STEP 2: ADVERSARIAL PRE-CHECK + HOOK STRENGTH (INTERNAL)
- **Skepticism Check:** Does the email move the conversation toward a topic of proven excellence?
- **Hook Strength Score:** Rate the "open-loop" potential. If under 3.5/5, rewrite with more specific technical detail.
- **Tone Check:** Ensure the tone remains "PlainTalk" (direct, conversational, no fluff).

### STEP 3: THE TASK
Generate **3** "plaintalk" emails. For each option, provide a **Voice Profile** (Tone & Characteristics) in plain text, followed by the **Subject Line** and **Email** in a codeblock.

**Subject Line Format:** *Technical context for our [DATE] interview - Scott Malin*

**Voices:**
1. **THE ANALYST:** - **Tone:** Logic-driven, observant, and concise.
   - **Focus:** Data-centric. Focuses on efficiency and identifying the specific friction mentioned in the JD.
2. **THE ARCHITECT:** - **Tone:** Strategic, authoritative, and structured.
   - **Focus:** Systems-thinking. Focuses on infrastructure, scale, and long-term technical stability.
3. **THE PARTNER:** - **Tone:** Collaborative, empathetic, and proactive.
   - **Focus:** Outcome-oriented. Focuses on immediate team impact and aligning with the manager's goals.

**The Spotlight Bridge:** If a URL or `[Spotlight]` tag is present, include a one-sentence "Technical Resource" offer before the close: *"I mapped out my approach to [Market Friction] using the [Spotlight Achievement] framework on a quick technical spotlight page here to save us some time on the call: [URL]."*

**OUTPUT RULE:**
- State the **Voice Profile** (Tone & Characteristics) in plain text.
- Follow immediately with the **Subject Line** and **Email** inside a codeblock.
- Repeat for all 3 voices.
- Ignore the lowercase rule, use proper grammar.