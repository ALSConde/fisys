from abc import ABC, abstractmethod
from models.wallets.Categories import Categories


class ICreateCategoryRepo(ABC):
    @abstractmethod
    def create(self, category: Categories) -> Categories: ...
