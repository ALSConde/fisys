from typing import Optional
from pydantic import BaseModel, EmailStr, SecretStr


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[SecretStr] = None
    
