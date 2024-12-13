from abc import ABC, abstractmethod
from models.wallets.stocks.StockSellHistory import StockSellHistory


class ILoadSellRepo(ABC):
    @abstractmethod
    def load(self, sell_id: str) -> StockSellHistory: ...
