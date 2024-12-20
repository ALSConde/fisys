from pydantic import BaseModel, ConfigDict


class WalletPost(BaseModel):
    name: str
