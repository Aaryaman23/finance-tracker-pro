from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import pandas as pd

from dependencies import get_db
from model import Expense
from utils.oauth import get_current_user


router = APIRouter(
    prefix="/export",
    tags=["Export"]
)


@router.get("/expenses")
def export_expenses(
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

    data = []

    for item in expenses:

        data.append({
            "title": item.title,
            "amount": item.amount,
            "category": item.category
        })

    df = pd.DataFrame(data)

    filename = "expenses.csv"

    df.to_csv(
        filename,
        index=False
    )

    return FileResponse(
        filename,
        media_type="text/csv",
        filename=filename
    )

@router.post("/")
def add_expense(
    expense: ExpenseCreate,
    current_user = Depends(
        get_current_user
    ),
    db: Session = Depends(
        get_db
    )
):

    return create_expense(
        expense,
        current_user,
        db
    )