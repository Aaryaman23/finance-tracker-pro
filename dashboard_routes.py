from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db
from model import Expense, Income

from utils.oauth import get_current_user
from model import Budget

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard(
    current_user = Depends(
        get_current_user
    ),
    db: Session = Depends(
        get_db
    )
):

    expenses = db.query(
        Expense
    ).filter(
        Expense.user_id == current_user.id
    ).all()

    income = db.query(
        Income
    ).filter(
        Income.user_id == current_user.id
    ).all()


    total_expense = sum(
        x.amount
        for x in expenses
    )

    total_income = sum(
        x.amount
        for x in income
    )

    balance = (
        total_income
        - total_expense
    )


    budget = db.query(
        Budget
    ).filter(
        Budget.user_id == current_user.id
    ).first()

    warning = None

    if budget:
        if total_expense > budget.amount:
            warning = "Budget exceeded"

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "expense_count": len(expenses),
        "income_count": len(income),
        "budget": budget.amount if budget else None,
        "warning": warning
    }