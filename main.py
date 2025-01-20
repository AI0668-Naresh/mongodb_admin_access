from fastapi import FastAPI
import admin

app = FastAPI()

app.include_router(admin.router, prefix="/admin", tags=["Admin"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the MongoDB Admin Access API"}

@app.get("/health")
async def health_check():
    return {"status": "OK"}
