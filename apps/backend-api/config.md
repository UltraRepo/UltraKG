# 🛠 UltraKG Deployment Configuration Guide

## 🌐 Network Architecture

```plaintext
[Internet]
   ↓
[Nginx Proxy Manager]
   ↓
[FastAPI via Uvicorn]
```

---

## ✅ Why This Setup?

| Feature | Why It’s Ideal |
|--------|----------------|
| ✅ **Simple Setup** | Works perfectly with Docker Compose |
| ✅ **Built-in SSL** | NGINX Proxy Manager handles certs with Let’s Encrypt |
| ✅ **Reverse Proxy Routing** | Easily route `ai.yourdomain.com`, `chat.yourdomain.com`, etc. |
| ✅ **FastAPI Native Server** | Uvicorn is async, lightweight, and ideal for FastAPI API services and web serving |
| ✅ **No Learning Curve** | No need to learn NGINX Unit’s JSON config API |
| ✅ **Better Compatibility** | Works seamlessly with Flowise, PGVector, Jena, and other services |

---

## 🌍 Recommended Subdomain Routing (via NGINX Proxy Manager)

| Service | Subdomain (via NPM) | Internal Port |
|--------|---------------------|---------------|
| FastAPI + UI | `ai.yourdomain.com` | `8000` |
| Flowise | `flowise.yourdomain.com` | `3000` |
| Jena Fuseki | `sparql.yourdomain.com` | `3030` |
| PostgreSQL Studio (optional) | `pg.yourdomain.com` | `5432` |
| Open WebUI | `chat.yourdomain.com` | `8081` |
| NGINX Proxy Manager | `admin.yourdomain.com` or `localhost:81` | `81` |

> 🔁 Replace `yourdomain.com` with your real domain.
> Ensure your DNS records point to the server running UltraKG.

---

## 🧱 Service Stack Summary

- **Reverse Proxy:** NGINX Proxy Manager (GUI + SSL)
- **API Backend:** FastAPI (served via Uvicorn)
- **LLM Chat Interface:** Open WebUI
- **Vector Search:** PostgreSQL + PGVector
- **Symbolic Query:** Apache Jena Fuseki
- **Document RAG:** Flowise (LangChain visual builder)
- **Landing Page:** Served via FastAPI static folder

---

## 🐳 Docker Compose Ports Overview

| Service | Port |
|---------|------|
| NGINX Proxy Manager | `80`, `81`, `443` |
| FastAPI | `8000` |
| PostgreSQL | `5432` |
| Jena Fuseki | `3030` |
| Flowise | `3000` |
| Open WebUI | `8081` |

---

## ✅ Included in This UltraKG Deployment

- `docker-compose.yml` with all services prewired
- `Dockerfile.fastapi` using Python 3.12 + Uvicorn
- `FastAPI` app serving static landing page
- `.env` and `example.env` files
- `.gitignore` for secrets and cache
- `README.md` with full onboarding instructions
- `Open WebUI` for local/private AI chat

---

## 📌 Notes

- NGINX Proxy Manager is your main entry point to route traffic and manage SSL certs.
- FastAPI requires `uvicorn` because it is an ASGI application — NGINX Proxy Manager **cannot** serve FastAPI directly.
- This architecture is secure, modular, and runs on **any cloud or on-prem VM**.

---

