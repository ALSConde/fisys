from fastapi import Depends
from infra.sqlalchemy.wallet.AlchemyWalletRepo import AlchemyWalletRepo
from models.User import User
from models.wallets.Wallet import Wallet
from repos.wallet.IWalletRepo import IWalletRepo
from schemas.pydantic.wallet.WalletPost import WalletPost
from schemas.pydantic.wallet.WalletUpdate import WalletUpdate
from services.contracts.Service import IService


class UpdateService(IService[WalletUpdate, Wallet]):
    wallet_repo: IWalletRepo

    def __init__(self, wallet_repo: IWalletRepo = Depends(AlchemyWalletRepo)) -> None:
        self.wallet_repo = wallet_repo

    async def execute(self, dto: WalletUpdate, wallet_id: int, user: User) -> Wallet:
        wallet = await self.wallet_repo.load_by(id=wallet_id, user_id=user.id)

        if not wallet:
            raise ValueError("Wallet not found")

        wallet.__dict__.update(dto.model_dump(exclude_unset=True))

        wallet = await self.wallet_repo.update(wallet_id, wallet)

        return wallet
