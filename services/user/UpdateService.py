from typing import Annotated, Optional
from fastapi import Depends
from infra.sqlalchemy.user.AlchemyUserRepo import AlchemyUserRepo
from models.User import User
from repos.user.IUserRepo import IUserRepo
from schemas.pydantic.user.UserPost import UserPost
from services.contracts.Service import IService


class UpdateService(IService[Annotated[UserPost, Optional[UserPost]], User]):
    user_repo: IUserRepo

    def __init__(self, user_repo: IUserRepo = Depends(AlchemyUserRepo)) -> None:
        self.user_repo = user_repo

    async def execute(self, dto: UserPost, **kwargs) -> User | None:
        user = await self.user_repo.load_by(email=dto.email)
        if user is not None:
            data = await self.user_repo.update(
                user.id,
                User(id=user.id, name=dto.name, email=dto.email, password=dto.password),
            )
            return data
        else:
            return None
