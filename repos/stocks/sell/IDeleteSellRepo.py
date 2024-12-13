from abc import ABC, abstractmethod


class IDeleteSellRepo(ABC):
    @abstractmethod
    def delete_buy(self, sell_id: int) -> None: ...
