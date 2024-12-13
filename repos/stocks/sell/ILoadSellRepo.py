from abc import ABC, abstractmethod
from models.wallets.stocks.StockSellHistory import StockSellHistory


class ILoadSellRepo(ABC):
    @abstractmethod
    def load_all(self) -> list[StockSellHistory]: ...

    @abstractmethod
    def load_by(self, **kwargs) -> StockSellHistory | list[StockSellHistory] | None: ...

    @abstractmethod
    def load_first(self, **kwargs) -> StockSellHistory | None: ...
