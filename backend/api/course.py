from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from models.course import Course, CourseCreate
from services.course_service import CourseService

router = APIRouter()

course_service = CourseService()

@router.get("/", response_model=List[Course])
async def list_courses():
    return course_service.get_all_courses()

@router.post("/", response_model=Course)
async def create_course(course_in: CourseCreate):
    return course_service.create_course(course_in)

@router.get("/{course_id}", response_model=Course)
async def get_course(course_id: int):
    course = course_service.get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
