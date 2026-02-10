from fastapi import FastAPI
from app.api.ingest import router as ingest_router

app = FastAPI(title="Learngenie Backend")
app.include_router(ingest_router)
@app.get("/")
def health():
	return {"status":"ok"}

