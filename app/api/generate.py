from fastapi import APIRouter, UploadFile, File, Form 
from app.models.schemas import LessonOutput

router = APIRouter()

@router.post("/generate", response_model=LessonOutput)
async def generate_lesson(
    file: UploadFile = File(...),
    duration: int = Form(...)
):

    return {
        "total_duration": duration,
        "notes": [
            {
                "heading": "Introduction",
                "explanation": "This section introduces the topic.",
                "estimated_minutes": duration // 2
            }
        ],
        "learning_flow": [
            {
                "step_number": 1,
                "description": "Introduce the core concept."
            }
        ],
        "activities": [
            {
                "type": "familiar",
                "name": "Think–Pair–Share",
                "description": "Discuss the main idea with a classmate."
            },
            {
                "type": "innovative",
                "name": "Error Spotting",
                "description": "Find incorrect statements in a set."
            }
        ]
    }
    