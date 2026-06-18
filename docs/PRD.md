# Insight‑Loom — Product Requirements Document (PRD)

**Document Version**: 1.0  
**Last Updated**: 2026‑06‑18  
**Author**: Senior Product/Engineering Lead, Axentx  

---  

## 1. Overview  

**Product Name**: Insight‑Loom  
**Tagline**: *Weave scattered data into actionable insight.*  

Insight‑Loom is a SaaS platform for founders, product teams, and early‑stage executives that aggregates, structures, and analyses disparate information sources (documents, chat logs, tickets, analytics dashboards, etc.) into a unified knowledge graph. The system surfaces clear insights, trend visualisations, and concrete recommendations to accelerate decision‑making and reduce the time spent on manual information hunting.

---

## 2. Problem Statement  

Founders and high‑growth teams constantly juggle information spread across:

| Source Type | Typical Pain |
|-------------|--------------|
| Google Docs / Notion pages | Version drift, no single source of truth |
| Slack / Teams chat | Context buried in long threads |
| Issue trackers (Jira, GitHub) | Fragmented metrics, manual correlation |
| Analytics dashboards (Mixpanel, Amplitude) | Data silos, limited narrative |
| Email & external docs | Unstructured, hard to search |

**Consequences**

* Decision latency ↑ (average 3‑5 days to locate relevant context)  
* Cognitive overload → missed patterns & opportunities  
* Re‑work due to duplicated knowledge capture  
* Investor & board reporting becomes ad‑hoc and error‑prone  

**Validated Need** (from market discovery): 78 % of surveyed founders (Series A‑C) rate “centralised insight generation” as a top‑3 priority, and 62 % are willing to pay **$199‑$399 /mo** for a solution that cuts research time by ≥30 %.

---

## 3. Target Users & Personas  

| Persona | Role | Primary Goals | Pain Points |
|---------|------|---------------|-------------|
| **Founder‑Strategist** | CEO / Co‑founder | Quick, data‑backed strategic pivots | Sifting through scattered notes before board decks |
| **Product Lead** | Head of Product | Align roadmap with real user signals | Disconnected feature requests vs. usage analytics |
| **Operations Manager** | COO / Ops Lead | Streamline cross‑team knowledge flow | Duplicate SOPs, outdated process docs |
| **Data‑Curator** | Analyst / PM | Turn raw data into narratives | Manual data stitching across tools |

---

## 4. Goals & Success Metrics  

| Goal | Success Metric | Target (12 mo) |
|------|----------------|----------------|
| **Reduce information‑search time** | Avg. time to locate a specific insight (seconds) | ↓ 50 % from baseline (≈30 s → 15 s) |
| **Increase insight‑driven decisions** | % of decisions logged with an Insight‑Loom reference | ≥ 70 % |
| **Drive revenue** | Monthly Recurring Revenue (MRR) | $250 k |
| **Achieve high product‑market fit** | NPS from paying customers | ≥ 55 |
| **Maintain data security compliance** | SOC 2 Type II attestation | Achieved by Q4 2026 |

---

## 5. Key Features (Prioritized)

| Priority | Feature | Description | MVP Acceptance Criteria |
|----------|---------|-------------|--------------------------|
| **1** | **Unified Connectors** | Pre‑built, OAuth‑secured connectors for Google Workspace, Notion, Slack, GitHub, Jira, Mixpanel, Amplitude, and generic email/IM APIs. | • User can link ≥ 6 sources with 1‑click auth.<br>• Data ingestion runs nightly with <5 min latency. |
| **2** | **Knowledge Graph Engine** | Automatic entity extraction (people, projects, metrics) and relationship mapping across sources, stored in a scalable graph DB. | • ≥ 85 % entity extraction F1 on internal test set.<br>• Graph query latency <200 ms for typical queries. |
| **3** | **Insight Dashboard** | Visual canvas showing trend cards, anomaly alerts, and recommendation widgets (e.g., “Feature X usage dropping → consider A/B test”). | • Users can create & share a dashboard in ≤ 5 min.<br>• At least 3 auto‑generated recommendation types per month per active org. |
| **4** | **Natural‑Language Query** | Conversational UI (chat‑style) powered by the instruction‑response dataset to retrieve insights (“What were the top three churn reasons last quarter?”). | • 80 % of queries return correct answer within 2 turns.<br>• UI supports text & voice input. |
| **5** | **Collaboration & Annotation** | Inline comments, tagging, and versioned snapshots on any insight card; role‑based permissions. | • Teams can co‑author an insight in real‑time.<br>• Audit log records all changes. |
| **6** | **Export & Reporting** | One‑click PDF/PowerPoint export of selected insights; API endpoint for downstream BI tools. | • Exported assets retain visual fidelity and source citations. |
| **7** | **Security & Compliance Layer** | End‑to‑end encryption, SSO (SAML/OIDC), data residency options, audit trails. | • Passes internal penetration test.<br>• SOC 2 Type II audit ready. |

*Features 1‑4 are in‑scope for the MVP (launch Q3 2026). Features 5‑7 are in‑scope for Phase 2 (launch Q1 2027).*

---

## 6. Scope  

### In‑Scope (MVP)

* Connectors for the six most common sources (Google Docs, Notion, Slack, GitHub, Jira, Mixpanel).  
* Core knowledge‑graph pipeline (entity extraction, relationship mapping).  
* Insight Dashboard with auto‑generated trend cards & recommendations.  
* Conversational query interface (text only).  
* Basic role‑based access (Admin / Member).  
* Hosted SaaS deployment on AWS (us‑east‑1) with GDPR‑compliant data handling.  

### Out‑of‑Scope (Post‑MVP)

* Voice‑enabled query.  
* Deep custom connector SDK for on‑prem data sources.  
* Advanced analytics (predictive modeling, custom ML pipelines).  
* Multi‑region data residency beyond EU & US.  
* Marketplace for third‑party insight widgets.  

---

## 7. Assumptions & Dependencies  

| Assumption | Impact if Invalid |
|------------|-------------------|
| Founders will allocate 2 hrs/week to configure connectors. | Adoption friction; may need guided onboarding. |
| Existing datasets (auto, messages, instr‑resp, query‑resp) are sufficient to fine‑tune the NL query model for our domain. | Model performance may degrade; may require additional domain data. |
| AWS services (Lambda, Neptune, S3) meet latency & cost targets. | Need to evaluate alternative (GCP, Azure) or self‑hosted graph DB. |
| Legal can obtain SOC 2 Type II audit by Q4 2026. | Delay in enterprise sales; may need interim compliance statements. |

---

## 8. Milestones & Timeline  

| Milestone | Target Date | Owner |
|-----------|-------------|-------|
| **Discovery & Architecture Finalisation** | 2026‑07‑15 | Lead Architect |
| **Connector SDK & First 3 Connectors Built** | 2026‑08‑31 | Integration Team |
| **Knowledge Graph MVP (entity extraction + graph store)** | 2026‑09‑30 | ML & Backend Team |
| **Insight Dashboard UI Prototype** | 2026‑10‑15 | Front‑end Team |
| **NL Query Engine (text only) Beta** | 2026‑11‑01 | NLP Team |
| **Closed Alpha (5 pilot customers)** | 2026‑11‑30 | PM / Customer Success |
| **Public Beta Launch** | 2026‑12‑31 | PM |
| **General Availability (GA) – MVP** | 2027‑02‑28 | All Teams |
| **Phase 2 Features (Collaboration, Export, Security)** | 2027‑06‑30 | Product Roadmap |

---

## 9. Risks & Mitigations  

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Connector brittleness** (API changes break ingestion) | Medium | High (data loss) | Build versioned connector adapters; automated regression tests on API schemas. |
| **NL query accuracy insufficient** | Medium | Medium | Leverage existing instruction‑response dataset; fine‑tune with active learning loop from pilot feedback. |
| **Data privacy concerns** (founders reluctant to grant access) | Low | High | Transparent permission model; allow selective source sync; obtain SOC 2 audit. |
| **Performance bottleneck in graph queries** | Medium | Medium | Use AWS Neptune with auto‑scaling; benchmark early; fallback to materialised views for heavy queries. |
| **Market overlap with existing knowledge‑base tools** | Low | Medium | Emphasise cross‑source synthesis & automated recommendations – not just storage. |

---

## 10. Acceptance Criteria (MVP)

1. **Onboarding** – New org can connect at least three data sources in ≤ 5 minutes, with no manual token handling.  
2. **Data Freshness** – Ingested data is no older than 15 minutes for real‑time sources (Slack, Jira).  
3. **Insight Generation** – System surfaces ≥ 2 actionable insights per week per active user (e.g., trend, anomaly, recommendation).  
4. **Query Accuracy** – 80 % of natural‑language queries return a correct answer within two conversational turns.  
5. **Performance** – Dashboard loads < 3 seconds; graph query latency < 200 ms.  
6. **Security** – All data encrypted at rest & in transit; role‑based access enforced.  
7. **Reliability** – 99.5 % uptime SLA for core services during GA.  

---

## 11. Appendices  

### A. Glossary  

* **Entity** – A distinct object extracted from source data (e.g., *User*, *Feature*, *Metric*).  
* **Insight Card** – UI component summarising a trend, anomaly, or recommendation.  
* **NL Query** – Natural‑language request processed by the instruction‑response model.  

### B. Reference Datasets  

| Dataset | Size | License |
|---------|------|---------|
| `auto` | 17,933,967 pairs | Mixed |
| `messages` | 6,806,519 pairs | Apache‑2.0, MIT |
| `instr‑resp` | 6,387,449 pairs | Apache‑2.0, CDLA‑Permissive‑2.0, MIT |
| `query‑resp` | 2,091,470 pairs | Apache‑2.0, MIT |

These will be used to pre‑train and continuously improve the NL query engine.  

---  

*Prepared for internal review and alignment across Axentx product, engineering, and go‑to‑market teams.*
