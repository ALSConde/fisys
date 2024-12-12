from fastapi import APIRouter, Depends, Response

from services.user.DeleteService import DeleteService


DeleteRouter = APIRouter(prefix="/user", tags=["v1", "user"])


@DeleteRouter.delete("/delete/{id}")
async def delete(
    id: int, response: Response, delete_service: DeleteService = Depends(DeleteService)
):
    try:
        data = await delete_service.execute(id)
        response.status_code = 204
        if not data:
            response.status_code = 404
        return response
    except Exception as e:
        response.status_code = 500
        return response
