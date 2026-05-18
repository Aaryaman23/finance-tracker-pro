from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db
from model import Budget
from schemas import BudgetCreate

from utils.oauth import get_current_user


router = APIRouter(
    prefix="/budget",
    tags=["Budget"]
)


@router.post("/")
def set_budget(
    data: BudgetCreate,
    current_user = Depends(
        get_current_user
    ),
    db: Session = Depends(
        get_db
    )
):

    budget = Budget(
        amount=data.amount,
        month=data.month,
        user_id=current_user.id
    )

    db.add(budget)

    db.commit()

    db.refresh(budget)

    return budget