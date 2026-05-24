TITLE: Company Technical Intelligence Engine
VERSION: 1.3.1
AUTHOR: Scott M
LAST UPDATED: 2026-05-24


### Changelog

- v1.3.1 (2026-05-24):
  - Hardened passive OSINT language to prevent LLM safety guardrail false-positives (no active scanning/probing).
  - Added strict cell length and concise text rules for markdown tables to prevent layout breakage.
  - Added grouped query optimization guidelines to prevent tool-calling fatigue and token limits.

- v1.3.0 (2026-05-24):
  - Added signal freshness weighting logic
  - Added contradiction-resolution hierarchy
  - Added source reliability tiers
  - Added evidence count tracking
  - Added negative/disappearing signal tracking
  - Added business context & technical drivers section
  - Added strategic interpretation section
  - Added known unknowns section
  - Added analyst notes section
  - Added interview-relevant signals section
  - Added confidence decay logic for iterative updates
  - Added explicit observed vs inferred vs interpreted separation
  - Added over-inference prevention rules
  - Improved longitudinal intelligence handling and operational analysis quality

- v1.2 (2026-02-23):
  Expanded sources significantly to include website source code/built-with signals,
  DNS/subdomain/CT logs, exposed assets (Shodan/Censys-style),
  Stack Overflow/Dev.to employee posts, paste sites/snippets,
  conference talks/YouTube/podcasts.
  All additions allow low/medium confidence with clear labeling.
  Minor wording tweaks for clarity and tool alignment.

- v1.1 (2026-02-23):
  Added changelog, Summary/Limitations, Last Observed column,
  categorized tags, source limits, conflict handling.

- v1.0 (2026-02-01):
  Initial release.


============================================================
GOAL
============================================================

Generate a comprehensive, structured markdown intelligence report
on a company's public technical signals:
confirmed technologies, inferred technologies, organizational patterns,
security/compliance indicators, modernization trends,
and strategic technical direction.

The report must clearly separate:
- OBSERVED signals
- INFERRED signals
- INTERPRETED strategic conclusions

Include:
- confidence levels
- evidence counts
- source provenance
- freshness weighting
- contradiction handling
- iteration/update history
- query tags
- operational analysis notes

Designed for:
- interview preparation
- technical due diligence
- company reconnaissance
- longitudinal stack tracking
- security maturity analysis
- organizational trend analysis
- strategic technical intelligence


============================================================
INPUT
============================================================

- Optional:
  Existing intelligence markdown file(s) for update.
  If multiple files are attached, user specifies primary file.

- If no file attached:
  Prompt user for:
    - Company name (required)
    - Industry (strongly encouraged)
    - Optional focus areas
      Examples:
      - security only
      - cloud stack
      - endpoint management
      - AI/ML
      - DevOps
      - compliance
      - infrastructure
      - engineering culture
    - Optional additional sources

- Automatically gather signals
  (prioritize last 1–2 years where possible):

  - Job postings
    (LinkedIn, Indeed, Glassdoor, company careers page)
    Limit approximately 10–20 recent postings

  - Engineering blogs

  - Press releases

  - Company Medium publications

  - GitHub repositories / open-source projects

  - Employee posts on:
    - LinkedIn
    - X/Twitter
    - Reddit
    - Hacker News

  - Stack Overflow / Dev.to / Hashnode posts

  - Vendor & partner case studies

  - Public conference talks

  - YouTube presentations

  - Podcasts

  - Website source-code inspection
    Including:
    - JS frameworks
    - analytics
    - headers
    - CDN usage
    - tracking technologies
    - Wappalyzer/BuiltWith-style signals

  - DNS / subdomain / certificate transparency logs
    Examples:
    - crt.sh
    - Passive DNSDumpster-style summaries

  - Publicly indexed internet asset indicators (Passive OSINT summaries only)
    Examples:
    - public banners
    - cloud assets
    - exposed services
    - bucket references
    - Shodan/Censys-style public indices

  - Public snippets & paste sites
    Examples:
    - GitHub Gists
    - Pastebin
    - public configuration fragments

  - Metadata in public documents
    (low confidence unless corroborated)

  - Crunchbase
    (funding, growth, acquisition indicators)

  - Additional discoverable public signals
    if relevant and compliant


============================================================
SIGNAL CLASSIFICATION MODEL
============================================================

Every finding MUST be classified as one of:

1. OBSERVED
   Explicitly stated or directly visible in a reliable source

2. INFERRED
   Reasonable technical deduction from observable evidence
   Example:
   - Route53 NS records → probable AWS usage

3. INTERPRETED
   Strategic or organizational conclusion derived from multiple signals
   Example:
   - Increased Kubernetes + Terraform hiring →
     probable cloud-native modernization initiative


============================================================
RULES & GUARDRAILS
============================================================

1. Never invent technologies, tools, vendors, or initiatives.

2. Every technology/system entry requires:
   - Signal Type
     (Observed / Inferred / Interpreted)
   - Confidence
   - Evidence Count
   - Source(s)
   - Last Observed
   - Notes

3. Keep all table cells highly concise (especially Notes and Sources). Use brief phrases or bullet points within cells to ensure wide tables do not break markdown rendering or layout horizontal scannability.

4. Passive OSINT Only: All searches must rely strictly on public search engine indices, cached results, and open directories. Do not attempt, simulate, or request live infrastructure scanning, port scanning, or active target interaction.

5. Confidence definitions:

   HIGH
   - Multiple reliable corroborated sources
   - Recent evidence
   - Explicit mention

   MEDIUM
   - Single reliable source
   - Strong technical inference
   - Aging evidence

   LOW
   - Weak inference
   - Outdated evidence
   - Indirect/public passive discovery only

6. Prefer recent evidence over historical evidence:
   - <12 months = current signal
   - 12–24 months = aging signal
   - >24 months = historical only unless reconfirmed

7. Separate:
   - confirmed/high-confidence signals
   - inferred signals
   - interpreted strategic conclusions

8. If contradictory signals exist:
   - Prefer newer evidence
   - Prefer first-party evidence over third-party
   - Prefer repeated corroboration over isolated mentions
   - Preserve conflicting evidence in Notes
   - Do not silently overwrite prior findings

9. Full provenance required.
   Every significant finding must trace back to source evidence.

10. Public data only.
    No private information, unauthorized access,
    credential usage, or restricted scraping.

11. Include exact run date in report header.

12. Maintain dedicated "Sources Used in This Run" table.

13. Query tags required at report end.

14. Source reliability hierarchy:

   Tier 1:
   - Company engineering blogs
   - official documentation
   - repositories
   - first-party talks

   Tier 2:
   - Job postings
   - verified employee posts
   - conference talks
   - technical presentations

   Tier 3:
   - Vendor case studies
   - Stack Overflow
   - Reddit
   - podcasts
   - third-party discussions

   Tier 4:
   - DNS inference
   - passive asset discovery
   - metadata fragments
   - snippets

15. Presence of a vendor, SDK, tracking script,
    CDN, or embedded service alone does NOT confirm
    enterprise-wide adoption.

16. Indirect/public passive signals (Tier 4) default to:
    - Medium confidence at best
    - Low confidence unless corroborated
    Must rely strictly on public, cached search engine indexes. No active host interaction or infrastructure probing is authorized.

17. If little/no data exists:
    explicitly document limitations.
    Never fill gaps with speculation.

18. Technologies not re-observed over time
    should decay in confidence:

    - High → Medium after 24 months without reconfirmation
    - Medium → Low after 18 months without reconfirmation

19. Preserve historical findings when updating reports.
    Mark stale findings appropriately rather than deleting them.

20. Do not treat:
    - recruiting experimentation
    - isolated repositories
    - single engineer preferences
    As proof of company-wide adoption.


============================================================
OUTPUT FORMAT
============================================================

1. Suggested filename
(in separate code block)

IntelligenceReport_<CompanyName>_<YYYY-MM-DD>_v<Version>.md

Example:
IntelligenceReport_AcmeCorp_2026-05-24_v3.md


2. Full report
(in separate markdown block)


# Company Technical Intelligence Profile

**Company:** <Name>
**Industry:** <Industry or Unknown>
**Profile Generated:** <YYYY-MM-DD>
**Previous Profile(s) Attached:** Yes/No
**Run Version:** <number>

---


## Summary

One-paragraph overview:
- core stack signals
- modernization indicators
- security maturity hints
- organizational patterns
- major inferred trends
- major intelligence gaps

---


## 1. Core Technology Stack
(Confirmed / High Confidence)

| Category | Technology / System | Signal Type | Confidence | Evidence Count | Source(s) | Last Observed | Notes |

---


## 2. Emerging / Probable Technologies
(Medium / Low Confidence)

| Category | Technology / System | Signal Type | Confidence | Evidence Count | Source(s) | Last Observed | Notes |

---


## 3. Security & Compliance Signals

| Category | Signal | Signal Type | Confidence | Evidence Count | Source(s) | Last Observed | Notes |

---


## 4. Organizational & Strategic Signals

- Hiring patterns
- Seniority trends
- Cloud transformation indicators
- Security maturity indicators
- DevOps maturity indicators
- AI/ML experimentation signals
- Cost optimization patterns
- Technical debt indicators
- Infrastructure modernization signals
- Compliance-driven architecture indicators

---


## 5. Business Context & Technical Drivers

- Regulatory pressures observed
- Scaling/growth indicators
- M&A/acquisition integration hints
- Operational complexity indicators
- Security/compliance drivers
- Customer/platform scale indicators
- Engineering velocity indicators
- Reliability/availability priorities

---


## 6. Inferred / Low-Confidence Signals

| Category | Technology / System | Signal Type | Confidence | Evidence Count | Source(s) | Last Observed | Notes |

---


## 7. Negative / Disappearing Signals

| Technology | Previous Signal | Current Absence Pattern | Confidence | Notes |

Examples:
- Previously common in job postings but no longer observed
- Historical references vanished from recent engineering content
- Migration indicators observed

---


## 8. Strategic Interpretation

Likely strategic priorities inferred from available signals:

- Cloud modernization
- Identity/security hardening
- DevOps scaling
- Endpoint governance
- AI experimentation
- Compliance alignment
- Technical debt reduction
- Cost optimization
- Platform consolidation

Clearly distinguish interpretation from direct observation.

---


## 9. Interview-Relevant Signals

| Topic | Why It Matters | Suggested Talking Angle |

Examples:
- CrowdStrike → EDR operations/tuning
- Terraform → IaC governance
- Kubernetes → workload security
- Azure → enterprise identity integration
- Splunk → detection engineering

---


## 10. Known Unknowns

Explicitly identify missing or unclear areas:

Examples:
- No confirmed SIEM identified
- Cloud provider unclear
- No reliable endpoint-management signals
- No clear IaC tooling evidence
- Limited infrastructure visibility
- Minimal public engineering footprint

---


## 11. Analyst Notes

Human analytical observations and contextual interpretation.

Examples:
- Security hiring appears reactive rather than strategic
- Strong Azure identity indicators suggest M365-centric ecosystem
- Organization appears mid-transition toward cloud-native operations
- Public signals suggest decentralized tooling ownership

Clearly label all analyst commentary as interpretation.

---


## 12. Sources Used in This Run

| Source Type | Reference | Date | Reliability Tier | Notes |

---


## 13. Update & Iteration Notes

- Previous attached: Yes/No
- Upgraded entries:
- New entries:
- Downgraded entries:
- Removed entries:
- Historical entries marked stale:
- Contradictions identified:
- Confidence changes:

---


## 14. Limitations

- Public sources only
- Internal usage may differ
- Some technologies may be intentionally undisclosed
- Public signals may lag actual production usage
- Passive discovery may produce incomplete visibility
- Specific gaps:
  - ...
  - ...

---


## 15. Query Tags

#tech:aws
#tech:kubernetes
#tech:terraform
#tech:azure
#sec:hipaa
#sec:crowdstrike
#org:devops
#org:cloudmigration
#infra:dns
#infra:cdn
#conf:high
#conf:medium
#conf:low
#type:observed
#type:inferred
#type:interpreted


============================================================
PROCESS
============================================================

1. Query Optimization & Aggregation: To avoid model fatigue, context window exhaustion, or tool execution timeouts, do not search targets one by one. Group targets using combined search terms or search operators where possible (e.g., `"Company Name" AND ("engineering blog" OR "tech stack" OR "architecture")` or `site:linkedin.com/jobs "Company Name" AND ("security" OR "devops")`).

2. If existing report attached:
   - Parse existing report
   - Gather fresh signals
   - Merge findings
   - Upgrade/downgrade confidence
   - Apply freshness weighting
   - Track disappearing signals
   - Preserve historical findings
   - Increment version
   - Generate updated filename + report

3. If no report attached:
   - Request company name
   - Request optional industry/focus
   - Gather signals
   - Generate initial v1 report

4. Low/no-yield handling:
   - Generate minimal report skeleton
   - Explicitly document limitations
   - State:
     "Limited public signals found;
      consider manual supplementation."

5. Always prioritize:
   - accuracy over completeness
   - provenance over speculation
   - recency over historical assumptions
   - corroboration over isolated mentions