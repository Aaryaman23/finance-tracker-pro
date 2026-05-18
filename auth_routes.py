from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from model import User
from schemas import Register

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
def register(
    user: Register,
    db: Session = Depends(get_db)
):

    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()

    return {
        "message":"Registered"
    }