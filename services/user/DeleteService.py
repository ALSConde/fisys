from typing import Optional

from fastapi import Depends
from exceptions.user.UserNotFound import UserNotFound
from infra.sqlalchemy.user.AlchemyUserRepo import AlchemyUserRepo
from models.User import User
from repos.user.IUserRepo import IUserRepo
from schemas.pydantic.user.UserPost import UserPost
from services.contracts.Service import IService


class DeleteService(IService[UserPost, User]):
    user_repo: IUserRepo

    def __init__(self, user_repo: IUserRepo = Depends(AlchemyUserRepo)) -> None:
        self.user_repo = user_repo

    async def execute(self, id) -> Optional[int]:
        if await self.user_repo.load_active_first(id=id):
            await self.user_repo.delete(id)
            return id
        else:
            raise UserNotFound()
        
