# Operational Guide: The Career Landing Page Engine (v3.6.6)

### 1. THE ARCHITECTURAL GOAL
The "Professional Spotlight" is a **Technical Briefing**. It proves you understand the company’s **Market Friction** and provides a "B-Side" narrative. It validates depth, domain alignment, and cultural fit beyond a standard resume.

---

### 2. THE GOOGLE SITES DEPLOYMENT (LOW-FRICTION HOSTING)
Hosting on Google Sites ensures the link passes corporate email filters and security scans.

* **Step A:** Go to [sites.google.com](https://sites.google.com) and create a "Blank" site.
* **Step B:** Use the "Embed" tool -> **Embed Code** and paste the FULL HTML block.
* **Step C:** Publish using one of the **2 Suggested URL Names** (v3.6.6 strictly avoids "security" or "admin" keywords to prevent IT flags).

---

### 3. NEW FEATURE: AUTOMATED CERTIFICATION LOGIC
The engine now scans your **[CAREER PROFILE]** for industry-standard certs (e.g., CISSP, PMP, AWS).
* **The Filter:** It automatically selects the top 3 most relevant certs for the specific **[JOB SNAPSHOT]**.
* **The Placement:** These appear as styled pills in the header for immediate technical validation.

---

### 4. THE 3-COLUMN "VALUE/PROOF/ALIGNMENT" GRID
v3.6.6 restored the high-contrast layout for maximum scannability:
* **Strategic Value:** What you bring to the table (High-level).
* **Technical Proof:** Hard data and specific wins.
* **Domain Alignment:** Why you fit this specific industry friction.

---

### 5. THE WORKFLOW & "DETECTION NOTE"
The engine now requires a confirmation gate to ensure the "Brand Mirroring" and "Market Friction" are accurate before generating code.

1.  **INPUT:** Provide [JOB SNAPSHOT], [COMPANY INTEL], and [CAREER PROFILE].
2.  **DETECTION:** Review the AI’s "Detection Note" (Brand colors + Market Friction).
3.  **CONFIRM:** Once you approve, the engine outputs the URLs and the FULL HTML.
4.  **DEPLOY:** Embed the code and update your Snapshot file with the live URL.

---

### 6. THE "TABLE SETTER" (v1.8.1) INTEGRATION
Add the following tag to the absolute bottom of your `[JOB SNAPSHOT]` file:

```ini
[Career Landing Page]
URL=[https://sites.google.com/view/](https://sites.google.com/view/)[your-custom-url]

When you run the Table Setter, the AI will see this tag and weave it into your outreach as a "Technical Leave-Behind."


### Documentation Gaps Addressed:
* **The Confirmation Gate:** Added the "Detection Note" step so you know why i'm stopping to ask for permission.
* **Cert Logic:** Explained how the engine picks which certs to show (relevance vs. just listing everything).
* **URL Safety:** Documented the new rule about avoiding "security" or "admin" in URLs to stop IT departments from blocking your site.
* **Layout Specifics:** Defined the 3-column grid roles so you know what each section is doing for the hiring manager.