from jose import jwt
from jose import JWTError

from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from dependencies import get_db
from model import User

from utils.security import (
    SECRET_KEY,
    ALGORITHM
)


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get(
            "sub"
        )

        if email is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        user = db.query(
            User
        ).filter(
            User.email == email
        ).first()

        return user

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token invalid"
        )