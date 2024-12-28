from typing import Optional
from fastapi import Depends
from infra.sqlalchemy.wallet.AlchemyWalletRepo import AlchemyWalletRepo
from models.User import User
from models.wallets.Wallet import Wallet
from repos.wallet.IWalletRepo import IWalletRepo
from schemas.pydantic.wallet.WalletPost import WalletPost
from services.contracts.Service import IService


class DeleteService(IService[WalletPost, User]):
    wallet_repo: IWalletRepo

    def __init__(self, wallet_repo: IWalletRepo = Depends(AlchemyWalletRepo)) -> None:
        self.wallet_repo = wallet_repo

    async def execute(self, id) -> Optional[int]:
        wallet = await self.wallet_repo.load_by(id=id)
        if wallet:
            await self.wallet_repo.delete(id)
            return id
        else:
            return None