from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from dependencies import get_db
from model import Expense
from utils.oauth import get_current_user


router = APIRouter(
    prefix="/analytics",
    tags=["Monthly Analytics"]
)


@router.get("/monthly")
def monthly_expenses(
    current_user = Depends(
        get_current_user
    ),
    db: Session = Depends(
        get_db
    )
):

    data = db.query(
        func.strftime(
            "%Y-%m",
            Expense.created_at
        ),

        func.sum(
            Expense.amount
        )
    ).filter(
        Expense.user_id == current_user.id
    ).group_by(
        func.strftime(
            "%Y-%m",
            Expense.created_at
        )
    ).all()

    result = []

    for month, total in data:

        result.append(
            {
                "month": month,
                "total": total
            }
        )

    return result