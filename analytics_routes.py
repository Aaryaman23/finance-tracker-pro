from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from dependencies import get_db
from model import Expense
from utils.oauth import get_current_user


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/category")
def category_analysis(
    current_user = Depends(
        get_current_user
    ),
    db: Session = Depends(
        get_db
    )
):

    result = db.query(
        Expense.category,
        func.sum(
            Expense.amount
        )
    ).filter(
        Expense.user_id == current_user.id
    ).group_by(
        Expense.category
    ).all()

    data = []

    for category, total in result:

        data.append(
            {
                "category": category,
                "total": total
            }
        )

    return data