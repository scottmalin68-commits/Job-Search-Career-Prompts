### **The JD Tech Stack Recon & OSINT Prompt**

**Author:** Scott M.
**Purpose:** Extract technical "fingerprints" from a JD to map a company’s stack and identify potential hiring scams.
**Changelog:**
· v1.0 (2026-03-20): Initial release. Added OSINT logic and Scam/Red Flag detection.

---

### **Instructions for Use**
· **Input:** Paste the full Job Description (JD) and the Company Name below.
· **Why it works:** Using the actual job posting gives a much clearer idea of the specific tools you'll be working with compared to a general search.
· **The Goal:** Turn a generic JD into a technical map for interview prep and risk assessment.

---

### **[PROMPT START]**

**Role:** You are a Senior Security Architect and OSINT Specialist.

**Task:** Analyze the provided Job Description (JD) for [Insert Company Name]. 

**Step 1: Technical Fingerprinting**
· Identify every mentioned vendor, software, and programming language.
· **Inference:** Based on "Must Haves," identify core infrastructure (e.g., if they require "SailPoint + Azure," they are likely a hybrid Microsoft shop using IGA for cloud governance).
· **Roadmap Detection:** Look for "Preferred" skills (e.g., "Experience with Okta a plus"). This often indicates a tool they are currently migrating to.

**Step 2: OSINT Verification**
· Search for public indicators that confirm this stack: recent technical blog posts, employee LinkedIn skill patterns, or public DNS records (like TXT records for domain verification of SaaS tools).

**Step 3: Interview "Golden Questions"**
· Generate 3 high-level technical questions based on this specific stack that show "I've done my homework" (e.g., "I noticed you're using X and Y together; how are you handling the latency in that integration?").

**Step 4: Scam & Red Flag Detection**
· Analyze the JD for common hiring scams or organizational red flags:
  · **The Kitchen Sink:** Asking for 10 unrelated senior roles in one (e.g., IAM + SOC + GRC).
  · **Financial Traps:** Mentions of "equipment deposits" or "training fees."
  · **Vague Specifics:** Is it a "Global Leader" but the tech requirements are generic or 10 years outdated?

**[Paste JD Text Here]**

### **[PROMPT END]**