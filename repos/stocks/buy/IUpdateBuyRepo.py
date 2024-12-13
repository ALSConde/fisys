from abc import ABC, abstractmethod
from models.wallets.stocks.StockBuyHistory import StockBuyHistory


class IUpdateBuyRepo(ABC):
    @abstractmethod
    def update_buy(self, buy: StockBuyHistory) -> StockBuyHistory: ...
