# Roadmap for **insight‑loom**
*Version: 2026‑06‑18*  
*Repo: `insight-loom`*  

---

## 🎯 Vision
Empower founders and teams to turn fragmented data—notes, emails, meeting transcripts, tickets, and analytics—into coherent insights and actionable recommendations, accelerating smarter decision‑making.

---

## 📅 Milestones Overview

| Milestone | Target Date | Description | MVP‑Critical |
|-----------|-------------|-------------|--------------|
| **MVP – Insight Core** | **2026‑08‑15** | Launch the minimal viable product that can ingest, index, and surface insights from a single data source. | ✅ |
| **v1 – Multi‑Source Fusion** | 2026‑11‑30 | Add support for multiple data streams, collaborative workspaces, and basic recommendation engine. | — |
| **v2 – Intelligent Automation** | 2027‑03‑31 | Introduce AI‑driven summarization, predictive analytics, and integrations with major PM/CRM tools. | — |
| **v3 – Enterprise Scale** | 2027‑09‑30 | Role‑based access, SSO, audit logs, on‑prem deployment option, and marketplace of plug‑ins. | — |

---

## 🚀 MVP – Insight Core (Must‑have for launch)

| Feature | Description | Acceptance Criteria |
|---------|-------------|----------------------|
| **Data Ingestion (single source)** | Upload or connect to one data source (e.g., CSV, Google Docs, or Slack export). | • UI wizard for file upload or OAuth connection.<br>• Data stored in encrypted PostgreSQL (or compatible) DB.<br>• Ingestion logs visible to user. |
| **Unified Indexing Engine** | Parse, chunk, and embed documents using the in‑house **vLLM** inference service. | • Text split into ≤ 512‑token chunks.<br>• Embeddings stored in pgvector for fast similarity search.<br>• Index rebuild on new upload completes < 5 min for ≤ 10 k docs. |
| **Search & Retrieval UI** | Simple web UI to query the knowledge base and view highlighted results. | • Keyword + semantic search bar.<br>• Top‑5 results displayed with snippet highlighting.<br>• Click‑through opens full document view. |
| **Insight Generation** | Generate a concise insight summary for a given query using **SGLang** structured generation. | • One‑click “Generate Insight” button.<br>• Output ≤ 3 sentences, cites source documents.<br>• Confidence score displayed. |
| **Export / Share** | Export insight as PDF or share a read‑only link. | • PDF includes query, insight, and source citations.<br>• Share link expires after configurable period (default 7 days). |
| **Auth & Billing (basic)** | Email/password login + Stripe trial subscription. | • Secure password hashing (bcrypt).<br>• Trial period 14 days, auto‑upgrade prompt. |
| **Observability** | Basic health dashboards & error logging. | • Prometheus metrics for ingestion latency, query latency, error rate.<br>• Grafana dashboard pre‑wired. |

### MVP Success Metrics
- **≥ 500** active trial users within 30 days of launch.  
- **Average query latency ≤ 2 s** for 10 k‑doc corpus.  
- **User‑reported insight relevance ≥ 4/5** (via in‑app rating).  

---

## 🌱 v1 – Multi‑Source Fusion

| Theme | Key Features | Target Release |
|-------|--------------|----------------|
| **Data Expansion** | • Connectors for Gmail, Outlook, Jira, Notion, Confluence.<br>• Incremental sync (webhooks / polling). | Q4 2026 |
| **Collaborative Workspaces** | • Team folders, shared queries, comment threads.<br>• Real‑time edit lock & change history. | Q4 2026 |
| **Recommendation Engine** | • Rule‑based suggestions (e.g., “You have 3 open tickets about X”).<br>• Simple “next‑action” prompts. | Q4 2026 |
| **Product Analytics** | • Dashboard of most‑queried topics, usage heat‑maps.<br>• Exportable CSV reports. | Q4 2026 |
| **Improved UI/UX** | • Dark mode, keyboard shortcuts, mobile‑responsive layout. | Q4 2026 |

### v1 Success Metrics
- **≥ 2 k** paid subscriptions within 60 days of v1 release.  
- **Multi‑source sync latency ≤ 5 min** for typical SaaS APIs.  
- **Team NPS ≥ 45**.

---

## 🤖 v2 – Intelligent Automation

| Theme | Key Features | Target Release |
|-------|--------------|----------------|
| **AI Summarization** | • Multi‑document executive summary (≤ 200 words).<br>• Customizable tone & length. | Q1 2027 |
| **Predictive Insights** | • Trend detection across time‑series data (e.g., ticket volume spikes).<br>• Forecast‑driven recommendations. | Q1 2027 |
| **Smart Integrations** | • Bi‑directional sync with Salesforce, HubSpot, Asana.<br>• Auto‑create tasks from insights. | Q1 2027 |
| **Feedback Loop** | • In‑app rating feeds back to fine‑tune SGLang prompts (continuous learning). | Q1 2027 |
| **Security Harden** | • End‑to‑end encryption, data residency options. | Q1 2027 |

### v2 Success Metrics
- **Insight generation accuracy ≥ 90 %** (human‑rated).  
- **Forecast error ≤ 15 %** on pilot datasets.  
- **Integration adoption ≥ 30 %** of active teams.

---

## 🏢 v3 – Enterprise Scale

| Theme | Key Features | Target Release |
|-------|--------------|----------------|
| **RBAC & SSO** | • SAML, OIDC, Azure AD support.<br>• Granular role permissions. | Q3 2027 |
| **On‑Prem / Private Cloud** | • Docker‑Compose & Helm charts for self‑hosted deployment.<br>• Data‑at‑rest encryption keys managed by customer. | Q3 2027 |
| **Marketplace** | • Plug‑in SDK for third‑party data connectors & custom insight modules.<br>• Revenue share model. | Q3 2027 |
| **Compliance** | • GDPR, CCPA, SOC‑2 audit‑ready reports. | Q3 2027 |
| **Performance Scaling** | • Sharded pgvector clusters, async ingestion pipelines, auto‑scale vLLM workers. | Q3 2027 |

### v3 Success Metrics
- **Enterprise ARR ≥ $2 M** within 12 months of v3 GA.  
- **99.9 % uptime SLA** met.  
- **Customer churn < 5 %** annually.

---

## 📦 Release Process (Aligned with Axentx Pipeline)

1. **PM/PRD** – Finalize feature specs per milestone.  
2. **Architecture** – Update design docs; ensure vLLM & SGLang scaling plans.  
3. **Development** – Feature branches follow `feature/<milestone>/<name>`. CI runs unit, integration, and performance tests.  
4. **QA** – Automated regression suite + manual exploratory testing on staging.  
5. **Reviewer Gate** – Code quality, security scan, and documentation completeness must pass.  
6. **Validation** – Pilot with 5‑10 target customers; collect willingness‑to‑pay signals before public launch.  

---

## 📌 Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Embedding latency at scale** | Delays in search & insight generation | Pre‑warm vLLM workers; use batch embedding; monitor via Prometheus. |
| **Data privacy concerns** | Customer trust loss | End‑to‑end encryption, clear data‑retention policies, SOC‑2 prep. |
| **Integration brittleness** | Breakage when SaaS APIs change | Abstract connector layer; automated contract tests; versioned API adapters. |
| **Model drift** | Degraded insight relevance | Continuous fine‑tuning loop using user feedback; schedule monthly re‑train. |

---

## 📈 Success Dashboard (Post‑Launch)

- **User Growth** – Daily active users, trial‑to‑paid conversion.  
- **Performance** – Avg. query latency, ingestion throughput.  
- **Quality** – Insight relevance score, NPS.  
- **Revenue** – MRR, ARR, churn.  

All metrics visualized in Grafana; alerts configured for SLA breaches.

---

*Prepared by the Insight‑Loom Product & Engineering Lead*  
*© Axentx 2026 – All rights reserved*
