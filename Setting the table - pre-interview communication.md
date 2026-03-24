# PRE-INTERVIEW "TABLE SETTER" PROMPT (V1.8)
# AUTHOR: SCOTT M.

### **PURPOSE STATEMENT**
To generate three (optionally four) distinct "plaintalk" email options that position the candidate as a high-value problem solver. These emails use adversarial logic to preemptively address skepticism and "hook" the hiring manager into a specific interview narrative.

### **CHANGELOG**
- **v1.8 (2026-03-23):** Added requirement for at least one company/job-specific detail per email in "The How" bullets. Integrated internal "Hook Strength" diagnostic (post-Adversarial Pre-Check) to ensure hooks neutralize the skepticism point (average ≥3.5/5). Expanded "The Why" to favor recent/verifiable tension points when context allows. Added optional close variant for confirmed/scheduled interviews. Added output optionality for a fourth variant.
- **v1.7 (2026-03-23):** Added "Adversarial Pre-Check" to identify and neutralize candidate weaknesses. Integrated "Reverse Prompting" logic to request missing critical context. Refined "The Why" to include industry-specific tension points.
- **v1.6 (2026-03-23):** Added "Bullet Quality Check Layer" for internal scoring. Integrated conversation steering logic.
- **v1.5 (2026-03-23):** Added diagnostic “Why” framing and readability constraints.

### **THE PROMPT**
**Context:** I have an interview for [JOB TITLE] at [COMPANY NAME] on [DATE].
**Inputs:**
- **The Job Posting/Snapshot:** [PASTE]
- **My Profile:** [PASTE]

---
### **STEP 1: REVERSE PROMPTING (CLARITY CHECK)**
Before generating emails, scan the Inputs. If any of the following are missing or vague, **STOP** and ask me for them:
1. The primary "pain point" or reason this role is open (if not in the posting).
2. A specific metric or tool mentioned in the job that is missing from my profile.
3. The name/title of the person I am meeting.
**If context is sufficient, proceed to Step 2.**

---
### **STEP 2: ADVERSARIAL PRE-CHECK + HOOK STRENGTH DIAGNOSTIC (INTERNAL)**
1. Identify one "Skepticism Point" (e.g., lack of specific industry exp, a gap, or being over/under-qualified).
   - Do not mention this weakness directly.
   - Instead, ensure at least one email subtly addresses it by highlighting a **transferable win** or **related logic** that proves the concern is a non-issue.

2. **After planning hooks for all three emails, internally score each hook 1–5 on "Hook Strength"** (how directly + convincingly it neutralizes the Skepticism Point without naming it).  
   - If average Hook Strength across the three emails is < 3.5, strengthen/replace with better transferable examples before proceeding.

---
### **STEP 3: THE TASK**
Generate **3** "plaintalk" emails in **separate code blocks**. (If requested or if context is especially rich, generate a fourth variant—e.g., more industry-specific, shorter, or tailored to a different voice.)

**Constraints:**
- **Length:** 120–180 words.
- **Readability:** No paragraph over 2 lines. Use bullet points.
- **Tone:** Direct, human, zero corporate hype (no "passionate," "excited," or "honored").
- **Company-Specific Requirement:** At least **one bullet** per email must reference a detail pulled directly from the job posting (e.g., a named tool, metric, goal, or stated challenge).

### **STRUCTURE FOR EACH EMAIL:**
#### **1. The Why (The Tension Point)**
Open with a sharp, researched-feeling observation about a challenge the company (or similar orgs) is likely facing.  
- Tie to something recent/verifiable when possible (e.g., from earnings calls, product news, industry reports, or common pain at that company size/stage).  
- *Example:* "Most mid-size SaaS teams right now are bleeding margin on [specific friction from recent earnings call / industry benchmark]. This role looks built to clamp that down."

#### **2. The How (The Hooks)**
Include **2–3 bullets** (internally scored for Relevance: 5/5, Clarity: 5/5, Hook: 4/5 **+ Hook Strength ≥3.5 average**).  
- Use "Before → After" or "Challenge → Outcome" logic.  
- Leave out the "process" details to invite "How did you do that?" questions.  
- **Mandatory:** At least one bullet references a specific detail from the job posting.

#### **3. The Close (Low Friction)**
- A simple forward-looking statement.  
- No hard "ask" for the job—just a "see you then" vibe.  
- **Optional variant (use when interview is confirmed/scheduled):** "Looking forward to digging into this on [day/time]."  
- Otherwise default to neutral: "See you [day/time]." or "Talk soon."

### **THE 3 VOICES:**
1. **The Direct Professional:** Factual, lean, focused on bottom-line results.
2. **The Conversational Peer:** Uses "And/But/So," sounds like a coffee chat between experts.
3. **The Strategic Adversary:** Directly addresses the hardest part of the job first to show you aren't afraid of the "mess."

### **OUTPUT RULE:**
- Do not show your internal scoring, adversarial notes, or hook-strength diagnostics.
- Only output the final emails (in separate code blocks).
- **Optional closing line (if user might want more):** "If you'd like a fourth variant (e.g., more industry-specific, shorter, or adjusted for tone), just say the word."