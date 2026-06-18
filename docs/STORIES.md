# STORIES.md
**Project:** insight‑loom  
**Owner:** Product & Engineering Lead  
**Target Release:** MVP (v0.1) → Full Feature Set (v1.0)  

---  

## Table of Contents
1. [Epics Overview](#epics-overview)  
2. [MVP Backlog (Priority Order)](#mvp-backlog-priority-order)  
3. [Full‑Feature Backlog](#full-feature-backlog)  

---  

## Epics Overview  

| Epic ID | Title | Description | MVP Scope |
|---------|-------|-------------|----------|
| **E1** | **Data Ingestion & Normalization** | Enable founders/teams to import data from a variety of sources (docs, spreadsheets, emails, Slack, CRM, etc.) and transform it into a unified, searchable format. | ✅ Import from local files, Google Drive, and CSV/Excel; basic schema detection and cleaning. |
| **E2** | **Knowledge Graph & Tagging** | Build a lightweight knowledge graph that links entities (people, projects, metrics) and auto‑tags content for fast retrieval. | ✅ Entity extraction, manual tagging UI, simple graph view. |
| **E3** | **Insight Generation Engine** | Apply LLM‑driven summarization, trend detection, and recommendation generation over the ingested knowledge base. | ✅ Summarize a selected collection; surface top‑3 actionable insights. |
| **E4** | **Collaboration & Annotation** | Allow multiple team members to comment, vote, and curate insights together. | ✅ Inline comments, up‑/down‑vote, insight “bookmark”. |
| **E5** | **Export & Integration** | Deliver insights to downstream tools (e.g., Notion, Jira, email) and provide an API for programmatic access. | ✅ Export to PDF/Markdown; simple webhook for Slack. |
| **E6** | **Security & Permissions** | Role‑based access control, data encryption at rest/in‑flight, and audit logging. | ✅ Admin/Member roles; audit trail view. |
| **E7** | **Analytics Dashboard** | Visualize usage metrics, insight impact, and data health. | ✅ Basic usage stats (documents ingested, insights generated). |

---  

## MVP Backlog (Priority Order)

| # | Epic | User Story | Acceptance Criteria |
|---|------|------------|----------------------|
| **1** | E1 | **As a founder, I want to upload a folder of PDFs and Google Docs, so that all my market research is stored in one place.** | • UI shows “Add Source” button.<br>• Supports drag‑and‑drop of local files and OAuth‑based Google Drive selection.<br>• Files are parsed, text extracted, and stored in the unified repository.<br>• Upload progress and success/failure notifications are displayed. |
| **2** | E1 | **As a product manager, I want the system to automatically detect tables and key‑value pairs in spreadsheets, so that data is searchable without manual cleanup.** | • CSV/Excel files are parsed.<br>• Detected tables are stored as structured rows.<br>• Users can run a “Preview” to verify extraction.<br>• Extraction accuracy ≥ 90 % on the provided test suite. |
| **3** | E2 | **As a team member, I want the platform to suggest tags for each document, so that I can quickly locate related content later.** | • After ingestion, the system displays up to 5 auto‑generated tags.<br>• Tags are derived from entity extraction (people, companies, metrics).<br>• User can accept, edit, or delete suggested tags. |
| **4** | E2 | **As a data analyst, I want to view a simple graph that links people to projects, so that I can understand who is involved where.** | • Graph view shows nodes for “Person” and “Project” entities.<br>• Edges represent mentions in the same document.<br>• Clicking a node filters the document list accordingly. |
| **5** | E3 | **As a founder, I want a one‑click “Generate Insight” on a selected collection, so that I receive a concise summary and top recommendations.** | • User selects 1‑N documents and clicks “Generate Insight”.<br>• System returns a ≤ 300‑word summary and ≤ 3 bullet‑point recommendations.<br>• Insight includes source references (document titles). |
| **6** | E4 | **As a collaborator, I want to comment on a generated insight, so that I can discuss its relevance with the team.** | • Inline comment box appears under each insight.<br>• Comments are timestamped and show author name.<br>• Other members can reply and resolve comments. |
| **7** | E4 | **As a team lead, I want to vote on insights, so that the most valuable ones rise to the top.** | • Up‑vote and down‑vote buttons are present.<br>• Insight list can be sorted by vote score.<br>• Vote count updates in real‑time for all viewers. |
| **8** | E5 | **As a founder, I want to export an insight as a PDF, so that I can share it with external stakeholders.** | • “Export PDF” button generates a well‑formatted PDF containing the insight text, source list, and vote score.<br>• PDF download starts immediately and matches the on‑screen view. |
| **9** | E6 | **As an admin, I want to assign “Member” or “Viewer” roles to users, so that sensitive data is protected.** | • Admin UI lists all users with role dropdown.<br>• “Member” can edit tags, comment, vote.<br>• “Viewer” can only read insights.<br>• Role changes take effect without logout. |
| **10** | E7 | **As a product owner, I want a dashboard showing how many documents have been ingested and insights generated per week, so that I can track adoption.** | • Dashboard displays two line charts: “Documents Ingested” and “Insights Generated”.<br>• Data updates daily.<br>• Exportable as CSV. |

---  

## Full‑Feature Backlog (Post‑MVP)

| # | Epic | User Story | Acceptance Criteria |
|---|------|------------|----------------------|
| **11** | E1 | As a sales ops manager, I want to connect my CRM (e.g., HubSpot) via API, so that deal notes are automatically added to Insight‑Loom. | • OAuth flow for HubSpot.<br>• Configurable mapping of CRM fields to document schema.<br>• Incremental sync runs every hour. |
| **12** | E2 | As a researcher, I want to merge duplicate entities automatically, so that the knowledge graph stays clean. | • System detects > 80 % duplicate entities (same name, similar context).<br>• Presents a merge suggestion UI with “Merge”/“Ignore”. |
| **13** | E3 | As a founder, I want trend detection over time (e.g., rising keywords), so that I can spot emerging market signals. | • UI to select a time window.<br>• Displays top‑5 trending entities with growth percentages.<br>• Links each trend to supporting documents. |
| **14** | E4 | As a team, we want real‑time collaborative editing of insight drafts, so that we can co‑author recommendations. | • Multiple users can edit the same insight draft simultaneously.<br>• Changes are merged with operational transform (OT) and shown live. |
| **15** | E5 | As a developer, I want a REST API to query insights programmatically, so that I can embed them in internal tools. | • `/api/v1/insights?tag=...` returns JSON list of insights.<br>• API key authentication with rate limiting (100 req/min). |
| **16** | E6 | As a compliance officer, I want audit logs of who accessed which document, so that we can meet regulatory requirements. | • Log entries include user, timestamp, document ID, and action (view, edit, export).<br>• Admin UI can filter and export logs. |
| **17** | E7 | As a product manager, I want to see impact metrics (e.g., “insight adopted” flag), so that we can measure ROI. | • Users can mark an insight as “Implemented”.<br>• Dashboard shows adoption rate per month. |
| **18** | E3 | As a founder, I want the system to suggest next‑step actions (e.g., “schedule meeting with X”), so that insights become executable tasks. | • Action suggestions are generated from insight text using LLM prompts.<br>• Each suggestion can be sent to a connected task tool (e.g., Asana) via webhook. |
| **19** | E2 | As a data steward, I want bulk tag editing, so that I can correct taxonomy across many documents efficiently. | • Multi‑select UI for documents.<br>• Add/remove tags in bulk with preview before commit. |
| **20** | E5 | As a founder, I want scheduled email digests of new insights, so that I stay informed without logging in daily. | • User configures frequency (daily/weekly).<br>• Email contains summary of top‑3 insights with links. |

---  

**Notes**

* Stories are ordered to deliver a usable MVP within 8‑10 weeks (2‑week sprints).  
* Acceptance criteria are written to be testable and automatable (unit, integration, UI).  
* All MVP stories rely only on the core ingestion pipeline, a simple LLM inference wrapper (vLLM), and the existing front‑end framework in the repo.  
* Post‑MVP items leverage additional integrations (CRM, task tools) and advanced graph analytics that can be phased in as demand validates the product‑market fit.
