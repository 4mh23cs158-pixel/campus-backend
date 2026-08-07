from sqlalchemy.orm import Session
from models import User

def get_user(db:Session,user_id:int):
    return db.query(User).filter(User.id==user_id).first()

def get_user_by_email(db:Session,email:str):
    return db.query(User).filter(User.email==email).first()

def create_user(db:Session,user):
    db_user=User(
        name=user.name,
        email=user.email,
        password=user.password,
        phone_number=user.phone_number,
        role="Student"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(db:Session,email:str,password:str):
    user=get_user_by_email(db,email)
    if user and user.password==password:
        return user
    return None

def get_all_users(db:Session):
    return db.query(User).all()

from fastapi import HTTPException

from sqlalchemy.orm import Session
from models import User


def update_user(db:Session,user_id:int,user,updated_user):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    update_data = updated_user.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(user, key, value)

    db.commit()

    db.refresh(user)

    return user