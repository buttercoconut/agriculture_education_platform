from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import user, course, qna

app = FastAPI(title="Agriculture Education Platform API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api/user", tags=["user"])
app.include_router(course.router, prefix="/api/course", tags=["course"])
app.include_router(qna.router, prefix="/api/qna", tags=["qna"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
