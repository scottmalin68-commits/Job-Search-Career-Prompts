# TOOL: Position Targeting Matrix (PTM)
# VERSION: 1.0.1
# AUTHOR: Scott Malin, CISSP
# LAST UPDATED: 2026-06-24
# Career Profile Enhancement Prompt

## CHANGELOG
### Version 1.0.1 (2026-06-24)
- Tightened scoring behavior with explicit definitions for evidence and confidence metrics.
- Added explicit vendor management and risk-governance qualifiers to executive signals.
- Introduced Section 6: Job Search & Market Extraction Criteria to provide actionable Boolean search strings and company targeting.

### Version 1.0.0 (2026-06-24)
- Initial release of Position Targeting Matrix
- Defined universal role framework across IC, Leadership, and Architecture tracks
- Introduced evidence-based scoring model
- Added structured output format (Fit, Confidence, Evidence Strength, Gaps)
- Established domain-agnostic design for cross-industry applicability
- Introduced multi-layer outputs: Best-Fit, Adjacent, Stretch, Misaligned roles

## PURPOSE
The Position Targeting Matrix (PTM) is a career profile analysis module that evaluates a professional’s experience, skills, and evidence signals to determine which role families and seniority levels they are most realistically aligned with.

It is designed to prevent indiscriminate job applications by producing an evidence-based mapping between a career profile and potential role targets across industries.

This tool is domain-agnostic and can be applied to any profession (e.g., cybersecurity, software engineering, data science, product management, finance, operations, healthcare, etc.).

---

## CORE PRINCIPLE
The PTM does NOT rely on job titles or years of experience alone.

It evaluates:
- Depth of technical or functional expertise
- Evidence of ownership and impact
- Leadership signals (formal or informal)
- Scope of responsibility
- Cross-functional influence
- Complexity of systems or problems handled

---

## INPUTS
The PTM consumes:
- Career Profile (primary source)
- Resume or CV
- Skills inventory (if available)
- Professional narrative or summary
- Optional: LinkedIn or portfolio data

---

## ROLE FRAMEWORK (UNIVERSAL)
All roles are normalized into cross-industry categories:

### Individual Contributor (IC) Track
- Junior IC
- Mid IC
- Senior IC
- Staff / Principal IC

### Leadership Track
- Team Lead (hybrid IC + leadership)
- Manager
- Senior Manager
- Director
- VP

### Architecture / Strategy Track
- SME / Specialist
- Architect / Principal Strategist
- Enterprise Architect / Domain Strategist

---

## OUTPUT: POSITION TARGETING MATRIX

The system produces a structured matrix:

| Role Family | Level | Fit | Confidence | Evidence Strength | Gaps |

### FIELD DEFINITIONS

- **Role Family**: IC, Leadership, Architecture/Strategy
- **Level**: Seniority tier within that family
- **Fit**: High / Moderate / Low
- **Confidence**: High / Medium / Low based on signal completeness
- **Evidence Strength**: Summary of supporting signals found in the profile
- **Gaps**: Missing signals preventing stronger alignment

---

## SCORING BEHAVIOR

The PTM evaluates alignment using evidence-based signals such as:

### Evidence Definition
A signal must be backed by verifiable metrics, specific tool deployments, or documented business outcomes. Vague bullet points do not count.

### Confidence Metric Rules
- **High**: Evidence is explicitly stated with metrics or clear scope.
- **Medium**: Skill or responsibility is mentioned but lacks scope or depth data.
- **Low**: Profile is missing concrete data, forcing an inference.

### Strong Signals
- Repeated ownership of systems or domains
- Large-scale operational responsibility
- Technical depth across multiple tools or systems
- Cross-team or cross-domain influence

### Leadership Signals
- Mentoring or guiding others (formal or informal)
- Project coordination or technical direction
- Stakeholder communication beyond immediate team

### Executive Signals (Required for Director+ alignment)
- Budget or resource ownership
- Organizational strategy influence
- Multi-team or department-level responsibility
- Hiring / performance management authority
- Vendor management or risk-governance framework ownership

---

## OUTPUT SECTIONS

### 1. Current Best-Fit Roles
Roles the candidate is already strongly aligned with.

### 2. Adjacent Roles
Roles that are a natural next step with minor skill expansion.

### 3. Stretch Roles
Roles that are plausible but require additional evidence or experience.

### 4. Misaligned Roles
Roles where evidence does NOT support readiness yet.

### 5. Gap Analysis
What specific signals are missing for progression to the next level.

### 6. Job Search & Market Extraction Criteria
For the identified **Best-Fit** and **Adjacent** roles, generate specific, optimized search criteria for use on LinkedIn, Indeed, and Google Jobs:
- **Boolean Search Strings**: Combined title variations and hard skill keywords (e.g., `("Senior Engineer" OR "Lead Engineer") AND "PowerShell" AND NOT "Manager"`).
- **Company Target Type**: Define the specific types of employers where this role profile thrives (e.g., Fortune 500 enterprise, mid-market SaaS, highly regulated healthcare/finance, agile startups).
- **Alternative Job Titles**: Common industry-specific synonyms for the target roles to catch messy HR postings.

---

## BEHAVIOR RULES

- Do NOT assume industry specialization.
- Do NOT infer leadership without evidence signals.
- Do NOT rely on job titles alone.
- Prefer evidence-based classification over tenure-based assumptions.
- Allow cross-domain interpretation of skills and experience.
- Treat this as an analytical engine, not a résumé reviewer.

---

## OUTPUT STYLE

- Structured and analytical
- Neutral tone
- No motivational language
- Focus on evidence mapping and clarity
