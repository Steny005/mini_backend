from  typing import List
from pydantic import BaseModel

class NotesSection(BaseModel):
    heading: str
    explanation: str
    estimated_minutes: int

class LearningFlowStep(BaseModel):
    step_number: int
    description: str

class Activity(BaseModel):
    type: str
    name: str
    description: str

class LessonOutput:
    total_duration: int
    notes: List[NotesSection]
    learning_flow: List[LearningFlowStep]
    activities: List[Activity] 