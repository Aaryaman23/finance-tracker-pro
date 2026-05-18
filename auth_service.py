from model import User

from utils.security import (
    hash_password,
    verify_password,
    create_access_token
)


def create_user(user, db):

    existing = db.query(
        User
    ).filter(
        User.email == user.email
    ).first()

    if existing:

        return {
            "message": "User already exists"
        }

    hashed = hash_password(
        user.password
    )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message":"registered"
    }


def login_user(
    login_data,
    db
):

    user = db.query(
        User
    ).filter(
        User.email == login_data.email
    ).first()

    if not user:
        return None

    valid = verify_password(
        login_data.password,
        user.password
    )

    if not valid:
        return None

    token = create_access_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": token,
        "token_type":"bearer"
    }