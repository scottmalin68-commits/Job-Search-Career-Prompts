# PRE-INTERVIEW "TABLE SETTER" PROMPT (V1.8.1)
# AUTHOR: SCOTT M.

### **CHANGELOG**
- **v1.8.1 (2026-03-28):** Minor integration update. Added support for [SPOTLIGHT URL] within the Job Snapshot. If detected, the engine will weave a "Technical Resource" bridge into the close of each email.
- **v1.8 (2026-03-23):** Added "Hook Strength" diagnostic (average ≥3.5/5) and mandatory JD-specific details.

### **THE PROMPT**
**Context:** I have an interview for [JOB TITLE] at [COMPANY NAME] on [DATE].
**Inputs:**
- **The Job Posting/Snapshot:** [PASTE - Include SPOTLIGHT URL here if generated]
- **My Profile:** [PASTE]

---
### **STEP 1: REVERSE PROMPTING (CLARITY CHECK)**
(Same as v1.8, but adds): 
4. Check for a **SPOTLIGHT URL**. If present, acknowledge it will be used as a "Technical Resource" bridge in the emails.

---
### **STEP 2: ADVERSARIAL PRE-CHECK + HOOK STRENGTH (INTERNAL)**
(Keep all v1.8 logic for Skepticism Points and 3.5/5 scoring.)

---
### **STEP 3: THE TASK**
Generate **3** "plaintalk" emails in separate code blocks. 

**The Spotlight Bridge (New for 1.8.1):** If a URL is present, include a one-sentence "Technical Resource" offer before the close. It should feel like a time-saver for the manager, not a self-promotion.
*Example:* "I mapped out my approach to [Market Friction] on a quick technical spotlight page here: [URL]."

### **STRUCTURE & VOICES**
(Keep all v1.8 structures for The Why, The How, and the 3 Voices.)

### **OUTPUT RULE**
- Output only the final emails in code blocks.