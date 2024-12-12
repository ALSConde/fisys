from typing import Annotated, Optional
from fastapi import Depends
from exceptions.APIError import APIError
from exceptions.user.UserNotFound import UserNotFound
from infra.sqlalchemy.user.AlchemyUserRepo import AlchemyUserRepo
from models.User import User
from repos.user.IUserRepo import IUserRepo
from schemas.pydantic.user.UserPost import UserPost
from schemas.pydantic.user.UserUpdate import UserUpdate
from services.contracts.Service import IService


class UpdateService(IService[UserUpdate, User]):
    user_repo: IUserRepo

    def __init__(self, user_repo: IUserRepo = Depends(AlchemyUserRepo)) -> None:
        self.user_repo = user_repo

    async def execute(self, user: UserUpdate, id: int) -> User:
        try:

            old_user = await self.user_repo.load_active_first(id=id)

            if not old_user:
                raise UserNotFound()

            old_user.__dict__.update(user.model_dump(exclude_unset=True))

            new_user = await self.user_repo.update(id, old_user)

            return new_user

        except UserNotFound as e:
            raise e
        except APIError as e:
            raise APIError(500, "Unexpected error")
