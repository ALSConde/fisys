from abc import ABC, abstractmethod


class IDeleteCateogryRepo(ABC):
    @abstractmethod
    def delete(self, category_id: int) -> None: ...