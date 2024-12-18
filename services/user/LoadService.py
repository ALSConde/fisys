from typing import Annotated, Optional, Union
from fastapi import Depends
from pydantic import EmailStr
from infra.sqlalchemy.user.AlchemyUserRepo import AlchemyUserRepo
from repos.user.IUserRepo import IUserRepo
from schemas.pydantic.user import UserPost
from services.contracts.Service import IService
from models.User import User


class LoadService(IService[Annotated[UserPost, Optional[UserPost]], User]):
    user_repo: IUserRepo

    def __init__(self, user_repo: IUserRepo = Depends(AlchemyUserRepo)) -> None:
        self.user_repo = user_repo

    async def execute(self, dto: str | EmailStr, **kwargs) -> Optional[Union[User, list[User]]]:
        if kwargs["all"]:
            data = await self.user_repo.load_all_actives()
        else:
            data = await self.user_repo.load_actives_by(email=dto)

        return data

    async def load_all_by_email(self, email: str | EmailStr) -> list[User] | None:
        data = await self.user_repo.load_by(email=email)
        return data