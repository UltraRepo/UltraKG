# AirVeo Monorepo

**AirVeo** is a modular, standards-based AI reasoning platform that empowers developers and enterprises to deploy high-accuracy, explainable, and extensible AI systems using open ontologies and symbolic logic.

---

## 🔐 API Key Manager Integration (FastAPI + Admin UI)

AirVeo supports multiple API key management approaches. The recommended solution is to use **FastAPI Admin** for a web-based UI and centralized API key control.

### ✅ FastAPI Admin Setup (Basic)

1. Define your `APIKey` model:
```python
class APIKey(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=100)
    key = fields.CharField(max_length=255, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
```

2. Use `FastAPI Admin` to manage keys via web UI:
- Add
- Delete
- Assign to users
- View usage logs

3. Secure your endpoints:
```python
from fastapi import Depends, HTTPException, Request

API_KEY = "your-secret-key"

@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    if request.headers.get("x-api-key") != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await call_next(request)
```

---

## 🧠 Keycloak Integration (Planned Feature)

For enterprise OAuth2 and multi-client token control, **Keycloak** is planned as an optional identity provider.

### 🔐 Keycloak vs Traditional API Key Managers

| Feature                        | FastAPI Admin | FastAPI Simple Security | 🔐 Keycloak |
|-------------------------------|----------------|---------------------------|-------------|
| Web UI to manage keys/users   | ✅              | ❌ (CLI only)              | ✅ Full admin console |
| Fine-grained roles/scopes     | ❌ (manual)     | ❌                        | ✅ Native |
| Expiration / rotation         | ❌             | ✅ (static keys)           | ✅ Token-based rotation |
| Multi-client API access       | ❌             | ❌                        | ✅ OAuth2 Clients |
| Standards-based (OAuth2)      | ❌             | ❌                        | ✅ OIDC/OAuth2 |

---

## 📁 Monorepo Structure

```
AirVeo/
├── apps/
│   ├── backend-api/            # FastAPI server
│   ├── backend-kg/             # Apache Jena RDF store
│   ├── desktop-app/            # Electron app (optional)
│   └── flowise-agent/          # Flowise agent orchestration
│
├── packages/
│   ├── shared-ui/              # React component lib
│   ├── design-tokens/          # Theme, colors, spacing
│   ├── types/                  # Shared types/interfaces
│   └── utils/                  # Common logic
│
├── docker/                     # Dockerfiles per app (if needed)
│
├── infra/                      # Infra and deployment (NGINX, LocalAI, Keycloak)
│
├── models/                     # Mounted volume for LocalAI model caching
├── .github/                    # GitHub Actions / CI workflows
├── .env.example                # Example env vars
├── README.md
└── LICENSE
```

---

## 🚀 Next Steps

- Integrate FastAPI Admin UI
- Optionally deploy Keycloak + configure OAuth2
- Connect to frontend or desktop app using token-based security
