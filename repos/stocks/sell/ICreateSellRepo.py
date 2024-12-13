from abc import ABC, abstractmethod
from models.wallets.stocks.StockSellHistory import StockSellHistory


class ICreateSellRepo(ABC):
    @abstractmethod
    def create(self, sell: StockSellHistory) -> StockSellHistory: ...
