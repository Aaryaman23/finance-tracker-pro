from fastapi import APIRouter
from schemas import ExpenseCreate

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