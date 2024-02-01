from abc import ABC, abstractmethod

from models import User


class ICreateUserRepo(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        ...
