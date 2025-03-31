# Deployment Guide

## Overview
This guide covers the deployment of UltraKG in various environments, from local development to production.

## Local Development

### Prerequisites
- Docker Desktop
- Python 3.12+
- Git

### Setup
1. Clone the repository
2. Copy `.env.example` to `.env`
3. Run `docker-compose up --build`

## Production Deployment

### Requirements
- Docker Engine
- Docker Compose
- NGINX (optional, for reverse proxy)

### Environment Variables
Required environment variables:
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`
- `ADMIN_SECRET`
- `FLOWISE_USERNAME`
- `FLOWISE_PASSWORD`

### Security Considerations
1. Change all default passwords
2. Configure SSL/TLS certificates
3. Set up proper firewall rules
4. Use secure secrets management

### Monitoring
- Service health checks available at `/health` endpoints
- NGINX Proxy Manager dashboard for traffic monitoring
- PostgreSQL monitoring tools

## Scaling
- Services can be scaled horizontally using Docker Compose
- Consider using Docker Swarm or Kubernetes for production
- Monitor resource usage and adjust accordingly 