from typing import Sequence
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

    async def load_by(self, **kwargs) -> User:
        return await super().load_by(**kwargs)

    async def load_all(self, **kwargs) -> list[User] | None:
        return await super().load_all(**kwargs)

    async def update(self, user_id: int, user: User) -> User:
        return await super().update(user_id, user)
