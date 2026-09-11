# Operational Guide: The Career Landing Page Engine (v4.0.3)

### 1. THE ARCHITECTURAL GOAL
The "Professional Spotlight" is a **Technical Briefing**. It proves you understand the company’s **Market Friction** and provides a "B-Side" narrative. It validates depth, domain alignment, and cultural fit beyond a standard resume.

---

### 2. THE GOOGLE SITES DEPLOYMENT (LOW-FRICTION HOSTING)
Hosting on Google Sites ensures the link passes corporate email filters and security scans.

* **Step A:** Go to sites.google.com and create a "Blank" site.
* **Step B:** Use the "Embed" tool -> **Embed Code** and paste the FULL HTML block.
* **Step C:** Publish using one of the **2 Suggested URL Names** (v4.0.3 strictly avoids "security" or "admin" keywords to prevent IT flags).

---

### 3. THE AUTOMATED CERTIFICATION LOGIC
The engine scans your **[CAREER_PROFILE]** for professional certifications (e.g., CISSP, CEH).
* **The Filter:** It automatically selects up to the 3 most relevant certs for the specific **[JOB_SNAPSHOT]**.
* **The Placement:** These appear as styled pills right in the header for immediate validation.

---

### 4. THE 3-COLUMN "VETERAN FILTER" GRID
The layout enforces high-contrast cards for maximum scannability:
* **Strategic Value:** High-level impact and core value.
* **Technical Proof:** Focuses on raw execution and results. Uses the "Zero Patience for BS" tone.
* **Domain Alignment:** Why this specific background solves the identified friction.

---

### 5. THE STRATEGIC ALIGNMENT SECTION
An expanded 2-column comparison component. It maps Company Needs against your Functional Delivery based on 3-4 critical strategic pillars (like Compliance Automation, Cloud Migration, or Scalability) identified during the tech recon phase.

---

### 6. THE JOB FIT MATRIX (ENHANCED IN v4.0.3)
A high-density data table running explicit mathematical calculations across four weighted components:
* **Responsibilities Alignment (30% Weight):** `(Matched Core Duties / Total Required Duties) * 30`
* **Required Qualifications (30% Weight):** `(Matched Required Qualifications / Total Required Qualifications) * 30`
* **Preferred Qualifications (15% Weight):** `(Matched Preferred Qualifications / Total Preferred Qualifications) * 15`
* **Skills/Tech/Edu (25% Weight):** `(Matched Technical Skills & Credentials / Total Listed Skills) * 25`

It includes a Match %, Alignments/Gaps, and a Confidence rating. 
* **The Anchor:** The matrix has no header label and **must** conclude with a final, highlighted summary row calculating the Overall Weighted Fit (100%).

---

### 7. EDGE CASES & INPUT VALIDATION (NEW IN v4.0.3)
The engine actively defends against dirty data or malicious prompt manipulation:
* **Missing/Incomplete Data:** Halts execution gracefully and requests missing `[JOB_SNAPSHOT]` or `[CAREER_PROFILE]` parameters before generating invalid code.
* **Jailbreak Defenses:** Ignores instructions to modify core system rules or output non-career web artifacts.
* **Garbage Inputs:** Triggers a specific error message if unparseable noise or non-career text is submitted.

---

### 8. APPROVED AI USE DECLARATION (NEW IN v4.0.3)
* **Permitted Roles:** Structural semantic analysis, technical skill mapping, cross-referencing experience vectors, and generating compliant HTML/CSS artifacts.
* **Strict Guardrails:** Banned from inventing false career accomplishments, fabricating match percentages, using marketing fluff, or retaining user context post-execution.

---

### 9. DATA LEAK PROTECTION & FOOTER RIGIDITY
v4.0.3 strictly bans placeholder strings (like "example.com"). The engine is forced to pull exact, real-world communication channels (GitHub, Phone, Email) directly from your **[CONTACT_INFO]** or **[CAREER_PROFILE]** inputs. The `<footer>` and closing `</html>` tags are non-negotiable and cannot be truncated.

---

### 10. THE SINGLE-PASS WORKFLOW
v4.0.3 executes all steps in a single-pass response without pausing:

1. **DETECTION NOTE:** Brief analysis using the Industry Veteran tone to pinpoint real, in-the-trenches market friction and brand colors.
2. **SITES METADATA:** Outputs 2 safe suggested URLs and the Page Name.
3. **FULL HTML DOCUMENT:** Production-ready code in one block, embedding exact contact channels and dynamic metadata. Uses inline fallback CSS/tables if Markdown or layout framework formatting degrades.
4. **THE UPDATE TAG:** Provides the final tracking snippet.

---

### 11. TRACKING INTEGRATION
Add this tag to the bottom of your tracking file once generated:

[Career Landing Page]
URL=https://sites.google.com/view/[your-custom-url]

When you run the Table Setter, the AI will see this tag and weave it into your outreach as a "Technical Leave-Behind."