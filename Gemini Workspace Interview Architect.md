# [ENGINE] Gemini Workspace Interview Architect
# Version: 1.3.0
# Author: Scott Malin, CISSP
# Description: Generates a Google Calendar event and a Google Keep prep note using Gemini Workspace extensions.

## [CHANGELOG]
* **v1.3.0 (2026-06-05):** Moved changelog block to the upper section under the Description for better visibility.
* **v1.2.0 (2026-06-05):** Renamed to Gemini Workspace Interview Architect. Updated input specifications to utilize file attachments for automated extraction of job title, company, and context.
* **v1.1.0 (2026-06-05):** Pivoted target output to Google Keep. Consolidated interview metadata and checklist into a single Keep note structure. Added user instructions, author signature, and changelog block.
* **v1.0.0 (2026-06-05):** Initial release. Basic timeline mapping for standard copy-paste to Calendar and Tasks.

---

## [1.0 OBJECTIVE]
Analyze an attached job posting file and an interview date/time to build a structured preparation timeline. Output direct Workspace commands for Gemini to create a Google Calendar event and a unified Google Keep checklist based on the 24H Job Interview Checklist from image_8c5402.png.

## [2.0 INPUT SPECIFICATION]
The user must provide:
- [Attachment]: Job description file, posting screenshot, or PDF.
- [Interview Date & Time]: 

## [3.0 USER INSTRUCTIONS]
1. Attach your job posting document or screenshot to the chat.
2. Provide the interview date and time.
3. Paste this prompt engine alongside the inputs.
4. Once Gemini presents the plan, reply: "Execute Workspace creation" to let it use extensions to create the Calendar and Keep entries.

## [4.0 EXECUTION LOGIC]
1. Parse the attached document to extract the [Job Title], [Company Name], and key requirements.
2. Calculate the T-Minus schedule based on the provided interview start time.
3. Structure a single Google Keep note that embeds the target job context and the chronological checklist.
4. Group technical checks (audio, video, software) 2 hours before the interview.
5. Group strategic checks (walking deck, story categories, company research) logically across the preceding 24 hours.

## [5.0 OUTPUT FORMAT]

### 5.1 GOOGLE CALENDAR ACTION
* **Event Title:** Interview: [Extracted Job Title] @ [Extracted Company]
* **Date/Time:** [Date] from [Start Time] to [End Time]
* **Description:** [Insert brief company summary and a reference to the Google Keep prep note]

---

### 5.2 GOOGLE KEEP NOTE ACTION
* **Note Title:** 24H Prep: [Extracted Job Title] @ [Extracted Company]
* **Note Body:**
  
  **INTERVIEW DETAILS**
  * **Date/Time:** [Date & Time]
  * **Role:** [Extracted Job Title]
  * **Company Context:** [Brief analytical summary of company/posting from attachment]

  ---
  
  **PREP CHECKLIST**
  [ ] T-24h: Update Career Walking Deck (tailor to [Extracted Company] branding)
  [ ] T-24h: Identify 3 highlights on "About Me" slide relevant to the hiring manager
  [ ] T-18h: Practice 90-second intro to answer "Tell me about yourself"
  [ ] T-12h: Use AI to research company news, blogs, earnings, and exec socials
  [ ] T-12h: Research the team's hiring practices and recruitment guides
  [ ] T-4h: Review the job description to finalize the "Why Me" slide
  [ ] T-3h: Review 5 Story Categories (Teamwork, Problem Solving, Leadership, Failures)
  [ ] T-2h: Update software & apps to ensure everything is restarted and running smoothly
  [ ] T-2h: Double-check audio settings and secure a working microphone/headphones
  [ ] T-2h: Double-check video settings and position camera (head to chest)
  [ ] T-1h: Practice sharing screen and using Presentation Mode for Walking Deck
  [ ] T-1h: Prepare 5 smart questions to learn more about the team and priorities