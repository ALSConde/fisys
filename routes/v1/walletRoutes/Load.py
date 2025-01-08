from typing import Annotated
from fastapi import APIRouter, Depends, logger
from fastapi.responses import JSONResponse
from models.User import User
from schemas.pydantic.wallet.Wallet import Wallet
from services.auth.user.CurrentUser import get_current_user
from services.contracts.Service import IService
from services.wallet.LoadService import LoadService


LoadRouter = APIRouter(prefix="/wallet", tags=["v1", "wallet"])


@LoadRouter.get("/load/", response_model=list[Wallet])
async def load(
    currentUser: Annotated[User, Depends(get_current_user)],
    loadService: IService = Depends(LoadService),
):
    try:
        wallets = await loadService.execute(currentUser)
        return wallets
    except Exception as e:
        raise e
