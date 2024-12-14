from repos.income.IIncomeRepo import IIncomeRepo
from ..AlchemyRepo import AlchemyRepo
from models.wallets.Income import Income
from sqlalchemy.orm import Session
from fastapi import Depends
from configs.Database import get_db


class IncomeAlchemyRepo(AlchemyRepo[Income], IIncomeRepo):
    def __init__(self, session: Session = Depends(get_db)) -> None:
        super().__init__(Income, session)
