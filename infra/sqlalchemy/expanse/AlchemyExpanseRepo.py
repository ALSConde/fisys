from infra.sqlalchemy.AlchemyRepo import AlchemyRepo
from models.wallets.Expense import Expense
from repos.expanse.IExpanseRepo import IExpanseRepo
from sqlalchemy.orm import Session
from fastapi import Depends
from configs.Database import get_db

class AlchemyExpanseRepo(AlchemyRepo[Expense], IExpanseRepo):
    def __init__(self, session: Session = Depends(get_db)) -> None:
        super().__init__(Expense, session)
