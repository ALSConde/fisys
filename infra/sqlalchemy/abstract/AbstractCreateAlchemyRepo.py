from .AbstractAlchemyRepo import AbstractAlchemyRepo, M


class AbstractCreateAlchemyRepo(AbstractAlchemyRepo[M]):
    async def create(self, model: M) -> M:
        self.session.add(model)
        self.session.commit()
        self.session.flush()
        return model
