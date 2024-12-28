from abc import ABC, abstractmethod
from models.wallets.Wallet import Wallet


class IUpdateWalletRepo(ABC):
    @abstractmethod
    async def update(self, wallet_id: int, wallet: Wallet) -> Wallet: ...
