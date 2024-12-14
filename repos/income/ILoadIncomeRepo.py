from abc import ABC, abstractmethod
from models.wallets.Income import Income


class ILoadIncomeRepo(ABC):
    @abstractmethod
    def load_first(self, **kwargs) -> Income | None: ...

    @abstractmethod
    def load_all(self) -> list[Income]: ...

    @abstractmethod
    def load_by(self, **kwargs) -> list[Income] | Income | None: ...
