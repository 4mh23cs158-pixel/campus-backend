from sqlalchemy.orm import Session

from repositories.department_repo import (
    create_department,
    get_departments,
    get_department_by_id
)


def create_new_department(
    db: Session,
    department
):

    return create_department(
        db,
        department
    )


def fetch_departments(
    db: Session
):

    return get_departments(db)


def fetch_department(
    db: Session,
    department_id: int
):

    return get_department_by_id(
        db,
        department_id
    )