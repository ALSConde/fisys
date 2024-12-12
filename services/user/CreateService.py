from typing import Union
from fastapi import Depends
from exceptions.APIError import APIError
from exceptions.user.UserAlreadyExists import UserAlreadyExists
from infra.sqlalchemy.user.AlchemyUserRepo import AlchemyUserRepo
from models import User
from repos.user.IUserRepo import IUserRepo
from schemas.pydantic.user import UserPost, User as PydanticUser
from services.auth.user.Secret import Secret
from services.contracts.Service import IService


class CreateService(IService[UserPost, User]):
    user_repo: IUserRepo

    def __init__(self, user_repo: IUserRepo = Depends(AlchemyUserRepo)) -> None:
        self.user_repo = user_repo

    async def execute(self, dto: UserPost) -> Union[PydanticUser, Exception, None]:
        try:
            user = await self.user_repo.load_by(email=dto.email)
            print(f"User: {user}")
            if user is None or len(user) == 0:
                secret = Secret()
                
                data = await self.user_repo.create(
                    User(
                        name=dto.name,
                        email=dto.email,
                        password=await secret.execute(
                            hash_password=dto.password.get_secret_value()
                        ),
                    )
                )

                return data
            else:
                raise UserAlreadyExists()
        except UserAlreadyExists as e:
            raise e
        except APIError as e:
            raise APIError(500, "Unexpected error")
