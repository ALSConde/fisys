from fastapi import Depends, HTTPException
from exceptions.login.LoginExceptions import InvalidCredentials
from exceptions.user.UserNotFound import UserNotFound
from infra.sqlalchemy.user.AlchemyUserRepo import AlchemyUserRepo
from models.User import User
from repos.user import IUserRepo
from schemas.pydantic.auth import Token
from schemas.pydantic.auth.login import LoginDTO
from services.auth.user.SecretService import SecretService
from services.contracts.Service import IService


class LoginService(IService[LoginDTO, Token]):
    user_repo: IUserRepo
    secretService: IService

    def __init__(
        self,
        user_repo: IUserRepo = Depends(AlchemyUserRepo),
        secretService: IService = Depends(SecretService),
    ) -> None:
        self.user_repo = user_repo
        self.secretService = secretService

    async def execute(self, dto: LoginDTO) -> Token:
        if dto.email is None or dto.password is None:
            raise InvalidCredentials()

        user = await self.user_repo.load_active_first(email=dto.email)
        
        if user is None:
            raise InvalidCredentials()
        
        if user.email != dto.email:
            raise InvalidCredentials()

        password_verified = await self.secretService.execute(
            dto=dto.password, verify_password=True,hashed_password=user.password
        )
        print(f"dto password: {password_verified}")
        if not password_verified:
            raise InvalidCredentials()

        jwt_token = Token.create_token(user.normalize())
        return Token(access_token=jwt_token, token_type="bearer")
