from abc import ABC, abstractmethod
from models.wallets.Categories import Categories


class ILoadCategoryRepo(ABC):
    @abstractmethod
    def load_first(self, **kwargs) -> Categories | None: ...

    @abstractmethod
    def load_all(self) -> list[Categories]: ...

    @abstractmethod
    def load_by(self, **kwargs) -> list[Categories] | Categories | None: ...
