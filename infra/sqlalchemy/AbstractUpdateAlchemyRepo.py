from typing import Generic
from infra.sqlalchemy.AbstractAlchemyRepo import AbstractAlchemyRepo, M


class AbstractUpdateAlchemyRepo(Generic[M], AbstractAlchemyRepo[M]):
    async def update(self, model: M) -> M:
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model