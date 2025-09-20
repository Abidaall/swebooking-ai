from fastapi import FastAPI
from .core.config import settings
from .db.session import init_db
from .api.routes import router as api_router

app = FastAPI(title="SweBookkeeping AI (MVP)")

@app.on_event("startup")
async def startup_event():
    init_db()

app.include_router(api_router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok", "env": settings.BANKID_ENV}
