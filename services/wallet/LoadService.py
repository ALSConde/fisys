from fastapi import Depends, logger
from infra.sqlalchemy.wallet.AlchemyWalletRepo import AlchemyWalletRepo
from models.User import User
from models.wallets.Wallet import Wallet
from repos.wallet.IWalletRepo import IWalletRepo
from services.contracts.Service import IService


class LoadService(IService[User, Wallet]):
    wallet_repo: IWalletRepo

    def __init__(self, wallet_repo: IWalletRepo = Depends(AlchemyWalletRepo)) -> None:
        self.wallet_repo = wallet_repo

    async def execute(self, dto: User) -> Wallet:
        wallets = await self.wallet_repo.load_by(user_id=dto.id)
        if not wallets:
            raise ValueError("Wallets not found")

        return wallets
