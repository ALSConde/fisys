from pydantic import BaseModel


class SecretResolve(BaseModel):
    hash_password: str | None = None
    verify_password: str | None = None
