from infra.sqlalchemy.AlchemyRepo import AlchemyRepo
from models.wallets.stocks.Stock import Stock
from repos.stocks.IStockRepo import IStockRepo
from sqlalchemy.orm import Session
from fastapi import Depends
from configs.Database import get_db


class AlchemyStockRepo(AlchemyRepo[Stock], IStockRepo):
    def __init__(self, session: Session = Depends(get_db)) -> None:
        super().__init__(Stock, session)
