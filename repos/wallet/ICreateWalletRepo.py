from abc import ABC, abstractmethod

from models.wallets.Wallet import Wallet


class ICreateWalletRepo(ABC):
    @abstractmethod
    async def create(self, wallet: Wallet) -> Wallet: ...
