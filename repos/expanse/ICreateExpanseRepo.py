from abc import ABC, abstractmethod
from models.wallets.Expense import Expanse


class ICreateExpanseRepo(ABC):
    @abstractmethod
    def create(self, expanse: Expanse) -> Expanse: ...
