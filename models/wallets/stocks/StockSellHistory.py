from sqlalchemy import Column, Float, ForeignKey, Integer
from models.BaseModel import BaseModel
from sqlalchemy.orm import relationship


class StockSellHistory(BaseModel):
    __tablename__ = "stock_sell_history"

    # StockSellHistory Attributes
    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey("wallets.id"), nullable=False)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)
    total = Column(Float, nullable=False)

    # StockSellHistory Relationships
    wallet = relationship("Wallet", back_populates="stock_sell_history")
    stock = relationship("Stock", back_populates="stock_sell_history")
