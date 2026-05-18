from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Float)
    category = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))


class Income(Base):
    __tablename__ = "income"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String)
    amount = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))