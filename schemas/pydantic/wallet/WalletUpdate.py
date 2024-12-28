from typing import Optional
from pydantic import BaseModel


class WalletUpdate(BaseModel):
    name: Optional[str] = None
    stocks: Optional[dict] = None
    buys: Optional[dict] = None
    sells: Optional[dict] = None
