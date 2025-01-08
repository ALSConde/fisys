from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)