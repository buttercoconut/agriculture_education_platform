from typing import List, Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext

from models.user import User, UserCreate, UserInDB

# Dummy in-memory store
fake_users_db = {
    "alice": {"username": "alice", "email": "alice@example.com", "hashed_password": "$2b$12$KIXQ1YyqS/fWznuaCG2l9uOAXoJ1i8LojRxurx8Wc1SUg/K3PaYy", "id": 1, "is_active": True},
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class UserService:
    def get_user(self, username: str) -> Optional[UserInDB]:
        user_dict = fake_users_db.get(username)
        if user_dict:
            return UserInDB(**user_dict)
        return None

    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        user = self.get_user(username)
        if not user or not pwd_context.verify(password, user.hashed_password):
            return None
        return User(**user.dict())

    def create_user(self, user_in: UserCreate) -> User:
        hashed_password = pwd_context.hash(user_in.password)
        user_dict = user_in.dict()
        user_dict.update({"hashed_password": hashed_password, "id": len(fake_users_db)+1, "is_active": True})
        fake_users_db[user_in.username] = user_dict
        return User(**user_dict)

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = self.get_user(username)
        if user is None:
            raise credentials_exception
        return User(**user.dict())
