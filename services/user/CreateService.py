from fastapi import Depends
from infra.sqlalchemy.user.AlchemyUserRepo import AlchemyUserRepo
from models import User
from repos.user.IUserRepo import IUserRepo
from schemas.pydantic.user import UserPost, User as PydanticUser
from services.contracts.Service import IService


class CreateService(IService[UserPost, User]):
    user_repo: IUserRepo

    def __init__(self, user_repo: IUserRepo = Depends(AlchemyUserRepo)) -> None:
        self.user_repo = user_repo

    async def execute(self, dto: UserPost) -> PydanticUser | None:
        user = await self.user_repo.load_by(email=dto.email)
        if user is None:

            data = await self.user_repo.create(
                User(name=dto.name, email=dto.email, password=dto.password)
            )

            return data
        else:
            return None
