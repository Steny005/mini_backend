from fastapi import APIRouter, UploadFile, File
import os
import shutil
from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_text
router = APIRouter()
UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
@router.post("/ingest")
async def ingest(file: UploadFile = File(...)):
	file_path = os.path.join(UPLOAD_DIR, file.filename)
	with open(file_path, "wb") as buffer:
		shutil.copyfileobj(file.file, buffer)
	raw_text = extract_text_from_pdf(file_path)
	cleaned_text = clean_text(raw_text)
	return{
	"filename": file.filename,
	"char_count": len(cleaned_text),
	"preview": cleaned_text[:400]
	}

