from typing import Generic
from fastapi import Depends
from configs.Database import get_db
from sqlalchemy.orm import Session
from infra.sqlalchemy.abstract.AbstractAlchemyRepo import M
from infra.sqlalchemy.abstract.AbstractCreateAlchemyRepo import (
    AbstractCreateAlchemyRepo,
)
from infra.sqlalchemy.abstract.AbstractDeleteAlchemyRepo import (
    AbstractDeleteAlchemyRepo,
)
from infra.sqlalchemy.abstract.AbstractLoadAlchemyRepo import AbstractLoadAlchemyRepo
from infra.sqlalchemy.abstract.AbstractUpdateAlchemyRepo import (
    AbstractUpdateAlchemyRepo,
)


class AlchemyRepo(
    Generic[M],
    AbstractCreateAlchemyRepo[M],
    AbstractLoadAlchemyRepo[M],
    AbstractUpdateAlchemyRepo[M],
    AbstractDeleteAlchemyRepo[M],
):
    def __init__(self, model: M, session: Session = Depends(get_db)) -> None:
        super().__init__(model, session)
