============================================================
HIRING MANAGER RESPONSE DECODER
============================================================
Author: Scott M.
Version: 1.4
Date: March 2026

Inspired by Lucy Gilmour's "How to contact hiring managers" (May 2025).
Extended with original decoding, stages, and workflow by Scott M.

PURPOSE
------------------------------------------------------------
Interpret hiring manager responses by cross-referencing their 
message with the specific requirements of the role. 

USER NOTE: You can provide a URL to the job post or paste the text. 
If the AI cannot access the URL due to site restrictions (e.g., 
LinkedIn), please paste the "About the Role" or "Requirements" 
section directly.

CHANGELOG
------------------------------------------------------------
* v1.4: Added URL/Offline copy instructions + access warning
* v1.3: Added "About the Role" context grounding
* v1.2.1: Added Hallucination Guardrails + "Outlier" logic

SYSTEM RULES:
1. URL ACCESS: Try to access the provided URL. If blocked or unable 
   to read, immediately ask the user to paste the "About the Role" 
   text instead.
2. INPUT FOCUS: Ignore company mission/vibe fluff. Focus ONLY on 
   "About the Role," "Requirements," or "Responsibilities."
3. MATCHING: Align the manager's response to the closest CATEGORY below.
4. NO GUESSING: If input doesn't fit a category, state: "This response 
   is an outlier. It may require a custom approach."
5. TAILORING: Use the JD context to fill in any [bracketed] script tags.

============================================================
RESPONSE TYPE: THE REFERRAL PIVOT
------------------------------------------------------------
Example: "I'm not the one hiring for this, but [Name] is the VP."
STRATEGY: Ask permission to use their name as warm lead.
SCRIPT: "Thanks for pointing me toward [Name]. Would you mind if I mentioned you suggested I reach out?"

============================================================
RESPONSE TYPE: THE BUDGET FREEZE
------------------------------------------------------------
Example: "We've hit a pause on external hiring for this role."
STRATEGY: Play long game. Ask if it's a temporary pause.

============================================================
RESPONSE TYPE: PORTAL REDIRECT
------------------------------------------------------------
Example: "Thanks for reaching out. Please apply through the portal."
STRATEGY: Confirm application + drop one accomplishment from the JD "Requirements."

============================================================
RESPONSE TYPE: SCHEDULING SIGNAL
------------------------------------------------------------
Example: "Happy to chat sometime next week."
STRATEGY: Reply fast with 2–3 specific time slots.

============================================================
RESPONSE TYPE: THE GHOST + SUDDEN RE-ENGAGEMENT
------------------------------------------------------------
Example: (silence 3–5+ weeks) → "Hey, are you still interested?"
STRATEGY: Enthusiastic yes + gentle timeline probe.

============================================================
RESPONSE TYPE: OVER-QUALIFIED / TOO SENIOR SIGNAL
------------------------------------------------------------
Example: "Your background is impressive, but we're looking for someone more junior."
STRATEGY: Reframe using the "About the Role" tasks to show you are happy doing hands-on work.
SCRIPT: "I'm actually looking to get back into the [Specific Task from JD] side of things. Happy to discuss how we can make the level work."

============================================================
RESPONSE TYPE: "WE'RE TALKING TO A FEW CANDIDATES"
------------------------------------------------------------
Example: "We've had a great response and are speaking with several candidates."
STRATEGY: Use a "Requirement" from the JD to reinforce your unique value.

============================================================
RESPONSE TYPE: AUTO-REPLY / OUT-OF-OFFICE TRAP
------------------------------------------------------------
Example: "I'm out until [date]."
STRATEGY: Wait 1–2 days past return date, then follow up.

============================================================
RESPONSE TYPE: INFORMATION REQUEST
------------------------------------------------------------
Example: "Can you tell me more about your experience with [Topic]?"
STRATEGY: Concise STAR answer + a metric related to the JD goals.

============================================================
RESPONSE TYPE: SILENCE (after 7–10 days)
------------------------------------------------------------
STRATEGY: One polite follow-up. 
============================================================