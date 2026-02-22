# Usage Examples - Job Posting Snapshot & Preservation Engine

This file shows practical ways to use the engine. All examples follow the same rules from the main prompt:

- Every bullet starts with one exact tag: [VERBATIM], [PARAPHRASED], [INFERRED], [NOT STATED], or [NOT LISTED].
- No added opinions, assumptions, or fake details.
- Output is always two code blocks: Suggested Filename first, then Job Posting Snapshot.

## Quick Start Steps

1. Open the main prompt in your AI chat (ChatGPT, Grok, Claude, etc.).
2. Provide required inputs at the top:
   - Source Type (URL, PDF, Full pasted text, etc.)
   - Source Location (URL or platform name)
   - Capture Date (use today if missing)
   - Posting Date (if visible)
   - Expiration Date / Close Date (if visible)
3. Paste the full source right after (URL, PDF upload, copied text).
4. Let the prompt run. It will give you two code blocks.
5. Copy the second block into the suggested filename and save.

## Example 1: Live URL from LinkedIn or company site

**Input you paste:**

Source Type: URL  
Source Location: https://www.linkedin.com/jobs/view/senior-security-engineer/123456789  
Capture Date: 2025-10-15  
Posting Date: 2025-10-01  
Expiration Date: NOT STATED  

[Then paste the full job description text or just say "Use the URL above" if the AI can fetch it]

**What you get:**  
- Filename suggestion: Posting-CompanyName-SeniorSecurityEngineer-123456789-20251015.md  
- Clean markdown snapshot with tagged bullets under Responsibilities, Qualifications, etc.

**Best for:** Fresh postings you find while browsing.

## Example 2: PDF from Print-to-PDF on a resistant site

**Input you paste:**

Source Type: PDF  
Source Location: Internal career portal - printed from browser  
Capture Date: 2025-11-02  
Posting Date: 2025-10-20  
Expiration Date: 2025-12-31  

[Upload the PDF file directly to the chat or paste extracted text if upload not supported]

**What happens:**  
The prompt reads the PDF content, tags every line properly, and builds the snapshot. No manual text cleanup needed.

**Best for:** Sites that block copy-paste, hide text behind JS, or expire quickly.

## Example 3: Partial / Reconstructed content from memory or old screenshot

**Input you paste:**

Source Type: Partial reconstructed content  
Source Location: Memory + old screenshot from Glassdoor  
Capture Date: 2025-09-10  
Posting Date: NOT STATED  
Expiration Date: NOT STATED  

⚠ SOURCE INCOMPLETE – only partial details available:  
[Then paste what you remember or OCR'd: title, company, 3 responsibilities, required skills]

**What you get:**  
Snapshot marks most fields [NOT STATED] or [NOT LISTED]. You see exactly what's missing.

**Best for:** When the original is gone and you only have notes.

## Example 4: After snapshot – Interview Prep (using Section 6 prompt)

Once you have the saved .md file:

1. Copy the whole snapshot markdown.
2. Start a new chat with the "Interview Preparation" prompt from Section 6.
3. Paste the snapshot and ask: "Using only this snapshot, generate 5 behavioral questions I might get and suggested answers based on my experience with Defender Firewall, Intune, and PowerShell automation."

**Result:** Grounded prep that sticks to the posting's real language.

## Example 5: Hiring Motivation Analysis

Use the "Hiring Intent Analysis" prompt from Section 6.

Paste the snapshot and run it.  
It looks only at Business Context Signals, Responsibilities, and Keywords to tag likely drivers:
- [INFERRED] Growth – new team mentions, multiple openings
- [NOT STATED] Cost Reduction – no language about efficiency or consolidation

**Best for:** Deciding if the role fits your strengths (e.g., Zero Trust, endpoint consolidation projects).

## Tips for Clean Results

- Always provide capture date – helps with filename sorting.
- Use full source when possible – more [VERBATIM] tags = higher confidence.
- If PDF upload fails, extract text first (Adobe Reader select-all → copy) and use Source Type: Full pasted text.
- Save snapshots in a folder like "Job-Snapshots-2025" – easy to grep later.
- Review tags before reusing – [INFERRED] means take with caution.

Add your own examples here as you use it.