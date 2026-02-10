import openai
import os

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_teacher_notes(text: str) -> str:
    """
    Generate teacher-style explanatory notes from academic text.
    """

    prompt = f"""
You are a university-level teacher.

Explain the following topic clearly for students.
Write structured explanatory notes in simple language.
Do NOT copy sentences exactly.
Explain concepts, mechanisms, and importance.

Topic content:
{text}
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response["choices"][0]["message"]["content"].strip()
