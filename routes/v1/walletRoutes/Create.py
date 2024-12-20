from typing import Annotated
from fastapi import APIRouter, Depends, Response, status
from fastapi.logger import logger
from fastapi.responses import JSONResponse
from exceptions import APIError
from models.User import User
from schemas.pydantic.wallet.WalletPost import WalletPost
from services.contracts.Service import IService
from services.wallet.CreateService import CreateService
from services.auth.user.CurrentUser import get_current_user

CreateRouter = APIRouter(prefix="/wallet", tags=["v1", "wallet"])


@CreateRouter.post("/create/", status_code=status.HTTP_201_CREATED)
async def create(
    walletData: WalletPost,
    current_user: Annotated[User, Depends(get_current_user)],
    createService: IService = Depends(CreateService),
) -> Response:
    try:

        await createService.execute(walletData, user=current_user)

        return JSONResponse(
            content={"detail": "Wallet created successfully"},
            status_code=status.HTTP_201_CREATED,
        )
    except APIError as e:
        logger.error(e.message)
        raise e
