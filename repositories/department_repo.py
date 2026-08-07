from sqlalchemy.orm import Session

from models import Department


def create_department(db: Session, department):

    db_department = Department(

        department_name=department.department_name,

        department_email=department.department_email,

        department_phone=department.department_phone
    )

    db.add(db_department)

    db.commit()

    db.refresh(db_department)

    return db_department


def get_departments(db: Session):

    return db.query(Department).all()


def get_department_by_id(
    db: Session,
    department_id: int
):

    return db.query(Department).filter(

        Department.id == department_id

    ).first()