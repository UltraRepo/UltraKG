**UltraKG** is a modular, cloud-agnostic, open-source Knowledge Graph (KG) system designed for hybrid symbolic + vector reasoning. It enables the creation, storage, and semantic querying of OWL2/RDF knowledge graphs alongside vectorized AI document search — ideal for enterprise-grade GraphRAG and OmniRAG workflows.

UltraKG is built on standards like RDF, OWL2, SPARQL, PostgreSQL, and PGVector, and runs on **any cloud** or **on-prem infrastructure** using Docker.

---

## 🚀 Features

- 🧠 **Apache Jena + Fuseki** SPARQL server for OWL2/RDF querying
- 🐘 **PostgreSQL + PGVector** for vector search and hybrid AI queries
- 🔄 **LangChain (via Flowise)** for document ingestion + RAG agents
- 📄 **XLS to OWL2 Conversion** using ProtegeProject’s `mapping-master`
- 🌍 **Nginx Proxy Manager** for domain-based access (e.g., `ai.yourdomain.com`)
- ☁️ **Cloud-agnostic Docker deployment** (Azure, AWS, GCP, on-prem)

---

## 🧱 Architecture

``` plaintext
+-------------+     +----------------+     +----------------------+
| Flowise RAG | --> | PGVector (SQL) | --> | Apache Jena Fuseki   |
|  (LangChain)|     | + PostgreSQL   |     |  SPARQL Server       |
+-------------+     +----------------+     +----------------------+
                             ↑
     +----------------+      |      +--------------------+
     | XLS to OWL2    |------+----->| OWL2 Individuals   |
     | mapping tool   |             | with GUID links    |
     +----------------+             +--------------------+
```

---

## ⚙️ Quick Start

### 1. Clone the repo

``` bash
git clone https://github.com/UltraRepo/UltraKG.git
cd UltraKG
``` 

### 2. Set environment variables

``` bash
cp .env.example .env
``` 

Edit `.env` to match your local or cloud environment.

### 3. Launch stack with Docker

``` bash
docker-compose up --build
``` 

---

## 📂 Directory Overview

| Folder | Purpose |
|--------|---------|
| \jena-fuseki | SPARQL server with OWL2/RDF support |
| \postgres  | PostgreSQL with PGVector extension |
| \flowise  | Visual LangChain UI for RAG pipelines |
| \tools/xls-to-owl  | XLS to OWL2 RDF mapping CLI utility |
| \reverse-proxy  | Nginx Proxy Manager for subdomain routing |

---

## 🧪 Sample Use Case

1. Ingest documents via Flowise to PostgreSQL + PGVector
2. Convert metadata (or XLS files) to OWL2 using the CLI tool
3. Load OWL2 graph into Apache Jena Fuseki
4. Query knowledge via SPARQL + vector search
5. Route services via `ai.yourdomain.com\`, `sparql.yourdomain.com\`, etc.

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
