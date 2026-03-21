### **The JD Tech Stack Recon & OSINT Prompt**

**Author:** Scott M.
**Purpose:** Extract technical "fingerprints" and context clues from a JD to map a company’s stack and identify potential hiring scams.
**Changelog:**
· v1.3 (2026-03-20): Added Indirect Context Clues (protocols/flavors) and Saveable Report output logic.
· v1.2: Added "Golden Questions" for interview prep.
· v1.1: Added Scam/Red Flag detection layer.
· v1.0: Initial release (Vendor extraction).

---

### **Instructions for Use**
· **Input:** Paste the full Job Description (JD) and the Company Name below.
· **Context Clues:** This looks for direct mentions (e.g., "CyberArk") AND indirect signals (e.g., "802.1x" suggests Cisco/Aruba network auth).
· **The Goal:** Turn a generic JD into a technical map for interview prep and risk assessment.

---

### **[PROMPT START]**

**Role:** You are a Senior Security Architect and OSINT Specialist.

**Task:** Analyze the provided Job Description (JD) for [Insert Company Name]. 

**Step 1: Technical Fingerprinting (Direct & Indirect)**
· **Direct Mentions:** Identify every explicitly named vendor, software, and language.
· **Context Clues (Indirect):** Identify protocols or niche skills that signal a specific stack. (e.g., "SAML/OIDC" = IDP present; "Powershell + GPO" = Heavy Windows/On-prem).
· **Infrastructure Inference:** Based on "Must Haves," identify the core ecosystem (e.g., "AWS + Terraform" = Cloud-native/DevOps focus).
· **Roadmap Detection:** Identify "Preferred" skills as migration targets (e.g., "Experience with ForgeRock a plus").

**Step 2: OSINT Verification**
· Search for public indicators confirming this stack: tech blog posts, employee LinkedIn skill patterns, or public DNS/SaaS records.

**Step 3: Interview "Golden Questions"**
· Generate 3 high-level technical questions that prove you understand their specific environment and its likely pain points.

**Step 4: Scam & Red Flag Detection**
· Analyze the JD for "Kitchen Sink" requirements, financial traps, or vague, outdated tech requests.

**Step 5: Saveable Output**
· Generate a final "Technical Environment & Recon Report" in a single Markdown codeblock using the [Recon-CompanyName-Position-YYYYMMDD.md] format for me to save.

**[Paste JD Text Here]**

### **[PROMPT END]**