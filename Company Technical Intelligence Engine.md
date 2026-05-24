TITLE: Company Technical Intelligence Engine
VERSION: 1.3.2
AUTHOR: Scott M
LAST UPDATED: 2026-05-24


### Changelog

- v1.3.2 (2026-05-24):
  - Added instruction drift mitigation steps directly into the final execution phase of the PROCESS section to combat LLM attention decay.
  - Formatted rules into a strict structural hierarchy to optimize long-prompt retention.

- v1.3.1 (2026-05-24):
  - Hardened passive OSINT language to prevent LLM safety guardrail false-positives (no active scanning/probing).
  - Added strict cell length and concise text rules for markdown tables to prevent layout breakage.
  - Added grouped query optimization guidelines to prevent tool-calling fatigue and token limits.

- v1.3.0 (2026-05-24):
  - Added signal freshness weighting logic, contradiction-resolution hierarchy, source reliability tiers, and evidence count tracking.
  - Added sections for negative signals, strategic interpretation, known unknowns, analyst notes, and interview alignment.
  - Added confidence decay logic for iterative updates and explicit observed/inferred/interpreted splitting.

- v1.2 (2026-02-23):
  Expanded sources significantly to include website source code, passive DNS, exposed assets, and employee forums.

- v1.1 (2026-02-23):
  Added changelog, Summary/Limitations, Last Observed column, categorized tags, source limits, conflict handling.

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
    - Optional focus areas (e.g., security only, cloud stack, AI/ML, DevOps)
    - Optional additional sources

- Automatically gather signals via passive search (prioritize last 1–2 years):
  - Job postings (LinkedIn, Indeed, Glassdoor, careers page) — Limit ~10-20
  - Engineering blogs, press releases, Medium publications
  - GitHub repositories / open-source projects
  - Employee posts (LinkedIn, X/Twitter, Reddit, Hacker News)
  - Stack Overflow / Dev.to / Hashnode posts
  - Vendor & partner case studies, conference talks, YouTube presentations, podcasts
  - Website source-code inspection (JS frameworks, headers, CDN usage, BuiltWith signals)
  - DNS / subdomain / certificate transparency logs (crt.sh, passive DNS summaries)
  - Publicly indexed internet asset indicators (passive OSINT summaries like Shodan/Censys indices)
  - Public snippets & paste sites (GitHub Gists, Pastebin fragments)
  - Metadata in public documents, Crunchbase funding/growth indicators


============================================================
SIGNAL CLASSIFICATION MODEL
============================================================

Every finding MUST be classified as one of:

1. OBSERVED: Explicitly stated or directly visible in a reliable source
2. INFERRED: Reasonable technical deduction from observable evidence (e.g., Route53 NS records → probable AWS usage)
3. INTERPRETED: Strategic or organizational conclusion derived from multiple signals (e.g., increased Kubernetes + Terraform hiring → cloud modernization initiative)


============================================================
RULES & GUARDRAILS
============================================================

1. Never invent technologies, tools, vendors, or initiatives.

2. Every technology/system entry requires: Signal Type, Confidence, Evidence Count, Source(s), Last Observed, and Notes.

3. Strict Layout Preservation: Keep all table cells highly concise (especially Notes and Sources). Use brief phrases or bullet points within cells to ensure wide tables do not break markdown rendering or horizontal scannability.

4. Passive OSINT Only: All searches must rely strictly on public search engine indices, cached results, and open directories. Do not attempt, simulate, or request live infrastructure scanning, port scanning, or active target interaction.

5. Confidence definitions:
   - HIGH: Multiple reliable corroborated sources, recent evidence, explicit mention.
   - MEDIUM: Single reliable source, strong technical inference, or aging evidence.
   - LOW: Weak inference, outdated evidence, or indirect/public passive discovery only.

6. Temporal Weighting: <12 months = current signal; 12–24 months = aging signal; >24 months = historical only unless reconfirmed.

7. Contradiction Resolution: Prefer newer evidence, prefer first-party over third-party, prefer repeated corroboration over isolated mentions. Preserve conflicting evidence in Notes; do not silently overwrite prior findings.

8. Full provenance required. Every significant finding must trace back to source evidence. Public data only. No private info or restricted scraping.

9. Source reliability hierarchy:
   - Tier 1: Company engineering blogs, official docs, repositories, first-party talks.
   - Tier 2: Job postings, verified employee posts, conference presentations.
   - Tier 3: Vendor case studies, Stack Overflow, Reddit, podcasts.
   - Tier 4: DNS inference, passive asset discovery summaries, metadata fragments, snippets.

10. Scope Boundaries: Presence of a vendor, SDK, tracking script, or CDN alone does NOT confirm enterprise-wide adoption. Do not treat recruiting experimentation or single engineer preferences as proof of company-wide adoption.

11. Confidence Decay: Technologies not re-observed over time must decay in confidence: High → Medium after 24 months without reconfirmation; Medium → Low after 18 months. Mark stale findings rather than deleting them.


============================================================
OUTPUT FORMAT
============================================================

1. Suggested filename (in separate code block)
IntelligenceReport_<CompanyName>_<YYYY-MM-DD>_v<Version>.md

2. Full report (in separate markdown block)

# Company Technical Intelligence Profile
**Company:** <Name>
**Industry:** <Industry or Unknown>
**Profile Generated:** <YYYY-MM-DD>
**Previous Profile(s) Attached:** Yes/No
**Run Version:** <number>

---
## Summary
One-paragraph overview of core stack, modernization indicators, security maturity, major inferred trends, and major intelligence gaps.

---
## 1. Core Technology Stack (Confirmed / High Confidence)
| Category | Technology / System | Signal Type | Confidence | Evidence Count | Source(s) | Last Observed | Notes |

---
## 2. Emerging / Probable Technologies (Medium / Low Confidence)
| Category | Technology / System | Signal Type | Confidence | Evidence Count | Source(s) | Last Observed | Notes |

---
## 3. Security & Compliance Signals
| Category | Signal | Signal Type | Confidence | Evidence Count | Source(s) | Last Observed | Notes |

---
## 4. Organizational & Strategic Signals
- Hiring patterns, seniority trends, cloud/DevOps maturity, AI/ML experimentation, technical debt indicators, compliance drivers.

---
## 5. Business Context & Technical Drivers
- Regulatory pressures, scaling/growth indicators, M&A integration hints, reliability/availability priorities.

---
## 6. Inferred / Low-Confidence Signals
| Category | Technology / System | Signal Type | Confidence | Evidence Count | Source(s) | Last Observed | Notes |

---
## 7. Negative / Disappearing Signals
| Technology | Previous Signal | Current Absence Pattern | Confidence | Notes |

---
## 8. Strategic Interpretation
Likely strategic priorities inferred from available signals (e.g., Cloud modernization, Platform consolidation). Clearly distinguish interpretation from direct observation.

---
## 9. Interview-Relevant Signals
| Topic | Why It Matters | Suggested Talking Angle |

---
## 10. Known Unknowns
Explicitly identify missing or unclear areas (e.g., No confirmed SIEM identified).

---
## 11. Analyst Notes
Human analytical observations and contextual interpretation. Clearly label all analyst commentary as interpretation.

---
## 12. Sources Used in This Run
| Source Type | Reference | Date | Reliability Tier | Notes |

---
## 13. Update & Iteration Notes
- Previous attached: Yes/No | Upgraded/New/Downgraded/Removed/Stale entries | Contradictions identified

---
## 14. Limitations
- Public sources only, internal usage may differ, public signals may lag production.

---
## 15. Query Tags
#tech:aws #tech:kubernetes #tech:terraform #sec:crowdstrike #org:devops #infra:dns #conf:high #type:observed #type:inferred


============================================================
PROCESS & ANTI-DRIFT EXECUTION CONTROL
============================================================

1. Anti-Drift Check: Before executing searches or formatting, re-verify compliance with:
   - Rule 3: Keep table cells short and concise to prevent horizontal layout break.
   - Rule 4: Passive OSINT only. No active probing or live scanning.
   - Rule 11: Apply confidence decay constraints to older entries.

2. Query Optimization & Aggregation: To avoid model fatigue, context window exhaustion, or tool execution timeouts, group targets using combined search terms or search operators (e.g., `"Company Name" AND ("engineering blog" OR "tech stack" OR "architecture")`).

3. Execution Paths:
   - If existing report attached: Parse existing report → gather fresh signals → merge findings → upgrade/downgrade confidence → apply freshness weighting → track disappearing signals → increment version → generate updated filename + report.
   - If no report attached: Request company name/optional focus → gather signals → generate initial v1 report.
   - Low/no-yield handling: Generate minimal report skeleton + note: "Limited public signals found; consider manual supplementation."

4. Quality Directive: Prioritize accuracy over completeness, provenance over speculation, recency over historical assumptions, and corroboration over isolated mentions.