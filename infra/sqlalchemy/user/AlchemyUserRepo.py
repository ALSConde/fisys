from typing import Optional, Sequence
from fastapi import Depends
from configs.Database import get_db
from infra.sqlalchemy.AlchemyRepo import AlchemyRepo
from models import User
from repos.user import IUserRepo
from sqlalchemy.orm import Session


class AlchemyUserRepo(AlchemyRepo[User], IUserRepo):
    def __init__(self, session: Session = Depends(get_db)) -> None:
        super().__init__(User, session)

    async def create(self, user: User) -> User:
        return await super().create(user)

    async def load_by(self, **kwargs) -> Optional[list[User]]:
        return await super().load_by(**kwargs)

    async def load_all(self) -> Sequence[User]:
        return await super().load_all()

    async def load_all_actives(self) -> Sequence[User]:
        return await super().load_all_actives()

    async def load_actives_by(self, **kwargs) -> Optional[User]:
        return await super().load_actives_by(**kwargs)

    async def load_first(self, **kwargs) -> list[User] | None:
        return await super().load_first(**kwargs)

    async def load_active_first(self, **kwargs) -> User | None:
        return await super().load_active_first(**kwargs)

    async def load_all_inactives(self) -> list[User]:
        return await super().load_all_inactives()

    async def update(self, user_id: int, user: User) -> User:
        return await super().update(user_id, user)
