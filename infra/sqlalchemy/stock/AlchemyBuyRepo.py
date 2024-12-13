from infra.sqlalchemy.AlchemyRepo import AlchemyRepo
from models.wallets.stocks.StockBuyHistory import StockBuyHistory
from repos.stocks.buy.IBuyRepo import IBuyRepo
from sqlalchemy.orm import Session
from fastapi import Depends
from configs.Database import get_db


class AlchemyBuyRepo(AlchemyRepo[StockBuyHistory], IBuyRepo):
    def __init__(self, session: Session = Depends(get_db)) -> None:
        super().__init__(StockBuyHistory, session)
