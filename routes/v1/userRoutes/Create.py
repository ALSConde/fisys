from fastapi import APIRouter, Depends, Response, status
from fastapi.logger import logger
from fastapi.responses import JSONResponse
from exceptions.APIError import APIError
from exceptions.user.UserAlreadyExists import UserAlreadyExists
from schemas.pydantic.user import UserPost
from services.user.CreateService import CreateService

CreateRouter = APIRouter(prefix="/user", tags=["v1", "user"])


@CreateRouter.post("/create/", status_code=status.HTTP_201_CREATED)
async def create(
    userData: UserPost,
    createService: CreateService = Depends(CreateService),
) -> Response:
    try:
        await createService.execute(userData)

        return JSONResponse(
            content={"detail": "User created successfully"},
            status_code=status.HTTP_201_CREATED,
        )
    except APIError as e:
        logger.error(e.message)
        raise e
