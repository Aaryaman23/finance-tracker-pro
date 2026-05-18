from model import Expense
from database import SessionLocal
from fastapi import APIRouter
from schemas import ExpenseCreate


def create_expense(expense):
    db=SessionLocal()

    item=Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        user_id=1
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


def get_expenses():

    db=SessionLocal()

    return db.query(
        Expense
    ).all()


def delete_expense(expense_id):

    db=SessionLocal()

    item=db.query(
        Expense
    ).filter(
        Expense.id==expense_id
    ).first()

    if item:
        db.delete(item)
        db.commit()

    return {
        "message":"deleted"
    }


def update_expense(id,data):

    db=SessionLocal()

    item=db.query(
        Expense
    ).filter(
        Expense.id==id
    ).first()

    item.title=data.title
    item.amount=data.amount
    item.category=data.category

    db.commit()

    return item

from services.expense_service import (
create_expense,
get_expenses,
delete_expense,
update_expense
)

router=APIRouter(
prefix="/expenses",
tags=["Expenses"]
)

@router.get("")
def read():
    return get_expenses()

@router.post("")
def add(expense:ExpenseCreate):
    return create_expense(expense)

@router.delete("/{id}")
def remove(id:int):
    return delete_expense(id)

@router.put("/{id}")
def edit(
id:int,
expense:ExpenseCreate
):
    return update_expense(
        id,
        expense
    )
