# FastAPI Admin Reinstallation Guide

## Current Issue

The FastAPI Admin app is failing to install due to dependency conflicts between different versions of packages:

1. The error `ImportError: cannot import name 'ModelField' from 'pydantic.fields'` indicates a version mismatch between `pydantic` and `fastapi-amis-admin`.
2. There are conflicting dependencies between:
   - FastAPI (requiring pydantic with specific version constraints)
   - SQLModel (requiring pydantic >=1.10.13)
   - Pydantic-settings (requiring pydantic >=2.7.0)

## Resolution Steps

1. **Clean Docker Environment**
   ```bash
   # Stop all containers and remove volumes
   docker-compose down -v
   
   # Clean Docker cache
   docker system prune -f
   ```

2. **Update Dependencies**
   - Edit `apps/services/admin-api/requirements.txt`:
     ```
     fastapi==0.95.2
     pydantic==1.10.13
     fastapi-amis-admin==0.5.8
     sqlmodel==0.0.8
     ```

3. **Rebuild Admin Service**
   ```bash
   docker-compose build api-admin
   docker-compose up api-admin
   ```

## Verification Steps

1. **Check Container Status**
   ```bash
   docker-compose ps
   ```
   Expected: `api-admin` container should be running

2. **Check Container Logs**
   ```bash
   docker-compose logs api-admin
   ```
   Expected: No error messages about pydantic or ModelField

3. **Test API Endpoints**
   - Open browser to `http://localhost:8500/`
   - Should see message: "API Admin is running"

4. **Test Admin Interface**
   - Open browser to `http://localhost:8500/admin/`
   - Should see login page
   - Default credentials:
     - Username: admin
     - Password: admin

5. **Verify Database Connection**
   - After login, check if API Keys table is visible
   - Try creating a new API key to verify CRUD operations

## Troubleshooting

If issues persist:

1. **Check Dependencies**
   ```bash
   docker-compose exec api-admin pip freeze
   ```
   Verify versions match requirements.txt

2. **Check Container Health**
   ```bash
   docker inspect api-admin
   ```
   Look for health status and network settings

3. **Test Database Connection**
   ```bash
   docker-compose exec api-admin python
   >>> from sqlmodel import create_engine
   >>> engine = create_engine("postgresql+asyncpg://postgres:password123@postgres:5432/db")
   ```

## Common Issues

1. **Pydantic Version Conflicts**
   - Solution: Pin pydantic to version 1.10.13
   - Reason: FastAPI AMIS Admin requires pydantic v1

2. **Port Conflicts**
   - Check if port 8500 is already in use
   - Solution: Change port in docker-compose.yml if needed

3. **Database Connection**
   - Ensure postgres container is running
   - Check database credentials in environment variables 