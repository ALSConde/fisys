from .BaseModel import BaseModel
from configs.Environment import get_env
from datetime import datetime, timedelta
from jose import jwt
from sqlalchemy import Column, Integer, String


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    def normalize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }

    def check_password(self, password: str) -> bool:
        return bool(self.password == password)

    
