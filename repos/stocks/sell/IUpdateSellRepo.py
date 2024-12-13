from abc import ABC, abstractmethod
from models.wallets.stocks.StockSellHistory import StockSellHistory


class IUpdateSellRepo(ABC):
    @abstractmethod
    def update_Sell(self, Sell: StockSellHistory) -> StockSellHistory: ...
