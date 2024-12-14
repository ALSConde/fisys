from abc import ABC, abstractmethod


class IDeleteExpanseRepo(ABC):
    @abstractmethod
    def delete(self, expanse_id: int) -> None: ...
