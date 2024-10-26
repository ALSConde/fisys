from fastapi import APIRouter, Depends, HTTPException
from schemas.pydantic.APIResponse import ApiResponse
from schemas.pydantic.user import UserPost
from schemas.pydantic.user import User
from services.user.CreateService import CreateService
CreateRouter = APIRouter(prefix="/user", tags=["v1", "user"])


@CreateRouter.post("/create/", response_model=ApiResponse[User])
async def create(
    userData: UserPost, createService: CreateService = Depends(CreateService)
) -> ApiResponse[User]:
    try:
        data = await createService.execute(userData)
        if data is None:
            return ApiResponse(message="User already exists", status_code=400)
        return ApiResponse(message="User created successfully", status_code=200)
    except Exception as e:
        raise HTTPException(500, str(e))
