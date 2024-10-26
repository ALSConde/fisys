from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from repos import user
from schemas.pydantic.APIResponse import ApiResponse
from schemas.pydantic.user import UserPost
from schemas.pydantic.user import User
from services.user.LoadService import LoadService

LoadRouter = APIRouter(prefix="/user", tags=["v1", "user"])


@LoadRouter.get("/load/{userData}&{all}", response_model=ApiResponse[User | list[User]])
async def load(
    userData: str | EmailStr = "",
    loadService: LoadService = Depends(LoadService),
    all: bool = False,
) -> ApiResponse[User]:
    try:
        data = await loadService.execute(userData, all=all)
        print(f"data = {data}")
        if data is None:
            return ApiResponse(message="User not found", status_code=400)
        return ApiResponse(message="User found", status_code=200, body=data)
    except Exception as e:
        raise HTTPException(500, str(e))
