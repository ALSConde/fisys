from abc import ABC, abstractmethod


class IDeleteWalletRepo(ABC):
    @abstractmethod
    async def delete(self, wallet_id: str) -> bool: ...
