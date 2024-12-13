from abc import ABC, abstractmethod
from models.wallets.stocks.Stock import Stock


class ICreateStockRepo(ABC):
    @abstractmethod
    def create(self, stock: Stock) -> Stock: ...
