from typing import List

from models.course import Course, CourseCreate

# Dummy in-memory store
fake_courses_db: List[Course] = []

class CourseService:
    def get_all_courses(self) -> List[Course]:
        return fake_courses_db

    def create_course(self, course_in: CourseCreate) -> Course:
        course = Course(id=len(fake_courses_db)+1, **course_in.dict())
        fake_courses_db.append(course)
        return course

    def get_course(self, course_id: int) -> Course:
        for c in fake_courses_db:
            if c.id == course_id:
                return c
        return None
