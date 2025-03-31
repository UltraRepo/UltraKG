# Development Guide

## Prerequisites
- Docker Desktop
- Python 3.12+
- Git

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/UltraRepo/UltraKG.git
cd UltraKG
```

2. Create environment file:
```bash
cp .env.example .env
```

3. Start the development stack:
```bash
docker-compose up --build
```

## Development Workflow

### Directory Structure
- `apps/services/` - Backend services
- `apps/frontend/` - Frontend applications
- `packages/` - Shared packages and utilities
- `docker/` - Docker configurations
- `infra/` - Infrastructure code
- `doc/` - Documentation

### Service Ports
- FastAPI: http://localhost:8000
- Admin API: http://localhost:8500
- Flowise: http://localhost:3000
- LocalAI: http://localhost:8080
- Open WebUI: http://localhost:8081
- Jena Fuseki: http://localhost:3030
- NGINX Proxy Manager: http://localhost:81

### Default Credentials
- NGINX Proxy Manager: admin@example.com / changeme
- Flowise: admin / secret
- PostgreSQL: postgres / password123 / db 