from typing import Generic
from .AbstractAlchemyRepo import AbstractAlchemyRepo, M

class AbstractCreateAlchemyRepo(Generic[M], AbstractAlchemyRepo[M]):
    
    async def create(self, model: M) -> M:
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model