from abc import ABC, abstractmethod
from models import User


class IDeleteUserRepo(ABC):
    @abstractmethod
    async def delete(self, user: User) -> None: ...
