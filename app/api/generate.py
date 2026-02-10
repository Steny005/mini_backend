from fastapi import APIRouter, UploadFile, File, Form 
from app.models.schemas import LessonOutput
from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_text
from app.core.chunker import chunk_text
from app.core.notes_builder import build_notes_from_chunks
import os
import shutil

router = APIRouter()

@router.post("/generate", response_model=LessonOutput)
async def generate_lesson(
    file: UploadFile = File(...),
    duration: int = Form(...)
):
    file_path = f"data/uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    raw_text = extract_text_from_pdf(file_path)

    cleaned_text = clean_text(raw_text)

    chunks = chunk_text(cleaned_text, max_words=200)

    notes = build_notes_from_chunks(chunks, duration)

    return {
        "total_duration": duration,
        "notes": notes,
        "learning_flow": [],
        "activities": []
    }
    