from sqlalchemy import Column, Integer, String
from models.BaseModel import BaseModel
from sqlalchemy.orm import relationship


class Categories(BaseModel):
    __tablename__ = "categories"

    # Categories Attributes
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(String(100), nullable=False)

    # Categories Relationships
    stocks = relationship(
        "Stock", back_populates="category", cascade="all, delete-orphan"
    )
    incomes = relationship(
        "Income", back_populates="category", cascade="all, delete-orphan"
    )
    expenses = relationship(
        "Expanse", back_populates="category", cascade="all, delete-orphan"
    )
