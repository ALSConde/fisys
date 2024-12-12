from typing import Generic
from fastapi import Depends
from configs.Database import get_db
from infra.sqlalchemy.AbstractAlchemyRepo import M
from infra.sqlalchemy.AbstractLoadAlchemyRepo import AbstractLoadAlchemyRepo
from infra.sqlalchemy.AbstractCreateAlchemyRepo import AbstractCreateAlchemyRepo
from infra.sqlalchemy.AbstractUpdateAlchemyRepo import AbstractUpdateAlchemyRepo
from infra.sqlalchemy.AbstractDeleteAlchemyRepo import AbstractDeleteAlchemyRepo
from sqlalchemy.orm import Session


class AlchemyRepo(
    Generic[M],
    AbstractCreateAlchemyRepo[M],
    AbstractLoadAlchemyRepo[M],
    AbstractUpdateAlchemyRepo[M],
    AbstractDeleteAlchemyRepo[M],
):
    def __init__(self, model: M,session: Session = Depends(get_db)) -> None:
        super().__init__(model,session)
