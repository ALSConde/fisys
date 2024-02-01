from typing import Generic
from .AbstractAlchemyRepo import AbstractAlchemyRepo, M


class AbstractLoadByAlchemyRepo(Generic[M], AbstractAlchemyRepo[M]):
    async def load_by(self, **kwargs) -> M.__class__ | None:
        ret = self.session.query(M.__class__).filter_by(**kwargs).first()
        print(f"{M.__class__.__name__} not found")
        print(f"kwargs: {kwargs}")
        print(f"ret: {ret}")
        return ret
