from fastapi import APIRouter, Depends
from typing import List

from models.community import CommunityPost, CommunityPostCreate
from services.community_service import CommunityService

router = APIRouter()

community_service = CommunityService()

@router.get("/posts", response_model=List[CommunityPost])
async def list_posts():
    return community_service.get_all_posts()

@router.post("/posts", response_model=CommunityPost)
async def create_post(post_in: CommunityPostCreate):
    return community_service.create_post(post_in)
