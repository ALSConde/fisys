from fastapi import Depends
from exceptions.APIError import APIError
from exceptions.wallet.WalletAlreadyExists import WalletAlreadyExists
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
        try:
            wallet = await self.wallet_repo.load_by(name=dto.name, user_id=user.id)

            if not wallet:
                return await self.wallet_repo.create(
                    Wallet(
                        name=dto.name,
                        user_id=user.id,
                    )
                )
            else:
                raise WalletAlreadyExists()
        except WalletAlreadyExists as e:
            raise e
        except APIError:
            raise APIError(500, "Unexpected error")
