from services.contracts.Service import IService
from passlib.context import CryptContext


class Secret(IService):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self) -> None:
        pass

    async def execute(self, **kwargs):
        if kwargs.fromkeys("hash_password"):
            return self.hash_password(kwargs["hash_password"])
        if kwargs.fromkeys("verify_password"):
            return self.verify_password(
                kwargs["verify_password"], kwargs["hashed_password"]
            )

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)
