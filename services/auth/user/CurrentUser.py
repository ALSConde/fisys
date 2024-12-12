from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from infra.sqlalchemy.user.AlchemyUserRepo import AlchemyUserRepo
from repos.user.IUserRepo import IUserRepo
from schemas.pydantic.auth.login.TokenData import TokenData
from services.contracts.Service import IService
from configs.Environment import get_env

env = get_env()


class CurrentUser(IService):
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    user_repo: IUserRepo

    def __init__(self, user_repo: IUserRepo = Depends(AlchemyUserRepo)) -> None:
        self.user_repo = user_repo

    async def execute(
        self,
        token=Depends(oauth2_scheme),
    ):
        return await self.get_current_user(token)

    async def get_current_user(self, token):
        try:
            payload = jwt.decode(
                token, env.JWT_SECRET_KEY, algorithms=[env.JWT_ALGORITHM]
            )
            email = payload.get("sub")
            if email is None:
                raise Exception("Invalid token")
            token_data = TokenData(username=email)
        except JWTError:
            raise ValueError("Invalid token")

        user = self.user_repo.load_by(email=email)
        if user is None:
            raise Exception("User not found")
        return user
