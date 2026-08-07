from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db

from schemas.department_schemas import (
    DepartmentCreate,
    DepartmentResponse
)

from services.department_services import (
    create_new_department,
    fetch_departments,
    fetch_department
)

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.post(
    "/",
    response_model=DepartmentResponse
)
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db)
):

    return create_new_department(
        db,
        department
    )


@router.get(
    "/",
    response_model=list[DepartmentResponse]
)
def get_departments(
    db: Session = Depends(get_db)
):

    return fetch_departments(db)


@router.get(
    "/{department_id}",
    response_model=DepartmentResponse
)
def get_department(
    department_id: int,
    db: Session = Depends(get_db)
):

    return fetch_department(
        db,
        department_id
    )