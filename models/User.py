from .BaseModel import BaseModel
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class User(BaseModel):
    __tablename__ = "users"

    # User Attributes
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    active = Column(Boolean, default=True, nullable=False)
    password = Column(String(255), nullable=False)

    # User Relationships
    expenses = relationship("Expense", back_populates="user")
    incomes = relationship("Income", back_populates="user")
    wallets = relationship("Wallet", back_populates="user")

    # User Methods
    def normalize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }

    def check_password(self, password: str) -> bool:
        return bool(self.password == password)
