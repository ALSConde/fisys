from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from models.BaseModel import BaseModel
from sqlalchemy.orm import relationship


class Expense(BaseModel):
    __tablename__ = "expenses"

    # Expanse Attributes
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)

    # Expanse Foreign Keys
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Expanse Relationships
    user = relationship("User", back_populates="expenses")
    category = relationship("Categories", back_populates="expenses")
