from typing import Optional, Union
from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import EmailStr
from repos import user
from schemas.pydantic.user import UserPost
from schemas.pydantic.user import User
from services.user.LoadService import LoadService

LoadRouter = APIRouter(prefix="/user", tags=["v1", "user"])


@LoadRouter.get("/load/{userData}&{all}", response_model=Union[User, list[User]])
async def load(
    response: Response,
    userData: str | EmailStr = "",
    loadService: LoadService = Depends(LoadService),
    all: bool = False,
) -> User | list[User] | Response:
    try:
        data = await loadService.execute(userData, all=all)
        if data is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        response.status_code = status.HTTP_200_OK
        return data
    except Exception as e:
        print(f"Error: {e.__str__()}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response
