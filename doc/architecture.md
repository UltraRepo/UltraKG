# UltraKG Architecture

## Overview
UltraKG is a modular, cloud-agnostic Knowledge Graph system designed for enterprise private AI systems. This document outlines the system architecture and components.

## System Components

### Core Services
1. **FastAPI Service** (`apps/services/api`)
   - Main API service
   - Serves web client and API endpoints
   - Port: 8000

2. **Admin API** (`apps/services/admin-api`)
   - API key management and admin interface
   - Port: 8500

3. **Knowledge Graph Service** (`apps/services/kg-fuseki`)
   - Apache Jena Fuseki for SPARQL querying
   - Port: 3030

4. **Flowise Service** (`apps/services/flowise`)
   - Document ingestion and RAG agents
   - Port: 3000

5. **LocalAI Service**
   - Local AI instance with private and cloud LLMs
   - Port: 8080

6. **Open WebUI**
   - Chat interface for AI interactions
   - Port: 8081

### Infrastructure
1. **PostgreSQL + PGVector**
   - Vector search and hybrid AI queries
   - Port: 5432

2. **NGINX Proxy Manager**
   - Reverse proxy and SSL management
   - Ports: 80, 81, 443

## Directory Structure
```
UltraKG/
├── apps/
│   ├── services/          # Backend services
│   └── frontend/          # Frontend applications
├── packages/              # Shared packages
├── docker/               # Docker configurations
├── infra/                # Infrastructure code
└── doc/                  # Documentation
``` 