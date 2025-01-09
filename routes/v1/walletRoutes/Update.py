from fastapi import APIRouter, Depends, Response

from models.User import User
from schemas.pydantic.wallet.WalletUpdate import WalletUpdate
from services.auth.user.CurrentUser import get_current_user
from services.wallet.UpdateService import UpdateService


updateRouter = APIRouter(prefix="/wallet", tags=["v1", "wallet"])


@updateRouter.patch("/update/{id}")
async def update(
    id: int,
    response: Response,
    wallet: WalletUpdate,
    current_user: User = Depends(get_current_user),
    update_service: UpdateService = Depends(UpdateService),
):
    try:
        data = await update_service.execute(wallet, id, current_user)
        response.status_code = 204
        if not data:
            response.status_code = 404
        return response
    except Exception as e:
        response.status_code = 500
        return response
