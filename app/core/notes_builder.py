from app.core.ai_generator import generate_teacher_notes

def build_notes_from_chunks(chunks: list[str]):
    """
    Builds AI-generated teacher-style notes from text chunks
    """

    notes = []

    for idx, chunk in enumerate(chunks, start=1):
        explanation = generate_teacher_notes(chunk)

        notes.append({
            "heading": f"Section {idx}",
            "explanation": explanation
        })

    return notes
