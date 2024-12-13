from infra.sqlalchemy.AlchemyRepo import AlchemyRepo
from models.wallets.stocks.StockSellHistory import StockSellHistory
from repos.stocks.sell.ISellRepo import ISellRepo
from sqlalchemy.orm import Session
from fastapi import Depends
from configs.Database import get_db


class AlchemySellRepo(AlchemyRepo[StockSellHistory], ISellRepo):
    def __init__(self, session: Session = Depends(get_db)) -> None:
        super().__init__(StockSellHistory, session)
