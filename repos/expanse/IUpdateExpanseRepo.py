from abc import ABC, abstractmethod
from models.wallets.Expanse import Expanse


class IUpadteExpanseRepo(ABC):
    @abstractmethod
    def update(self, expanse_id: int, expanse: Expanse) -> Expanse: ...
