from abc import ABC, abstractmethod
from models.wallets.stocks.Stock import Stock


class IUpdateStockRepo(ABC):
    @abstractmethod
    def update_stock(self, stock: Stock) -> Stock: ...
