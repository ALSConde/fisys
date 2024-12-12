from typing import Generic, Type
from .AbstractAlchemyRepo import AbstractAlchemyRepo, M


class AbstractLoadAlchemyRepo(AbstractAlchemyRepo[M]):

    async def load_actives_by(self, **kwargs) -> list[M] | M | None:
        query = self.session.query(self.model)
        for field, value in kwargs.items():
            query = query.filter(
                getattr(self.model, field).like(f"%{value}%")
            ).filter_by(active=True)
        return query.all()

    async def load_active_first(self, **kwargs) -> M | None:
        query = self.session.query(self.model)
        for field, value in kwargs.items():
            query = query.filter(
                getattr(self.model, field).like(f"%{value}%")
            ).filter_by(active=True)
        return query.first()

    async def load_all(self) -> list[M]:
        return self.session.query(self.model).all()

    async def load_all_actives(self) -> list[M]:
        return self.session.query(self.model).filter_by(active=True).all()

    async def load_all_inactives(self) -> list[M]:
        return self.session.query(self.model).filter_by(active=False).all()
    
    async def load_by(self, **kwargs) -> list[M] | M | None:
        query = self.session.query(self.model)
        for field, value in kwargs.items():
            query = query.filter(getattr(self.model, field).like(f"%{value}%"))
        return query.all()
    
    async def load_first(self, **kwargs) -> M | None:
        query = self.session.query(self.model)
        for field, value in kwargs.items():
            query = query.filter(getattr(self.model, field).like(f"%{value}%"))
        return query.first()
