from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="UltraKG API")

# Mount the static files directory from the frontend/web location
app.mount("/static", StaticFiles(directory="/app/frontend/web/public"), name="static")

@app.get("/")
async def read_index():
    index_path = "/app/frontend/web/public/index.html"
    if os.path.exists(index_path):
        return FileResponse(index_path)
    raise HTTPException(status_code=404, detail="Index file not found")

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 