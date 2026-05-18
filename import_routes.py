from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
import pandas as pd

from dependencies import get_db
from model import Expense
from utils.oauth import get_current_user


router = APIRouter(
    prefix="/import",
    tags=["Import"]
)


@router.post("/csv")
async def import_csv(
    file: UploadFile = File(...),
    current_user = Depends(
        get_current_user
    ),
    db: Session = Depends(
        get_db
    )
):

    df = pd.read_csv(
        file.file
    )

    for _, row in df.iterrows():

        expense = Expense(
            title=row["title"],
            amount=float(
                row["amount"]
            ),
            category=row["category"],
            user_id=current_user.id
        )

        db.add(expense)

    db.commit()

    return {
        "message":
        "Expenses imported successfully"
    }