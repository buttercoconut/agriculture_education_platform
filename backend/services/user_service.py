from typing import Optional
from models.user import User, UserCreate

# Dummy in-memory store
USERS: List[User] = []

class UserService:
    @staticmethod
    def get_user_by_email(email: str) -> Optional[User]:
        for u in USERS:
            if u.email == email:
                return u
        return None

    @staticmethod
    def authenticate_user(email: str, password: str) -> Optional[User]:
        user = UserService.get_user_by_email(email)
        if user and user.password == password:  # Simplified; use hashing in real
            return user
        return None

    @staticmethod
    def create_user(user_in: UserCreate) -> User:
        new_id = len(USERS) + 1
        user = User(id=new_id, email=user_in.email, full_name=user_in.full_name, is_active=True)
        USERS.append(user)
        return user

    @staticmethod
    def create_access_token(data: dict, expires_delta=None):
        import jwt
        from datetime import datetime, timedelta
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, "supersecretkey", algorithm="HS256")
        return encoded_jwt
