# Business Model Canvas – insight‑loom
*Version 1.0 – June 2026*  

---  

## 1. Value Proposition
| What we deliver | How it solves a pain point | Measurable benefit |
|-----------------|----------------------------|--------------------|
| **Unified knowledge hub** – ingest documents, Slack/Discord threads, emails, tickets, and code‑review comments into a single searchable graph. | Founders spend > 30 % of their time locating context; we eliminate manual hunting. | ↓ time‑to‑insight by ≈ 70 % (validated in pilot). |
| **AI‑driven synthesis** – LLM‑powered summarisation, trend detection, and recommendation engine (built on vLLM + SGLang). | Raw data is noisy; our structured generation surfaces actionable signals. | ↑ decision‑quality score (internal metric) by ≥ 25 %. |
| **Collaborative insight workspaces** – real‑time annotation, voting, and “insight cards” that can be exported to road‑maps or investor decks. | Teams struggle to align on what the data actually means. | ↑ team alignment (survey NPS + 15). |
| **Compliance‑ready audit trail** – immutable provenance metadata for every ingested artifact. | Investors & regulators demand traceability. | ↓ audit‑prep effort by ≈ 80 %. |

---

## 2. Customer Segments
| Primary Segment | Characteristics | Pain |
|-----------------|----------------|------|
| **Seed & Series‑A founders** | 1‑20 employees, data scattered across tools, limited analyst resources. | Need fast, low‑cost insight to guide product/market fit. |
| **Product & Growth teams** (PM, growth marketers) | Mid‑size SaaS, multiple data sources (analytics, support, sales). | Require unified view to prioritize experiments. |
| **VC‑backed incubators / accelerators** | Run multiple startups, provide shared services. | Want a turnkey insight platform for portfolio companies. |
| **Compliance‑focused fintech & health‑tech** | Regulated data, heavy audit requirements. | Need provable data lineage and secure storage. |

*Total addressable market (TAM) ≈ US $12 B (founder tools + analytics market).*  

---

## 3. Channels
| Channel | Tactics | KPI |
|---------|---------|-----|
| **Direct sales (self‑serve SaaS)** | Free tier → upgrade via in‑app prompts; targeted LinkedIn ads. | CAC ≤ $150, conversion free→paid 5 % within 30 days. |
| **Partner ecosystem** | Integration partners (Notion, Linear, Slack, HubSpot) – co‑marketing & bundled offers. | Partner‑generated ARR ≥ 20 % of total. |
| **Accelerator programs** | Offer “founder‑first” seats, mentorship sessions, and API credits. | 10 % of accelerator cohorts adopt within 6 mo. |
| **Content & community** | Blog series “Insight‑Loom Playbooks”, webinars, open‑source SDK. | Organic traffic → trial sign‑ups > 2 k/mo. |
| **Enterprise sales** (later stage) | Dedicated account execs, custom SLAs, on‑prem deployment. | Average contract value (ACV) $45k/year. |

---

## 4. Revenue Streams
| Stream | Pricing Model | Rationale |
|--------|---------------|-----------|
| **Subscription SaaS** | Tiered plans: Free (5 GB, 1 workspace), Pro ($29/mo per user, 50 GB), Team ($99/mo per user, 200 GB, admin console), Enterprise (custom). | Recurring, predictable cash flow; aligns with team size. |
| **Usage‑based add‑ons** | Extra AI inference credits ($0.002 per 1 k tokens), additional storage ($0.10/GB/mo). | Monetise high‑volume customers while keeping base price low. |
| **Professional Services** | On‑boarding, data‑migration, custom insight models ($150/hr). | Capture value from complex integrations & compliance setups. |
| **Marketplace extensions** | Third‑party “Insight cards” templates sold via marketplace (revenue share 70/30). | Ecosystem growth & incremental revenue. |
| **Data‑license (optional)** | Aggregated, anonymised trend datasets sold to market‑research firms (opt‑in). | New B2B stream, fully compliant with GDPR/CCPA. |

*Target ARR in Year 1: $3.2 M; Year 3: $18 M.*

---

## 5. Cost Structure
| Category | Main Cost Drivers | % of OPEX |
|----------|-------------------|-----------|
| **Cloud infrastructure** (compute for vLLM inference, storage for ingested data) | GPU instances (AWS/GCP), object storage, CDN. | 35 % |
| **R&D & engineering** | Salaries (ML, backend, UI), open‑source contributions, licensing of SGLang/vLLM. | 30 % |
| **Sales & Marketing** | Paid ads, partner commissions, events, content creation. | 20 % |
| **Compliance & security** | Audits, SOC2/ISO certifications, data‑encryption tooling. | 8 % |
| **General & Admin** | HR, legal, office, utilities. | 7 % |

*Break‑even point projected at 12 months with 4,500 paid seats.*

---

## 6. Key Resources
| Resource | Description |
|----------|-------------|
| **AI inference stack** – vLLM (high‑throughput LLM serving) + SGLang (structured generation). |
| **Knowledge graph engine** – custom graph DB built on PostgreSQL + pgvector for semantic search. |
| **Data pipelines** – connectors for Slack, Gmail, Notion, GitHub, JIRA, CSV/JSON imports. |
| **Product team** – PM, senior full‑stack engineers, ML scientists, UX designers. |
| **Brand & community** – founder‑focused content hub, open‑source SDK (npm, PyPI). |
| **Compliance framework** – ISO‑27001 certified cloud tenancy, audit‑trail module. |

---

## 7. Key Activities
| Activity | Frequency / Owner |
|----------|-------------------|
| **Data ingestion & normalization** | Continuous, automated connectors (engineer). |
| **Model training & fine‑tuning** (domain‑specific summarisation) | Quarterly (ML team). |
| **Feature rollout & A/B testing** | Bi‑weekly (PM & dev). |
| **Customer success & onboarding** | Ongoing (CS team). |
| **Partner integration development** | Ongoing (partner engineering). |
| **Compliance monitoring & security patches** | Monthly (SecOps). |
| **Community building & content production** | Weekly (Marketing). |

---

## 8. Key Partners
| Partner | Role |
|---------|------|
| **GPU Cloud providers** (AWS, GCP, Azure) | Scalable inference compute, reserved instance discounts. |
| **Collaboration platforms** (Slack, Microsoft Teams, Notion, Linear) | Native connectors, co‑marketing. |
| **Accelerators / VC funds** (Y Combinator, Techstars) | Early‑adopter pipeline, credibility boost. |
| **Open‑source communities** (vLLM, SGLang) | Continuous improvements, talent pool. |
| **Compliance auditors** (SOC2, ISO) | Certification, trust signals. |
| **Marketplace curators** (Template creators) | Ecosystem enrichment, revenue share. |

---  

*Prepared by the Insight‑Loom product & engineering leadership team, Axentx.*
