from fastapi import FastAPI
from app.api.ingest import router as ingest_router
from app.api.generate import router as generate_router
app = FastAPI(title="Learngenie Backend")
app.include_router(ingest_router)
app.include_router(generate_router)
@app.get("/")
def health():
	return {"status":"ok"}

