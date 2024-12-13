from sqlalchemy import Column, ForeignKey, Integer
from models.BaseModel import BaseModel
from sqlalchemy.orm import relationship


class StockBuyHistory(BaseModel):
    __tablename__ = "stock_buy_histories"

    # StockBuyHistory Attributes
    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey("wallets.id"), nullable=False)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    tax = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)

    # StockBuyHistory Relationships
    stock = relationship("Stock", back_populates="buy_history")
    wallet = relationship("Wallet", back_populates="stock_buy_history")
