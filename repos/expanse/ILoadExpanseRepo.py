from abc import ABC, abstractmethod
from models.wallets.Expanse import Expanse


class ILoadExpanseRepo(ABC):
    @abstractmethod
    def load_first(self, **kwargs) -> Expanse | None: ...

    @abstractmethod
    def load_all(self) -> list[Expanse]: ...

    @abstractmethod
    def load_by(self, **kwargs) -> list[Expanse] | Expanse | None: ...
