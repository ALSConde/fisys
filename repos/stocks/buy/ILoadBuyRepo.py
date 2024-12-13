from abc import ABC, abstractmethod
from models.wallets.stocks.StockBuyHistory import StockBuyHistory


class ILoadBuyRepo(ABC):
    @abstractmethod
    def load_all(self) -> list[StockBuyHistory]: ...

    @abstractmethod
    def load_by(self, **kwargs) -> StockBuyHistory | list[StockBuyHistory] | None: ...

    @abstractmethod
    def load_first(self, **kwargs) -> StockBuyHistory | None: ...
