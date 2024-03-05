from pydantic import BaseModel, EmailStr, SecretStr


class UserPost(BaseModel):
    name: str
    email: EmailStr
    password: SecretStr

    class Config:
        from_attributes = True
