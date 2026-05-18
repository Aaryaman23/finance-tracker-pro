from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from model import Income
from schemas import IncomeCreate

router = APIRouter(
    prefix="/income",
    tags=["Income"]
)


@router.post("/")
def add_income(
    income: IncomeCreate,
    db: Session=Depends(get_db)
):

    item=Income(
        source=income.source,
        amount=income.amount,
        user_id=1
    )

    db.add(item)
    db.commit()

    return {
        "message":"Income Added"
    }