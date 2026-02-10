from fastapi import APIRouter, UploadFile, File
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
from app.models.schemas import LessonOutput
from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_text
from app.core.chunker import chunk_text
from app.core.notes_builder import build_notes_from_chunks
import shutil
import os

router = APIRouter()

@router.post("/generate", response_model=LessonOutput)
async def generate_lesson(
    file: Optional[UploadFile] = File(None),
    text: Optional[str] = Form(None)
):

    if not file and not text:
        raise HTTPException(
            status_code=400,
            detail="Either a PDF file or text input must be provided."
        )

    # 1. Get raw text
    if file:
        file_path = f"data/uploads/{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        raw_text = extract_text_from_pdf(file_path)

    else:
        raw_text = text

    # 2. Clean text
    cleaned_text = clean_text(raw_text)

    # 3. Chunk text
    chunks = chunk_text(cleaned_text, max_words=200)

    # 4. Generate notes
    notes = build_notes_from_chunks(chunks)

    return {
        "topic": file.filename if file else "Custom Text Input",
        "notes": notes,
        "learning_flow": [],
        "activities": []
    }

