from abc import ABC, abstractmethod
from models.wallets.stocks.StockBuyHistory import StockBuyHistory


class ICreateBuyRepo(ABC):
    @abstractmethod
    def create(self, buy: StockBuyHistory) -> StockBuyHistory: ...
