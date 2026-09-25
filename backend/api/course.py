from fastapi import APIRouter, Depends
from typing import List

from models.course import Course, CourseCreate
from services.course_service import CourseService
from dependencies import get_current_user

router = APIRouter()

@router.get("/", response_model=List[Course])
async def list_courses(user=Depends(get_current_user)):
    return CourseService.list_courses()

@router.post("/", response_model=Course)
async def create_course(course_in: CourseCreate, user=Depends(get_current_user)):
    return CourseService.create_course(course_in)
