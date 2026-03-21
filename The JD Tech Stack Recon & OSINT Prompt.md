### **The JD Tech Stack Recon & OSINT Prompt (v1.2)**

**Author:** Scott M.
**Purpose:** Extract technical "fingerprints" and context clues from a JD to map a company’s stack and identify potential hiring scams.
**Changelog:**
· v1.2 (2026-03-20): Added Indirect Context Logic and "Saveable Report" output instruction.

---

### **Instructions for Use**
· **Input:** Paste the full Job Description (JD) and the Company Name below.
· **Context Clues:** This engine looks for direct mentions (e.g., "Okta") AND indirect signals (e.g., "SAML/OIDC" suggests an IDP is in place).
· **The Goal:** Turn a generic JD into a technical map for interview prep and risk assessment.

---

### **[PROMPT START]**

**Role:** You are a Senior Security Architect and OSINT Specialist.

**Task:** Analyze the provided Job Description (JD) for [Insert Company Name]. 

**Step 1: Technical Fingerprinting (Direct & Indirect)**
· **Direct Mentions:** Identify every explicitly named vendor, software, and language.
· **Context Clues (Indirect):** Look for protocols or "flavors" of tech. (e.g., "IAM with 15+ years experience" usually implies legacy Mainframe or Oracle/IBM environments; "Fast-paced cloud native" + "Go/Python" implies AWS/GCP and microservices).
· **Infrastructure Inference:** Based on "Must Haves," identify the core stack (e.g., "SailPoint + Azure" = Hybrid Microsoft shop).
· **Roadmap Detection:** Identify "Preferred" skills as migration targets (e.g., "Experience with Snowflake a plus" suggests a current data migration).

**Step 2: OSINT Verification**
· Search for public indicators that confirm this stack: technical blog posts, LinkedIn skill patterns for the team, or public DNS/SaaS verification records.

**Step 3: Interview "Golden Questions"**
· Generate 3 high-level technical questions that prove you understand their specific environment and its likely pain points.

**Step 4: Scam & Red Flag Detection**
· Analyze the JD for "Kitchen Sink" requirements, financial traps, or vague, outdated tech requests.

**Step 5: Saveable Output**
· After the analysis, generate a final "Comprehensive Job & Lead Report" in a single Markdown codeblock using the [Posting-CompanyName-Position-YYYYMMDD.md] format for me to save.

**[Paste JD Text Here]**

### **[PROMPT END]**