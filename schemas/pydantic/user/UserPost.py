from pydantic import BaseModel, EmailStr


class UserPost(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True
