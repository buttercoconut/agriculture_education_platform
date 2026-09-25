from typing import List
from models.course import Course

# Dummy in-memory store
COURSES: List[Course] = []

class CourseService:
    @staticmethod
    def list_courses() -> List[Course]:
        return COURSES

    @staticmethod
    def create_course(course_in) -> Course:
        new_id = len(COURSES) + 1
        course = Course(id=new_id, title=course_in.title, description=course_in.description, tags=course_in.tags, lessons=[])
        COURSES.append(course)
        return course
