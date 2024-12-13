from abc import ABC, abstractmethod


class IDeleteWalletRepo(ABC):
    @abstractmethod
    def delete_wallet(self, wallet_id: str) -> bool: ...
