from abc import ABC, abstractmethod
from models.wallets.Income import Income


class IUpdateIncomeRepo(ABC):
    @abstractmethod
    def update(self, income_id: int, income: Income) -> Income: ...
