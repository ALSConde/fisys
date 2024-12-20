from abc import ABC, abstractmethod
from models.wallets.Expense import Expanse


class IUpadteExpanseRepo(ABC):
    @abstractmethod
    def update(self, expanse_id: int, expanse: Expanse) -> Expanse: ...
