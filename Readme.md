# UltraKG 🧠🌐

**UltraKG** is a modular, cloud-agnostic, open-source Knowledge Graph (KG) system designed for hybrid symbolic + vector reasoning. It enables the creation, storage, and semantic querying of OWL2/RDF knowledge graphs alongside vectorized AI document search — ideal for enterprise-grade GraphRAG and OmniRAG workflows.

UltraKG is built on standards like RDF, OWL2, SPARQL, PostgreSQL, and PGVector, and runs on **any cloud** or **on-prem infrastructure** using Docker.

---

## 🚀 Features

- 🧠 **Apache Jena + Fuseki** SPARQL server for OWL2/RDF querying
- 🐘 **PostgreSQL + PGVector** for vector search and hybrid AI queries
- 🔄 **LangChain (via Flowise)** for document ingestion + RAG agents
- 📄 **XLS to OWL2 Conversion** using ProtegeProject’s `mapping-master`
- 🌐 **FastAPI Landing Page** with admin interface via Nginx Proxy Manager
- ☁️ **Cloud-agnostic Docker deployment** (Azure, AWS, GCP, on-prem)

---

## ⚙️ Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/UltraRepo/UltraKG.git
cd UltraKG
```

### 2. Set environment variables

```bash
cp .env.example .env
```

Edit `.env` to match your environment, including PostgreSQL, NGINX Proxy, and Flowise credentials.

### 3. Launch the full stack

```bash
docker-compose up --build
```

---

## 🌐 FastAPI Admin Landing Page

After logging in through **Nginx Proxy Manager**, navigate to:

```
http://ai.yourdomain.com
```

> 🔁 Replace `yourdomain.com` with your custom domain.

This page includes:

- 🔗 **Launch Flowise**: Open the visual LangChain builder
- 📤 **Upload XLS File**: For OWL2 KG conversion (using mapping-master)
- 📥 **Download Knowledge Graph**: List and export RDF/OWL graphs from Fuseki
- 🐘 **Launch PostgreSQL Studio**: Optional DB GUI (if integrated)
- 🔐 **Launch NGINX Proxy Manager**
- 🧬 **View GitHub Project**: [GitHub Repo](https://github.com/UltraRepo/UltraKG)

---

## 📂 Directory Overview

| Folder | Purpose |
|--------|---------|
| `backend/jena-fuseki/` | SPARQL server with OWL2/RDF support |
| `backend/postgres/` | PostgreSQL with PGVector |
| `backend/flowise/` | Flowise-based LangChain RAG interface |
| `backend/reverse-proxy/` | NGINX Proxy Manager |
| `frontend/public/` | Static landing page served by FastAPI |
| `frontend/app/` | FastAPI app code |
| `tools/xls-to-owl/` | XLS to OWL CLI utility based on mapping-master |

---

## 🧪 Sample Use Case

1. Ingest documents via Flowise to PostgreSQL + PGVector
2. Convert metadata or structured XLS sheets to OWL2 with CLI
3. Load and query the RDF graphs via SPARQL in Fuseki
4. Use the FastAPI landing page as a control center for your KG pipeline

---

## 🔐 Environment Variables (`.env`)

```dotenv
# PostgreSQL
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=ultrakg

# PGVector
VECTOR_DIM=1536

# Fuseki
FUSEKI_DATASET=ultrakg
FUSEKI_PORT=3030

# Flowise credentials
FLOWISE_USERNAME=admin
FLOWISE_PASSWORD=secret

# NGINX Proxy Manager
NPM_EMAIL=admin@example.com
NPM_PASSWORD=changeme

# FastAPI Server
FASTAPI_PORT=8000
```

---

## 🛡 License

UltraKG Core is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

> For access to UltraKG Enterprise (editor UI, AI extensions, WebProtégé integration), contact us for licensing options.

---

## 🙌 Acknowledgments

- [Apache Jena](https://jena.apache.org/)
- [PostgreSQL + PGVector](https://github.com/pgvector/pgvector)
- [FlowiseAI](https://github.com/FlowiseAI/Flowise)
- [ProtegeProject mapping-master](https://github.com/protegeproject/mapping-master)
