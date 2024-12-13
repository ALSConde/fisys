from abc import ABC, abstractmethod
from models.wallets.stocks.Stock import Stock


class IUpdateStockRepo(ABC):
    @abstractmethod
    def update(self, stock: Stock) -> Stock: ...
