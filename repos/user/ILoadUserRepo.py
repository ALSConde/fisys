from abc import ABC, abstractmethod
from models import User


class ILoadUserRepo(ABC):
    @abstractmethod
    def load(self, user: str) -> User | None:
        ...
