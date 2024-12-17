from pydantic import BaseModel, ConfigDict, EmailStr, SecretStr


class UserPost(BaseModel):
    name: str
    email: EmailStr
    password: SecretStr

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "testuser",
                "email": "example.user@email.com",
                "password": "examplepassword",
            }
        },
        from_attributes=True,
    )
