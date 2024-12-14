from abc import ABC, abstractmethod
from models.wallets.Expanse import Expanse


class ICreateExpanseRepo(ABC):
    @abstractmethod
    def create(self, expanse: Expanse) -> Expanse: ...
