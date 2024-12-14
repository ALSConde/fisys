from abc import ABC, abstractmethod


class IDeleteIncomeRepo(ABC):
    @abstractmethod
    def delete(self, income_id: int) -> None: ...
