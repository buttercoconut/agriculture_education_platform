from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.user import router as user_router
from api.course import router as course_router
from api.community import router as community_router

app = FastAPI(title="Agriculture Education Platform API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(course_router, prefix="/courses", tags=["courses"])
app.include_router(community_router, prefix="/community", tags=["community"])

@app.get("/")
async def root():
    return {"message": "Welcome to Agriculture Education Platform API"}
