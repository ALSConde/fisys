from abc import ABC, abstractmethod
from models.wallets.Income import Income


class ICreateIncomeRepo(ABC):
    @abstractmethod
    def create(self, income: Income) -> Income: ...
