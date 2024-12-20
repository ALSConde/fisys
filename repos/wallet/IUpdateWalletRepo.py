from abc import ABC, abstractmethod
from models.wallets.Wallet import Wallet


class IUpdateWalletRepo(ABC):
    @abstractmethod
    def update(self, wallet_id: int, wallet: Wallet) -> Wallet: ...
