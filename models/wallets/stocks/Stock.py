from sqlalchemy import Column, Float, ForeignKey, Integer, String
from models.BaseModel import BaseModel
from sqlalchemy.orm import relationship


class Stock(BaseModel):
    __tablename__ = "stocks"

    # Stock Attributes
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    ticker = Column(String(10), nullable=False, unique=True)
    quantity = Column(Integer, nullable=False)
    mean_price = Column(Float, nullable=False)
    wallet_id = Column(Integer, ForeignKey("wallets.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    # Stock Relationships
    wallet = relationship("Wallet", back_populates="stocks")
    buy_history = relationship(
        "StockBuyHistory", back_populates="stock", cascade="all, delete-orphan"
    )
    stock_sell_history = relationship(
        "StockSellHistory", back_populates="stock", cascade="all, delete-orphan"
    )
    category = relationship("Categories", back_populates="stocks")
