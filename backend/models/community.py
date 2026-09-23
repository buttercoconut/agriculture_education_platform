from pydantic import BaseModel
from typing import List

class CommunityPost(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    created_at: str

class CommunityPostCreate(BaseModel):
    user_id: int
    title: str
    content: str
