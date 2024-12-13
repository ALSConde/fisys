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

    async def load_first(self, **kwargs) -> list[User] | None:
        return await super().load_first(**kwargs)

    async def load_actives_by(self, **kwargs) -> list[User] | User | None:
        query = self.session.query(self.model)
        for field, value in kwargs.items():
            query = query.filter(
                getattr(self.model, field).like(f"%{value}%")
            ).filter_by(active=True)
        return query.all()

    async def load_active_first(self, **kwargs) -> User | None:
        query = self.session.query(self.model)
        for field, value in kwargs.items():
            query = query.filter(
                getattr(self.model, field).like(f"%{value}%")
            ).filter_by(active=True)
        return query.first()

    async def update(self, user_id: int, user: User) -> User:
        return await super().update(user_id, user)

    async def load_all_actives(self) -> list[User]:
        return self.session.query(self.model).filter_by(active=True).all()

    async def load_all_inactives(self) -> list[User]:
        return self.session.query(self.model).filter_by(active=False).all()

    async def delete(self, id: int) -> None:
        model = self.session.query(self.model).filter_by(id=id, active=True)
        model.update({"active": False})
        self.session.commit()
        self.session.flush()