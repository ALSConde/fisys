from pydantic import ConfigDict
from schemas.pydantic.wallet.WalletPost import WalletPost


class Wallet(WalletPost):
    id: int
    # stocks: dict
    # buys: dict
    # sells: dict

    model_config = ConfigDict(from_attributes=True)
