from pydantic import BaseModel
from typing import List

class CourseBase(BaseModel):
    title: str
    description: str
    tags: List[str] = []

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int
    lessons: List[Lesson] = []
    class Config:
        orm_mode = True
