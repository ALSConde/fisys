from abc import ABC, abstractmethod
from models.wallets.Wallet import Wallet


class IUpdateWalletRepo(ABC):
    @abstractmethod
    def update_wallet(self, wallet: Wallet) -> Wallet: ...
