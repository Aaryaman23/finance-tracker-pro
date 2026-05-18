from pydantic import BaseModel


class Register(BaseModel):
    username: str
    email: str
    password: str


class Login(BaseModel):
    email: str
    password: str


class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str


class IncomeCreate(BaseModel):
    source: str
    amount: float

