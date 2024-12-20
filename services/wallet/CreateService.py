from fastapi import Depends
from infra.sqlalchemy.wallet.AlchemyWalletRepo import AlchemyWalletRepo
from models.User import User
from models.wallets.Wallet import Wallet
from repos.wallet.IWalletRepo import IWalletRepo
from schemas.pydantic.wallet.WalletPost import WalletPost
from services.contracts.Service import IService


class CreateService(IService[WalletPost, Wallet]):
    wallet_repo: IWalletRepo

    def __init__(self, wallet_repo: IWalletRepo = Depends(AlchemyWalletRepo)) -> None:
        self.wallet_repo = wallet_repo

    async def execute(self, dto: WalletPost, user: User) -> Wallet:

        if self.wallet_repo.load_by(name=dto.name, user_id=user.id):
            raise ValueError("Wallet already exists")
        
        return await self.wallet_repo.create(
            Wallet(
                name=dto.name,
                user_id=user.id,
            )
        )
