from abc import ABC, abstractmethod
from models.wallets.stocks.StockBuyHistory import StockBuyHistory


class IUpdateBuyRepo(ABC):
    @abstractmethod
    def update(self, buy_id: int, buy: StockBuyHistory) -> StockBuyHistory: ...
