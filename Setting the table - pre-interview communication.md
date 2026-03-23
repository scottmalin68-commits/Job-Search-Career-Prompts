# PRE-INTERVIEW "TABLE SETTER" PROMPT (V1.4.0)
# AUTHOR: SCOTT M.

### **PURPOSE STATEMENT**
To generate three distinct "plaintalk" email options for a hiring manager before an interview. This version leverages "Job Posting Snapshot" intelligence—specifically company health, trajectory, and hidden pain points—to align the user’s career wins with the company’s actual business needs.

### **CHANGELOG**
- **v1.4.0 (2026-03-22):** Integrated "Job Posting Snapshot" logic. Added instructions to prioritize company trajectory, health, and specific "insider" pain points found in the snapshot document.
- **v1.3.0 (2026-03-22):** Added "Three-Voice Output" logic and code block formatting.
- **v1.2.0 (2026-03-22):** Added Negative Constraints and "Proof-of-Logic."
- **v1.1.0 (2026-03-22):** Integrated advanced logic (Chain-of-Thought, Self-Criticism, and Verification).

***

### **THE PROMPT**

**Context:** I have an interview for [JOB TITLE] at [COMPANY NAME] on [DATE]. I want to write a short, high-impact email to the hiring manager to "set the table" before we meet.

**Inputs:**
- **The Job Posting/Snapshot:** [PASTE JOB POSTING OR SNAPSHOT DOCUMENT]
- **My Profile:** [PASTE CAREER PROFILE/RESUME]

**Internal Logic Requirements (Perform these in <thought> tags before writing):**
1. **The Insider Gap:** Dig into the "Snapshot" data. Is the company scaling fast? Dealing with technical debt? Facing a specific market shift? Identify the #1 real-world struggle.
2. **The Strategic Match:** Find the win in my profile that directly addresses that specific trajectory or hurdle.
3. **The "Why":** Use a detail from the company's mission or health (from the Snapshot) to explain why I'm interested in *their* specific path.

**The Task:**
Provide 3 different versions of the email in a **single code block**. Keep them under 125 words. No corporate fluff, no "excited," no "harness."

**The 3 Voices:**
1. **The Direct Professional:** Lean, factual, and confident. Focuses on the "fit" and the business "win."
2. **The Conversational Peer:** Softens the tone. Sounds like a 1:1 message to a future teammate. Uses "And," "But," or "So" to start sentences.
3. **The Problem Solver:** Leads with the "insider" challenge identified in the Snapshot and offers a specific solution based on past experience.

**Style Guide:**
- Short sentences. Simple words. 
- Use "And," "But," or "So" to bridge ideas.
- No marketing fluff. 
- All outputs must be in a code block.