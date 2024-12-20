from abc import ABC, abstractmethod


class IDeleteWalletRepo(ABC):
    @abstractmethod
    def delete(self, wallet_id: str) -> bool: ...
