from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Optional

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Simplified: return token as user
    return token
