from abc import ABC, abstractmethod
from models.wallets.stocks.Stock import Stock


class ILoadStockRepo(ABC):
    @abstractmethod
    def load_all(self) -> list[Stock]: ...

    @abstractmethod
    def load_by(self, **kwargs) -> Stock | list[Stock] | None: ...

    @abstractmethod
    def load_first(self, **kwargs) -> Stock | None: ...
