from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db
from schemas.user_schemas import UserBase, UserUpdate
# pyrefly: ignore [missing-impor
from repositories.user_repo import (
    create_user,
    get_user,
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
def login(user: UserBase, db: Session = Depends(get_db)):
    return login_user(db, user)

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