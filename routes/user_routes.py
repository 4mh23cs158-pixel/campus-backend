from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from schemas.user_schemas import UserBase, UserUpdate, Userlogin
# pyrefly: ignore [missing-impor
from repositories.user_repo import (
    create_user,
    get_user,
    get_user_by_email,
    login_user,
    get_all_users,
    update_user
)

router = APIRouter()


@router.post("/signup")
def signup_user(user: UserBase, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/users/{user_id}")
def get_single_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)


@router.post("/login")
def login(
    user: Userlogin,
    db: Session = Depends(get_db)
):
    existing_user = get_user_by_email(
        db,
        user.email
    )

    if existing_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if existing_user.password != user.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "message": "Login successful",
        "user": {
            "id": existing_user.id,
            "name": existing_user.name,
            "email": existing_user.email,
            "phone_number": existing_user.phone_number,
            "role": existing_user.role
        }
    }

@router.get("/logout")
def logout():
    return {
        "message": "Logout successful"
    }
@router.get("/users")
def get_all(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.put("/users/{user_id}")
def update(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    return update_user(
        db,
        user_id,
        user
    )