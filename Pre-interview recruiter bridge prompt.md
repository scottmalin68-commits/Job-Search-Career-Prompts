# Pre-interview "recruiter bridge" prompt (V1.8-HR)
# ADAPTED FROM: SCOTT M.

### **PURPOSE STATEMENT**
To generate three "plaintalk" email options for an HR/Staffing contact. These emails position the candidate as a "safe bet" by aligning past wins directly with the recruiter’s screening criteria and pre-empting common HR filters (salary, longevity, specific tool gaps).

### **CHANGELOG (HR ADAPTATION)**
- **v1.8-HR:** Replaced "Adversarial Logic" with "De-Risking Logic." Shifted "The Why" from technical tension to organizational alignment. Focused "The How" on transferable wins that map to the job description's "must-haves."

---
### **STEP 1: REVERSE PROMPTING (CLARITY CHECK)**
Before generating emails, scan the Inputs. If any of the following are missing, STOP and ask:
1. The recruiter/HR contact's name and title.
2. The specific "must-have" tools or years of experience mentioned in the JD.
3. Any potential "red flags" (e.g., being overqualified, a recent job hop, or a pivot in industry).

---
### **STEP 2: DE-RISKING CHECK + ALIGNMENT DIAGNOSTIC (INTERNAL)**
1. Identify one "HR Filter Point" (e.g., "Is he too senior?", "Does he have [Specific Tool] experience?", "Will he stay?").
2. Ensure at least one email subtly neutralizes this by highlighting a **transferable win** or **logical career progression** that makes the move make sense.
3. Score each "Bridge" 1–5 on how well it makes the recruiter's job easier (Average ≥3.5/5).

---
### **STEP 3: THE TASK**
Generate **3** "plaintalk" emails in **separate code blocks**.

**Constraints:**
- **Length:** 100–150 words (Shorter than HM emails).
- **Readability:** No paragraph over 2 lines. Use bullet points ( · ).
- **Tone:** Helpful, professional, zero hype.
- **Specific Requirement:** At least **one bullet** must map a specific past result to a "Required Qualification" in the JD.

### **STRUCTURE FOR EACH EMAIL:**
#### **1. The Why (Alignment)**
Open with why this specific role at [COMPANY] is the logical next step. 
- Example: "I've been following how [COMPANY] is scaling their security ops; this role seems like the main pivot point for that growth."

#### **2. The How (The Transferable Wins)**
Include **2–3 bullets** using the middle dot ( · ).
- Use "JD Requirement → My Result" logic.
- Keep it high-level enough for a non-technical recruiter to "check the box."

#### **3. The Close (Low Friction)**
- "Ready to sync when your schedule allows."
- "Looking forward to the screen on [Day/Time]."

---
### **THE 3 VOICES:**
1. **The Safe Bet (Direct):** Clean, mirrors the JD language exactly, easy to pass up the chain.
2. **The Culture Fit (Conversational):** Friendly, shows personality, sounds like a "great find" for the team.
3. **The Problem Solver (Strategic):** Focuses on how you've handled similar "growth stages" or "tool migrations" before.

### **OUTPUT RULE:**
- No internal scoring or diagnostics in the output.
- Only the 3 emails in separate code blocks.