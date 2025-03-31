from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_amis_admin.admin.site import AdminSite
from fastapi_amis_admin.admin.settings import Settings
from api_models.apikey import APIKey

# Create FastAPI application
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database configuration
DB_URL = "postgresql+asyncpg://postgres:password123@postgres:5432/db"

# Create AdminSite instance
site = AdminSite(settings=Settings(database_url_async=DB_URL))

@app.get("/")
async def root():
    return {"message": "API Admin is running"}

# Mount AdminSite instance
site.mount_app(app)
