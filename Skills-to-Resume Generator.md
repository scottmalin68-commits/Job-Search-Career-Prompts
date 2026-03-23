# Prompt: Skills-to-Resume Generator (ATS-Friendly)
**Author:** Scott M.  
**Version:** 1.0.1  
**Changelog:** * **v1.0.1:** Added strict anti-hallucination logic; enforced career profile as mandatory input; added Author and Version headers.

## Purpose:
Transform a user’s raw **Career Profile** data into a clean, ATS-optimized resume. This is a foundational document intended for further manual tailoring per job application.

## ⚠️ Critical Rule: No Hallucination
* **Source Material Only:** Use *only* the information provided in the Career Profile. 
* **No Inventing:** Do not bridge gaps in employment or invent specific metrics (percentages, dollar amounts) if they aren't in the source data.
* **Placeholders:** If a standard section (like Dates or Job Titles) is missing from the Profile, use **[INSERT MISSING INFO]**—do not guess or fill it in.

## Instructions for the AI:
1. **Requirement Check:** You **cannot** proceed without a Career Profile input. If it is missing, ask the user to provide it before generating any text.
2. **Structure:** Generate the resume using these standard, ATS-safe headings:
    * CONTACT INFORMATION
    * PROFESSIONAL SUMMARY (2-3 sentences max)
    * SKILLS & CORE COMPETENCIES (Grouped or bulleted)
    * PROFESSIONAL EXPERIENCE (Reverse chronological)
    * EDUCATION
    * ADDITIONAL SECTIONS (Certifications, Projects, etc., if provided)
3. **Formatting Rules:**
    * Use plain text only. No tables, columns, or images.
    * Use bold or ALL CAPS for section headers.
    * Use standard bullet points (`*` or `-`).
    * Start experience bullets with strong action verbs (e.g., Managed, Developed, Resolved).
4. **Tone:** Keep it direct and professional. Avoid fluff, marketing hype, or cliches.

## Input:
**[PASTE CAREER PROFILE DATA HERE]**

## Output Instructions:
* Provide the resume in a clean, copy-pasteable format.
* After generating, include a brief list of any missing data points marked as [INSERT MISSING INFO] so the user knows what to update in their Career Profile.