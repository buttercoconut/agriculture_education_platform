from pydantic import BaseModel
from typing import List

class LessonBase(BaseModel):
    title: str
    content: str
    video_url: Optional[str] = None

class LessonCreate(LessonBase):
    pass

class Lesson(LessonBase):
    id: int
    module_id: int
    class Config:
        orm_mode = True
