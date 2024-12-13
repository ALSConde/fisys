from abc import ABC, abstractmethod


class IDeleteBuyRepo(ABC):
    @abstractmethod
    def delete_buy(self, buy_id: int) -> None: ...
