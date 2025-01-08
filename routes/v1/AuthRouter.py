from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from exceptions.login.LoginExceptions import InvalidCredentials
from schemas.pydantic.auth import Token
from schemas.pydantic.auth.login.LoginDTO import LoginDTO
from services.auth.login import LoginService
from services.contracts.Service import IService

AuthRouter = APIRouter(prefix="/auth", tags=["v1", "auth"])


@AuthRouter.post("/login")
async def login(
    form: OAuth2PasswordRequestForm = Depends(), loginService: IService = Depends(LoginService)
) -> Token:
    try:
        return await loginService.execute(
            LoginDTO(email=form.username, password=form.password)
        )
    except InvalidCredentials as e:
        raise HTTPException(status_code=401, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
