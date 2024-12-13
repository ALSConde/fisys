from sqlalchemy import Column, ForeignKey, Integer, String
from models.BaseModel import BaseModel
from sqlalchemy.orm import relationship

from models.wallets.stocks.Stock import Stock


class Wallet(BaseModel):
    __tablename__ = "wallets"

    # Wallet Attributes
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Wallet Relationships
    stocks = relationship(
        "Stock", back_populates="wallet", cascade="all, delete-orphan"
    )
    stock_buy_history = relationship("StockBuyHistory", back_populates="wallet")
    stock_sell_history = relationship("StockSellHistory", back_populates="wallet")
