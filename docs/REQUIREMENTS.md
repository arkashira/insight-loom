# REQUIREMENTS.md

## Project Overview
**Product:** Insight‑Loom  
**Purpose:** Enable founders and teams to collect, organize, and analyze scattered information (documents, notes, messages, metrics) and automatically surface actionable insights and recommendations that drive better decision‑making.  
**Target Users:** Startup founders, product managers, executive teams, and cross‑functional squads that operate with heterogeneous data sources and need a unified view of their knowledge base.

---

## 1. Functional Requirements  

| ID | Description | Acceptance Criteria |
|----|-------------|----------------------|
| **FR‑1** | **Data Ingestion** – Users can import data from supported sources. | • UI wizard allows selection of source type (file upload, cloud storage, email, Slack, Notion, Google Docs, CSV/JSON). <br>• System validates format and shows preview before import. <br>• Ingestion completes within 30 s for ≤ 10 MB files. |
| **FR‑2** | **Unified Knowledge Store** – All imported items are stored in a searchable, versioned repository. | • Each item receives a unique immutable ID. <br>• Metadata (source, timestamp, tags, owner) is persisted. <br>• Full‑text index supports Boolean, fuzzy, and semantic search. |
| **FR‑3** | **Automatic Classification & Tagging** – System auto‑tags content using LLM‑driven classification. | • ≥ 90 % precision on a held‑out validation set of 5 k labeled items. <br>• Users can edit tags; edits are fed back to the model (online learning). |
| **FR‑4** | **Insight Generation** – Produce concise insights and recommendations per project or topic. | • For a given query (“What are the biggest risks for Q3?”) the system returns ≤ 3 bullet‑point insights with confidence scores. <br>• Insights are traceable to source documents (click‑through links). |
| **FR‑5** | **Interactive Dashboard** – Visualize insights, trends, and knowledge gaps. | • Timeline view of document activity. <br>• Heatmap of topic coverage. <br>• Exportable PDF/PNG reports. |
| **FR‑6** | **Collaboration** – Users can comment, assign tasks, and vote on insights. | • Real‑time updates via WebSocket. <br>• Notification system (in‑app & email). |
| **FR‑7** | **Search & Retrieval** – Powerful search across all stored content. | • Keyword, semantic, and vector‑based search. <br>• Pagination with < 200 ms latency for typical queries (≤ 10 k results). |
| **FR‑8** | **Access Control** – Role‑based permissions (Owner, Editor, Viewer, Guest). | • Admin can assign roles per workspace. <br>• Permissions enforced on API endpoints and UI actions. |
| **FR‑9** | **Export / Integration** – Export curated insights to external tools (e.g., Notion, Confluence, CSV). | • One‑click export with format selection. <br>• Webhooks for push notifications to third‑party services. |
| **FR‑10** | **Audit Trail** – Immutable log of all actions for compliance. | • Log entries include user, timestamp, action, and affected resource. <br>• Exportable audit log (JSON). |

---

## 2. Non‑Functional Requirements  

| ID | Category | Requirement |
|----|----------|-------------|
| **NFR‑1** | **Performance** | • Average query latency ≤ 200 ms (cold cache) and ≤ 80 ms (warm cache). <br>• Data ingestion throughput ≥ 5 MB/s per concurrent worker. |
| **NFR‑2** | **Scalability** | • Horizontal scaling to support up to 10 k active users and 100 M stored items. <br>• Stateless API layer; state stored in PostgreSQL + Redis. |
| **NFR‑3** | **Security** | • All traffic TLS 1.3. <br>• Data at rest encrypted with AES‑256. <br>• OAuth 2.0 / OpenID Connect for authentication. <br>• Role‑based access enforced server‑side. |
| **NFR‑4** | **Reliability & Availability** | • 99.9 % uptime SLA. <br>• Automated backups every 24 h; point‑in‑time recovery within 2 h. |
| **NFR‑5** | **Observability** | • Structured logging (JSON) to ELK stack. <br>• Metrics (Prometheus) for request latency, error rates, ingestion throughput. <br>• Alerting on > 1 % error rate or latency breach. |
| **NFR‑6** | **Data Privacy** | • GDPR‑compliant data handling. <br>• Right‑to‑be‑forgotten endpoint that purges user data and associated embeddings. |
| **NFR‑7** | **Maintainability** | • Codebase follows Axentx’s Python/TypeScript style guide. <br>• 80 %+ unit test coverage; integration tests for all API endpoints. |
| **NFR‑8** | **Extensibility** | • Plugin architecture for new data source connectors (Python entry‑point). <br>• LLM model abstraction layer to swap between vLLM, SGLang, or custom fine‑tuned models. |
| **NFR‑9** | **Usability** | • UI complies with WCAG 2.1 AA. <br>• Onboarding flow < 5 min for first import and insight generation. |
| **NFR‑10** | **Compliance** | • SOC 2 Type II readiness (logging, access control, change management). |

---

## 3. Constraints  

1. **Technology Stack** – Must use Axentx‑approved components:  
   - Backend: Python 3.11, FastAPI, PostgreSQL, Redis.  
   - LLM inference: vLLM or SGLang (as per runbook).  
   - Frontend: React 18 + TypeScript, TailwindCSS.  

2. **Data Residency** – All customer data must reside in the region selected by the workspace (EU, US‑East, APAC).  

3. **Licensing** – Only open‑source libraries with permissive licenses (Apache‑2.0, MIT, BSD) may be added; any commercial SDK requires explicit approval.  

4. **Deployment** – Containerized (Docker) and orchestrated via Kubernetes (Axentx‑standard helm charts).  

5. **Resource Limits** – Initial production deployment limited to 8 vCPU / 32 GB RAM per inference node; must stay within this envelope until scaling justification is approved.  

---

## 4. Assumptions  

| ID | Assumption |
|----|------------|
| **A‑1** | Users have at least one cloud storage account (Google Drive, Dropbox, etc.) for source data. |
| **A‑2** | The LLM model used for classification/insight generation will be a 7‑B parameter model hosted on vLLM (fits within current GPU budget). |
| **A‑3** | Users will provide consent for processing their data; no personally identifiable information (PII) will be stored without explicit opt‑in. |
| **A‑4** | Network latency between the UI and backend is < 100 ms for core regions (EU, US‑East). |
| **A‑5** | The existing Axentx knowledge base (≈ 33 M pairs) will be leveraged for few‑shot prompting; no additional data collection is required for MVP. |
| **A‑6** | The product will launch as a SaaS multi‑tenant offering; on‑premise deployment is out of scope for the initial release. |

---

## 5. Acceptance Criteria (Overall)

- All functional requirements FR‑1 – FR‑10 are demonstrably met in a staged rollout (alpha → beta → GA).  
- Non‑functional thresholds (NFR‑1 – NFR‑10) are validated via automated performance, security, and compliance test suites.  
- No duplicate functionality with existing Axentx products (e.g., iceoryx2 IPC library) – Insight‑Loom focuses purely on knowledge aggregation and insight generation.  
- Documentation (API spec, user guide, developer onboarding) is complete and version‑controlled in the repository.  

---  

*Prepared by: Senior Product/Engineering Lead – Insight‑Loom*  
*Date: 2026‑06‑18*
