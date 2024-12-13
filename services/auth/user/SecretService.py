from typing import Optional
from schemas.pydantic.auth.login.LoginDTO import LoginDTO
from schemas.pydantic.auth.login.SecretResolve import SecretResolve
from services.contracts.Service import IService
from passlib.context import CryptContext


class SecretService(IService[LoginDTO, SecretResolve]):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self) -> None:
        pass

    async def execute(self, dto, **kwargs):
        if "hash_password" in kwargs and type(dto) == LoginDTO:
            return await self.hash_password(dto.password)
        elif "hash_password" in kwargs and type(dto) == str:
            return await self.hash_password(dto)
        elif (
            "verify_password" in kwargs
            and "hashed_password" in kwargs
            and type(dto) == str
        ):
            return self.verify_password(dto, kwargs["hashed_password"])
        else:
            return None

    async def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)
