from typing import List

from models.community import CommunityPost, CommunityPostCreate

# Dummy in-memory store
fake_posts_db: List[CommunityPost] = []

class CommunityService:
    def get_all_posts(self) -> List[CommunityPost]:
        return fake_posts_db

    def create_post(self, post_in: CommunityPostCreate) -> CommunityPost:
        post = CommunityPost(id=len(fake_posts_db)+1, **post_in.dict(), created_at=datetime.utcnow().isoformat())
        fake_posts_db.append(post)
        return post
