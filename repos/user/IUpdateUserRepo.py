from abc import ABC, abstractmethod

from models import User


class IUpdateUserRepo(ABC):
    @abstractmethod
    def update(self, user_id: int, user: User) -> User:
        ...