from pydantic import BaseModel
from typing import List, Optional

class Lesson(BaseModel):
    id: int
    title: str
    content: str
    video_url: Optional[str] = None

class Module(BaseModel):
    id: int
    title: str
    lessons: List[Lesson]

class Course(BaseModel):
    id: int
    title: str
    description: str
    modules: List[Module]

class CourseCreate(BaseModel):
    title: str
    description: str
    modules: List[Module]
