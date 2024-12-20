from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from models.BaseModel import BaseModel
from sqlalchemy.orm import relationship


class Income(BaseModel):
    __tablename__ = "incomes"

    # Income Attributes
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)

    # Income Foreign Keys
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    # Income Relationships
    category = relationship("Categories", back_populates="incomes")
    user = relationship("User", back_populates="incomes")
