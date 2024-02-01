from fastapi import Depends, HTTPException
from infra.sqlalchemy.user.AlchemyUserRepo import AlchemyUserRepo
from models.User import User
from repos.user import IUserRepo
from schemas.pydantic.APIResponse import ApiResponse
from schemas.pydantic.auth import Token
from schemas.pydantic.auth.login import LoginDTO
from services.contracts.Service import IService


class LoginService(IService[LoginDTO, Token]):
    user_repo: IUserRepo

    def __init__(self, user_repo : IUserRepo = Depends(AlchemyUserRepo)) -> None:
        self.user_repo = user_repo

    async def execute(self, dto: LoginDTO) -> Token:
        user = await self.user_repo.load_by(email=dto.email)
        if user is None:
            raise Exception("User not found")
        if not user.check_password(dto.password):
            raise Exception("Password is incorrect")
        
        jwt_token = Token.create_token(user)
        return Token(access_token=jwt_token, token_type="bearer")
