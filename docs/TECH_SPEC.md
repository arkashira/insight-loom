# TECH_SPEC.md  
**Project:** insight-loom  
**Owner:** Axentx – Product & Engineering Lead  
**Status:** Draft – Ready for review & implementation  

---  

## 1. Overview  

**insight‑loom** is a SaaS platform that ingests, organizes, and analyzes scattered information (documents, messages, tickets, notes, etc.) for founders and product teams. It transforms unstructured data into a **knowledge graph** and surfaces **actionable insights** and **recommendations** through a unified UI and API.  

Key goals:  

| Goal | Success Metric |
|------|----------------|
| Rapid ingestion of heterogeneous sources | ≤ 30 seconds per GB of raw data |
| High‑precision insight extraction | ≥ 85 % F1 on validated insight benchmark |
| Real‑time recommendation engine | ≤ 200 ms latency for top‑k suggestions |
| Multi‑tenant security & isolation | SOC‑2 compliant, per‑tenant encryption at rest & in‑flight |
| Scalable deployment | Horizontal scaling to 10 k concurrent users, 100 k daily active documents |

---  

## 2. Architecture Overview  

```
+-------------------+      +-------------------+      +-------------------+
|   Ingestion API   | ---> |   Ingestion Queue | ---> |   Workers (vLLM) |
+-------------------+      +-------------------+      +-------------------+
          |                         |                         |
          v                         v                         v
+-------------------+      +-------------------+      +-------------------+
|   Metadata Store  | <--> |   Knowledge Graph | <--> |   Insight Engine  |
+-------------------+      +-------------------+      +-------------------+
          ^                         ^                         ^
          |                         |                         |
+-------------------+      +-------------------+      +-------------------+
|   Frontend UI     | <--> |   REST / GraphQL  | <--> |   Recommendation  |
+-------------------+      +-------------------+      +-------------------+
```

### Core Layers  

1. **Ingestion Layer** – Handles file uploads, webhooks, email parsing, and API pulls. Normalizes to a canonical **Document** format (text + metadata).  
2. **Processing Workers** – Powered by **vLLM** (production‑grade LLM inference) and **SGLang** for structured generation (entity extraction, summarization, sentiment).  
3. **Knowledge Graph Store** – Neo4j (v5) representing entities, relationships, and temporal context.  
4. **Insight Engine** – Runs graph queries + LLM‑driven reasoning to produce insights, risk flags, and recommendations.  
5. **API Layer** – GraphQL for flexible queries + REST endpoints for legacy integrations.  
6. **Frontend** – React + TypeScript SPA with real‑time dashboards, annotation UI, and export tools.  

---  

## 3. Components & Responsibilities  

| Component | Language / Tech | Responsibilities | Key Interfaces |
|-----------|----------------|------------------|----------------|
| **Ingestion Service** | Python 3.11 (FastAPI) | Auth, validation, chunking, metadata extraction, push to Kafka | `POST /ingest`, `PUT /ingest/{id}` |
| **Ingestion Queue** | Apache Kafka (3.3) | Decoupled, at‑least‑once delivery of document payloads | Topics: `documents.raw`, `documents.metadata` |
| **Worker Pool** | Python (vLLM, SGLang) | LLM inference for NER, summarization, classification; writes results to Neo4j | Consumes `documents.raw`, produces `documents.processed` |
| **Metadata Store** | PostgreSQL 15 (TimescaleDB extension) | Tenant‑scoped document metadata, versioning, audit logs | SQL via SQLAlchemy |
| **Knowledge Graph** | Neo4j 5 (Aura Cloud) | Entity/relationship persistence, graph traversals | Bolt driver (Python) |
| **Insight Engine** | Python (LangChain, custom reasoning) | Generates insights, risk scores, recommendation lists | Internal service calls, GraphQL resolvers |
| **API Gateway** | Node.js (NestJS) | Auth (OAuth2/JWT), rate‑limiting, request routing | `/api/v1/*` (REST), `/graphql` |
| **Frontend** | React 18, TypeScript, MUI, Recoil | UI for document upload, graph visualization, insight dashboards | Calls API Gateway |
| **Observability** | Prometheus + Grafana, Loki, OpenTelemetry | Metrics, traces, logs, alerts | Exporters in each service |
| **CI/CD** | GitHub Actions, Docker, Helm (K8s) | Build, test, security scan, canary deploy | N/A |

---  

## 4. Data Model  

### 4.1 Document  

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Primary key |
| `tenant_id` | UUID | Foreign key to Tenant |
| `source` | Enum(`upload`,`webhook`,`email`,`api`) | Origin |
| `content_type` | String | MIME type |
| `raw_text` | TEXT | Full extracted text |
| `metadata` | JSONB | Key‑value pairs (author, created_at, tags) |
| `created_at` | TIMESTAMP | Ingestion timestamp |
| `status` | Enum(`pending`,`processed`,`failed`) | Pipeline state |

### 4.2 Entity (Graph Node)

| Property | Type | Description |
|----------|------|-------------|
| `uid` | UUID | Unique node ID |
| `type` | Enum(`person`,`company`,`product`,`event`,`concept`) | Semantic class |
| `name` | String | Canonical name |
| `attributes` | JSONB | Additional properties (e.g., role, market) |
| `tenant_id` | UUID | Isolation |
| `created_at` | TIMESTAMP | |

### 4.3 Relationship (Graph Edge)

| Property | Type | Description |
|----------|------|-------------|
| `uid` | UUID | Unique edge ID |
| `src` | UUID | Source node |
| `dst` | UUID | Destination node |
| `type` | Enum(`mentions`,`belongs_to`,`competitor_of`,`causes`,`related_to`) |
| `weight` | Float | Confidence from LLM |
| `tenant_id` | UUID | |
| `created_at` | TIMESTAMP | |

### 4.4 Insight  

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | |
| `tenant_id` | UUID | |
| `title` | String | Human‑readable headline |
| `description` | TEXT | Full narrative |
| `category` | Enum(`trend`,`risk`,`opportunity`,`actionable`) |
| `score` | Float (0‑1) | Confidence |
| `source_documents` | ARRAY[UUID] | Provenance |
| `generated_at` | TIMESTAMP | |

---  

## 5. Key APIs / Interfaces  

### 5.1 REST Endpoints (API Gateway)

| Method | Path | Description | Auth |
|--------|------|-------------|------|
| `POST` | `/api/v1/ingest` | Upload file or URL payload | Bearer JWT |
| `GET` | `/api/v1/insights` | List latest insights (filterable) | Bearer JWT |
| `GET` | `/api/v1/insights/{id}` | Retrieve single insight | Bearer JWT |
| `GET` | `/api/v1/graph` | Export sub‑graph (Cypher) | Bearer JWT |
| `POST` | `/api/v1/feedback` | Submit user feedback on insight quality | Bearer JWT |

### 5.2 GraphQL Schema (public)

```graphql
type Document {
  id: ID!
  title: String
  createdAt: DateTime!
  status: String!
}

type Insight {
  id: ID!
  title: String!
  description: String!
  category: String!
  score: Float!
  sources: [Document!]!
  generatedAt: DateTime!
}

type Query {
  insights(
    tenantId: ID!
    limit: Int = 20
    offset: Int = 0
    category: String
    minScore: Float
  ): [Insight!]!

  document(id: ID!): Document
  graphExplore(
    tenantId: ID!
    startNodeId: ID!
    depth: Int = 2
  ): GraphResult!
}
```

### 5.3 Internal Service Calls  

* **Worker → Neo4j**: `MERGE (e:Entity {uid: $uid}) SET e += $props`  
* **Insight Engine → GraphQL**: Query patterns, then feed results to LLM chain.  

---  

## 6. Technology Stack  

| Layer | Choice | Rationale |
|-------|--------|-----------|
| Language | Python 3.11 (core), TypeScript (frontend) | Mature ML ecosystem, async support |
| Inference Engine | **vLLM** (GPU‑accelerated, token‑level scheduling) | Handles high‑throughput LLM calls, proven in Axentx |
| Structured Generation | **SGLang** | Guarantees JSON‑compatible output for entities |
| Message Bus | Apache Kafka | Decoupled, replayable, back‑pressure handling |
| Graph DB | Neo4j Aura (managed) | Native graph queries, ACID, multi‑tenant |
| Relational DB | PostgreSQL (Timescale) | Time‑series metadata, audit |
| API Gateway | NestJS (Node) | Strong typing, built‑in guards, easy GraphQL |
| Frontend | React 18 + MUI + Recoil | Component library, state management |
| Containerization | Docker (multi‑stage) | Consistent builds |
| Orchestration | Kubernetes (v1.28) + Helm charts | Auto‑scaling, canary releases |
| Observability | OpenTelemetry → Prometheus/Grafana, Loki | End‑to‑end tracing |
| CI/CD | GitHub Actions + Dependabot | Automated testing, security updates |

---  

## 7. Dependencies  

| Dependency | Version | License |
|------------|---------|---------|
| vLLM | 0.4.2 | Apache‑2.0 |
| SGLang | 0.2.1 | MIT |
| Neo4j Python Driver | 5.12.0 | MIT |
| FastAPI | 0.110.0 | MIT |
| NestJS | 10.2.0 | MIT |
| React | 18.2.0 | MIT |
| PostgreSQL | 15 | PostgreSQL |
| Kafka | 3.3 | Apache‑2.0 |
| OpenTelemetry SDK | 1.24.0 | Apache‑2.0 |

All third‑party libraries are vetted for commercial use and listed in `LICENSES.md`.

---  

## 8. Deployment Architecture  

### 8.1 Cloud Provider  

- **Primary:** AWS (us‑east‑1) – leveraged for GPU instances (p4d) for vLLM workers, managed RDS (PostgreSQL), and MSK (Kafka).  
- **Backup/DR:** Azure (East US) – Neo4j Aura replica, S3 cross‑region replication.  

### 8.2 Kubernetes Cluster  

| Namespace | Service | Replicas (baseline) | Autoscaling |
|-----------|---------|---------------------|-------------|
| `ingest` | Ingestion API | 3 | CPU‑based HPA (min 2, max 8) |
| `workers` | vLLM Workers | 4 (GPU) | GPU‑based HPA (min 2, max 16) |
| `graph` | Neo4j (managed) | — | — |
| `api` | API Gateway | 3 | CPU HPA |
| `frontend` | React SPA (NGINX) | 2 | CPU HPA |
| `monitor` | Prometheus/Grafana | 1 | — |

All services expose **internal** ClusterIP; external traffic enters via **AWS ALB** with TLS termination (cert‑manager).  

### 8.3 CI/CD Pipeline  

1. **Push** → GitHub Actions lint & unit tests.  
2. **Build** Docker images (multi‑arch).  
3. **Security Scan** (Trivy).  
4. **Push** to ECR (versioned tags).  
5. **Helm Deploy** to `staging` cluster (canary).  
6. **Integration Tests** (Postman/Newman).  
7. **Promote** to `prod` after manual approval.  

---  

## 9. Security & Compliance  

- **Authentication:** OAuth2 Authorization Code Flow with PKCE; JWT signed with RS256.  
- **Authorization:** RBAC per tenant; scopes `read:insights`, `write:documents`.  
- **Encryption:** TLS 1.3 for all in‑flight traffic; AES‑256‑GCM at rest (EBS, S3, Neo4j).  
- **Data Isolation:** Separate PostgreSQL schemas per tenant; Neo4j label `Tenant_{id}`.  
- **Audit Logging:** Immutable logs stored in S3 Glacier via Loki.  
- **Compliance:** Designed for SOC‑2 Type II; GDPR‑compliant data‑subject deletion endpoint (`DELETE /api/v1/documents/{id}`).  

---  

## 10. Scalability & Performance  

| Metric | Target | Test Method |
|--------|--------|-------------|
| Ingestion throughput | 5 k docs/min (avg 200 KB) | Load test with Locust |
| LLM inference latency | ≤ 150 ms per 512‑token chunk | vLLM benchmark suite |
| Graph query latency | ≤ 200 ms for 2‑hop traversals | Neo4j query profiling |
| Insight generation latency | ≤ 500 ms for top‑5 recommendations | End‑to‑end integration test |
| Horizontal scaling | +1 GPU node adds ~30 % capacity | Autoscaling simulation |

---  

## 11. Monitoring & Alerting  

- **Metrics:** Request latency, error rates, worker queue depth, GPU utilization.  
- **Alerts:**  
  - `IngestionQueueDepth > 10k` → Slack #ops  
  - `vLLM latency > 300ms (5m avg)` → PagerDuty  
  - `Neo4j query timeout > 2s` → Email ops  
- **Dashboards:**  
  - System health (CPU/GPU, pod restarts)  
  - Business KPIs (documents ingested per tenant, insights generated)  

---  

## 12. Risks & Mitigations  

| Risk | Impact | Mitigation |
|------|--------|------------|
| LLM hallucination → false insights | Customer trust loss | Human‑in‑the‑loop feedback loop; confidence scoring; continuous fine‑tuning on validated data |
| Multi‑tenant data bleed | Legal/compliance | Strict schema separation; automated penetration testing |
| GPU resource exhaustion | Service degradation | Autoscaling policies; fallback to CPU inference with reduced model |
| Vendor lock‑in (Neo4j Aura) | Future migration cost | Abstract graph access via repository layer; maintain export scripts (CSV/GraphML) |
| Model drift over time | Degraded accuracy | Periodic re‑training using Axentx’s auto‑harvested pairs (≈150 M new pairs weekly) |

---  

## 13. Release Plan  

| Milestone | Duration | Deliverables |
|-----------|----------|--------------|
| **M1 – Foundations** | 4 weeks | Ingestion API, Kafka, PostgreSQL schema, CI pipeline |
| **M2 – LLM Workers** | 5 weeks | vLLM + SGLang integration, entity extraction, unit tests |
| **M3 – Knowledge Graph** | 3 weeks | Neo4j schema, import pipelines, basic queries |
| **M4 – Insight Engine** | 4 weeks | Reasoning chain, confidence scoring, feedback API |
| **M5 – API & Frontend** | 4 weeks | GraphQL, REST endpoints, React dashboards |
| **M6 – Security & Compliance** | 2 weeks | Auth, RBAC, encryption, audit logs |
| **M7 – Load & Stress Test** | 2 weeks | Performance benchmarks, autoscaling validation |
| **M8 – Beta Launch** | 2 weeks | Pilot with 3 external founders, collect NPS & feedback |
| **M9 – GA Release** | 1 week | Production rollout, monitoring dashboards, support hand‑off |

---  

## 14. Appendices  

### 14.1 Glossary  

- **LLM** – Large Language Model.  
- **SGLang** – Structured Generation Language for deterministic JSON output.  
- **vLLM** – High‑throughput LLM inference engine.  
- **Tenant** – Isolated customer workspace.  

### 14.2 References  

- Axentx Runbook (2026‑05‑23) – internal repository `arkashira/surrogate-1-harvest`.  
- vLLM GitHub: <https://github.com/vllm-project/vllm>  
- SGLang GitHub: <https://github.com/sgl-project/sglang>  

---  

*Prepared by the Insight‑Loom Engineering Team – June 2026*
