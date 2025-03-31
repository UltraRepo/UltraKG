
from fastapi import FastAPI
from fastapi_admin.app import app as admin_app

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API Admin is running"}

app.mount("/admin", admin_app)
