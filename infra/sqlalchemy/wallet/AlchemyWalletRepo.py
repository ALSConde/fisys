from infra.sqlalchemy.AlchemyRepo import AlchemyRepo
from models.wallets.Wallet import Wallet
from repos.wallet.IWalletRepo import IWalletRepo
from sqlalchemy.orm import Session
from fastapi import Depends
from configs.Database import get_db


class AlchemyWalletRepo(AlchemyRepo[Wallet], IWalletRepo):
    def __init__(self, session: Session = Depends(get_db)) -> None:
        super().__init__(Wallet, session)
