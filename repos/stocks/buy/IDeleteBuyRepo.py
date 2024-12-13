from abc import ABC, abstractmethod


class IDeleteBuyRepo(ABC):
    @abstractmethod
    def delete(self, buy_id: int) -> None: ...
