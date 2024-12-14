from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from models.BaseModel import BaseModel
from sqlalchemy.orm import relationship


class Income(BaseModel):
    __tablename__ = "incomes"

    # Income Attributes
    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey("wallets.id"), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    # Income Relationships
    wallet = relationship("Wallet", back_populates="incomes")
    category = relationship("Categories", back_populates="incomes")
