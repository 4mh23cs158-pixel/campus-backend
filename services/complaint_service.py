from sqlalchemy.orm import Session

from repositories.complaint_repo import (
    create_complaint,
    get_all_complaints,
    get_complaint_by_id,
    update_complaint,
    delete_complaint,
    get_student_complaints,
    get_staff_complaints
)

from schemas.complaint_schemas import (
    ComplaintCreate,
    ComplaintUpdate
)
from repositories.complaint_repo import (
    assign_staff,
    update_status,
    add_remarks
)


# ----------------------------------------
# Create Complaint
# ----------------------------------------
def create_new_complaint(
    db: Session,
    complaint: ComplaintCreate,
    student_id: int
):
    """
    Business Logic:
    - Validate complaint
    - Set default values
    - Later add AI prediction
    """

    return create_complaint(
        db,
        complaint,
        student_id
    )


# ----------------------------------------
# View All Complaints
# ----------------------------------------
def fetch_all_complaints(db: Session):

    return get_all_complaints(db)


# ----------------------------------------
# View Single Complaint
# ----------------------------------------
def fetch_single_complaint(
    db: Session,
    complaint_id: int
):

    return get_complaint_by_id(
        db,
        complaint_id
    )


# ----------------------------------------
# Update Complaint
# ----------------------------------------
def edit_complaint(
    db: Session,
    complaint_id: int,
    complaint: ComplaintUpdate
):

    return update_complaint(
        db,
        complaint_id,
        complaint
    )


# ----------------------------------------
# Delete Complaint
# ----------------------------------------
def remove_complaint(
    db: Session,
    complaint_id: int
):

    return delete_complaint(
        db,
        complaint_id
    )

def assign_complaint(
    db: Session,
    complaint_id: int,
    staff_id: int
):

    return assign_staff(
        db,
        complaint_id,
        staff_id
    )
def change_status(
    db: Session,
    complaint_id: int,
    status: str
):

    return update_status(
        db,
        complaint_id,
        status
    )
def update_remarks(
    db: Session,
    complaint_id: int,
    remarks: str
):

    return add_remarks(
        db,
        complaint_id,
        remarks
    )
def fetch_student_complaints(
    db: Session,
    student_id: int
):

    return get_student_complaints(
        db,
        student_id
    )
def fetch_staff_complaints(
    db: Session,
    staff_id: int
):

    return get_staff_complaints(
        db,
        staff_id
    )