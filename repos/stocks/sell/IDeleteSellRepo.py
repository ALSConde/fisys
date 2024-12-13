from abc import ABC, abstractmethod


class IDeleteSellRepo(ABC):
    @abstractmethod
    def delete(self, sell_id: int) -> None: ...
