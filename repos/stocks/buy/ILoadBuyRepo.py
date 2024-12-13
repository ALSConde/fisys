from abc import ABC, abstractmethod
from models.wallets.stocks.StockBuyHistory import StockBuyHistory


class ILoadBuyRepo(ABC):
    @abstractmethod
    def load(self, buy_id: str) -> StockBuyHistory: ...
