from fastapi import FastAPI
from fastapi_admin.app import app as admin_app
from tortoise.contrib.fastapi import register_tortoise
from api_models.apikey import APIKey
import os

app = FastAPI(title="UltraKG Admin API")

# Database configuration
DB_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password123@postgres:5432/db")

# Register Tortoise ORM
register_tortoise(
    app,
    db_url=DB_URL,
    modules={"models": ["api_models.apikey"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
async def root():
    return {"message": "API Admin is running"}

# Mount the admin interface
app.mount("/admin", admin_app)

# Admin interface configuration
@app.on_event("startup")
async def startup():
    await admin_app.configure(
        logo_url="https://preview.tabler.io/static/logo-white.svg",
        template_folders=["templates"],
        favicon_url="https://raw.githubusercontent.com/fastapi-admin/fastapi-admin/dev/images/favicon.png",
        providers=[
            {
                "model": APIKey,
                "icon": "fas fa-key",
                "label": "API Keys",
            }
        ],
        admin_secret=os.getenv("ADMIN_SECRET", "your-admin-secret-key")
    )
