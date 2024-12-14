from abc import ABC, abstractmethod
from models.wallets.stocks.StockSellHistory import StockSellHistory


class IUpdateSellRepo(ABC):
    @abstractmethod
    def update(self, sell_id: int, Sell: StockSellHistory) -> StockSellHistory: ...
