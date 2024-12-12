from fastapi import APIRouter, Depends, Response
from schemas.pydantic.user.UserUpdate import UserUpdate
from services.user.UpdateService import UpdateService


UpdateRouter = APIRouter(prefix="/user", tags=["v1", "user"])


@UpdateRouter.patch("/update/{id}")
async def update(
    id: int,
    response: Response,
    user: UserUpdate,
    update_service: UpdateService = Depends(UpdateService),
):
    try:
        data = await update_service.execute(user, id)
        response.status_code = 204
        if not data:
            response.status_code = 404
        return response
    except Exception as e:
        response.status_code = 500
        return response
