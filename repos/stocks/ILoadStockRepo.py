from abc import ABC, abstractmethod
from models.wallets.stocks.Stock import Stock


class ILoadStockRepo(ABC):
    @abstractmethod
    def load(self, stock_id: str) -> Stock: ...
