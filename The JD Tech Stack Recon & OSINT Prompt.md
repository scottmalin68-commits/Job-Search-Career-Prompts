### **The JD Tech Stack Recon & OSINT Prompt**
**Author:** Scott M. (@Thanos0000)  
**Purpose:** Extract technical "fingerprints" from a JD to map a company’s real stack, prep killer interview questions, and spot hiring scams or red flags early.  
**Changelog:**  
· v1.1 (2026-03-20): Expanded scam/red-flag list, clarified OSINT sources, added structured output format, extra inference examples.  

---

### **Instructions for Use**
· **Input:** Paste the full Job Description (JD) text and the Company Name below.  
· **Why it works:** The actual posting reveals far more specific tooling than generic searches or recruiter summaries.  
· **The Goal:** Transform a vague or buzzword-heavy JD into:  
  - A realistic tech map for interview preparation  
  - Smart, stack-specific questions that show you've done real homework  
  - Early warning on potential scams, disorganized teams, or unrealistic expectations  

---

### **[PROMPT START]**

**Role:** You are a Senior Security Architect, Technical Recon Specialist, and OSINT practitioner with deep experience reading between the lines of job postings.

**Task:** Analyze the provided Job Description for **[Insert Company Name]**.

**Step 1: Technical Fingerprinting**  
- List every explicitly named vendor, SaaS tool, programming language, framework, cloud provider, database, or security product.  
- **Core Stack Inference (Must-Haves):** Deduce the primary/current environment.  
  Examples:  
  - "SailPoint + Azure AD" → likely Microsoft-centric shop with IGA in the cloud  
  - "Okta + AWS + Terraform" → modern cloud-native identity on AWS with IaC  
  - "PingFederate + on-prem AD" → legacy federation, probably hybrid/multi-cloud migration candidate  
- **Roadmap / Migration Clues (Preferred / Nice-to-Have):** Tools listed as "a plus" or "preferred" often signal what they are moving toward or piloting.  

**Step 2: OSINT Verification (Public Signal Check)**  
Cross-reference the inferred stack against publicly available indicators (do not hallucinate; only use real, accessible sources):  
- Company careers page consistency (are similar roles posted officially?)  
- Recent employee LinkedIn profiles (endorsed skills, tools mentioned in experience)  
- Company tech blog posts, GitHub repos, or engineering talks/conference slides  
- BuiltWith / Wappalyzer-style web stack (for customer-facing properties)  
- Public DNS records (TXT/SPF/DMARC verification for SaaS like Okta, Google Workspace, etc.)  
- Recent press releases or job-board patterns  

**Step 3: Interview "Golden Questions"**  
Generate **3 high-signal technical questions** that demonstrate deep homework and systems thinking.  
Make them specific to the inferred stack, integrations, or likely pain points.  
Examples:  
- "I see you're using SailPoint with Azure AD — how are you handling just-in-time provisioning latency during peak login times?"  
- "With Okta + AWS + Terraform in the mix, what’s your current approach to secrets rotation across both IdP and cloud resources?"  

**Step 4: Scam & Red Flag Detection**  
Evaluate the JD and context for common hiring scam patterns and organizational dysfunction signals:  
- **Kitchen Sink / Unicorn Hunter JD** — one role demanding senior-level expertise across 8–10 unrelated domains (IAM + SOC + GRC + DevOps + compliance + pen-testing + etc.)  
- **Financial Traps** — any mention of paying for equipment, background checks, training, software licenses, or "deposits" (almost always a scam)  
- **Vague or Outdated Buzzword Salad** — "Global Leader" / "Fast-growing startup" but tech stack is 10+ years old or suspiciously generic  
- **No Official Footprint** — job not on company careers site, uses generic email (gmail, proton, etc.), no company domain in comms  
- **Pressure Tactics** — "act now," "immediate hire," "limited spots," interview via chat only or Google Hangouts/WhatsApp without video  
- **Unrealistic Pay/Requirements** — very high remote salary for entry-level skills or zero experience required  
- **Contradictory Posture** — security/compliance role mentioning FedRAMP + ancient on-prem tools, or heavy cloud but no IaC/CICD mentioned  
- **Communication Red Flags** — heavy typos/grammar issues, inconsistent story, refusal to do video call  

**[Paste JD Text Here]**

**Desired Output Format**  
Use this exact structure for clarity and scannability:

**Company:** [Name]  
**Confirmed / Explicitly Mentioned Tools:**  
[list]  

**Inferred Core Stack:**  
[summary + reasoning]  

**Likely Migration / Future Tools:**  
[summary + reasoning]  

**OSINT Corroboration Summary:**  
[brief findings — confirmed, partial match, no signal, conflicting]  

**3 Golden Interview Questions:**  
1. …  
2. …  
3. …  

**Red Flags / Risk Assessment:**  
Low / Medium / High  
[explanation + which flags triggered]
