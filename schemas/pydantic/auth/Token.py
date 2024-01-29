from datetime import datetime, timedelta, timezone
from jose import jwt
from pydantic import BaseModel

from configs.Environment import get_env

env = get_env()


class Token(BaseModel):
    access_token: str
    token_type: str

    @staticmethod
    def create_token(user: dict, expires_delta: timedelta | None = None):
        to_encode = user.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, env.JWT_SECRET_KEY, algorithm=env.JWT_ALGORITHM)
        return encoded_jwt
