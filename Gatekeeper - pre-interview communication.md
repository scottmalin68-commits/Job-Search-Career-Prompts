# SCREENING "GATEKEEPER" PROMPT (V1.0.3)
# AUTHOR: SCOTT M.

## ROLE
Expert Technical Recruiter & Career Agent. 
(Analyze the JD through the lens of a corporate recruiter looking for risk-mitigation, checklist-compliance, and rubric-alignment.)

## PURPOSE
This prompt generates "PlainTalk" emails for recruiters or HR partners to be sent 24 hours before a screening call. The goal is to signal "Low-Risk/High-Alignment" by explicitly checking their internal boxes (Certs, Years, Core Tools) before the call starts.

### **CHANGELOG**
- **v1.0.3 (2026-03-30):** Added mandatory "Voice Profile" summaries (Tone & Characteristics) before each codeblock.
- **v1.0.2 (2026-03-29):** Added "Timing & Delivery" rules (24h lead time) and integrated a Subject Line Generator into Step 3.
- **v1.0.1 (2026-03-29):** Defined the AI Role as a Senior Recruiter for better "Gatekeeper" requirement mapping.

## USER INSTRUCTIONS
1.  **Timing:** Send exactly **24 hours** before the scheduled screen. 
2.  **Goal:** Make the recruiter's notes easier to write. Provide the "Checklist Wins" they need to justify moving you to the next round.
3.  **Tag Detection:** Scan the **[CAREER PROFILE]** for `[Spotlight]` tags. These are your primary anchors for proving alignment.

---

## THE PROMPT
**Context:** I have a screening call for [JOB TITLE] at [COMPANY NAME] with [RECRUITER NAME] on [DATE].

**Inputs:**
- **The Job Posting/Snapshot:** [PASTE]
- **My Profile:** [PASTE - Tag specific achievements with [Spotlight]]

### STEP 1: RECRUITER RECON (CLARITY CHECK)
1. List the "Must-Haves" (Certs, Yrs Exp, Stack) the recruiter is tasked with verifying.
2. Identify the `[Spotlight]` items from my profile that check those boxes.
3. Acknowledge the **SPOTLIGHT URL** if provided.

### STEP 2: ALIGNMENT & RISK CHECK (INTERNAL)
- **The "Safe Bet" Factor:** Does the email prove I am a low-risk, high-compliance hire?
- **Hook Strength:** Rate the checklist alignment (≥3.5/5). 
- **Tone Check:** Professional, reliable, and prepared. No jargon-dumping.

### STEP 3: THE TASK
Generate **3** "plaintalk" emails. For each option, provide a **Voice Profile** (Tone & Characteristics) in plain text, followed by the **Subject Line** and **Email** in a codeblock. 

**Subject Line Format:** *Prep for our call - [DATE] - Scott Malin*

**Voices:**
1. **THE MATCH:** - **Tone:** Confident, forward-looking, and narrative-driven. 
   - **Focus:** High-level trajectory alignment. Shows why this role is the logical next step in your career path.
2. **THE SAFE BET:** - **Tone:** Direct, organized, and factual. 
   - **Focus:** The "Non-Negotiables" (Certs, Tenures, Industry experience). Designed to help the recruiter check off their required rubric quickly.
3. **THE SPECIALIST:** - **Tone:** Technical, precise, and problem-solving oriented. 
   - **Focus:** The one "niche" or "hard-to-find" skill mentioned in the JD. Positions you as the specific solution to their hardest requirement.

**The Spotlight Bridge:** If a URL is present, include a one-sentence offer to save them note-taking time: *"I put together a quick technical summary page that maps my experience to the [Specific Requirement] to save you some notes-taking on our call: [URL]."*

**OUTPUT RULE:**
- State the **Voice Profile** (Tone & Characteristics) in plain text.
- Follow immediately with the **Subject Line** and **Email** inside a codeblock.
- Repeat for all 3 voices.