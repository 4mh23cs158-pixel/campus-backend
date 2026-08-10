from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db

from schemas.complaint_schemas import (
    ComplaintCreate,
    ComplaintUpdate,
    ComplaintResponse
)

from services.complaint_service import (
    create_new_complaint,
    fetch_all_complaints,
    fetch_single_complaint,
    edit_complaint,
    remove_complaint,
    assign_complaint,
    change_status,
    update_remarks,
    fetch_student_complaints,
    fetch_staff_complaints
)


router = APIRouter(
    prefix="/complaints",
    tags=["Complaints"]
)


# ========================================
# CREATE COMPLAINT
# ========================================

@router.post(
    "/",
    response_model=ComplaintResponse
)
def create_complaint(
    complaint: ComplaintCreate,
    db: Session = Depends(get_db)
):

    # Temporary student ID
    # Later this will come from logged-in user
    student_id = 1

    return create_new_complaint(
        db,
        complaint,
        student_id
    )


# ========================================
# GET STUDENT COMPLAINTS
# ========================================

@router.get(
    "/student/{student_id}",
    response_model=list[ComplaintResponse]
)
def get_student_complaints(
    student_id: int,
    db: Session = Depends(get_db)
):

    return fetch_student_complaints(
        db,
        student_id
    )


# ========================================
# GET STAFF COMPLAINTS
# ========================================

@router.get(
    "/staff/{staff_id}",
    response_model=list[ComplaintResponse]
)
def get_staff_dashboard(
    staff_id: int,
    db: Session = Depends(get_db)
):

    return fetch_staff_complaints(
        db,
        staff_id
    )


# ========================================
# GET ALL COMPLAINTS
# ========================================

@router.get(
    "/",
    response_model=list[ComplaintResponse]
)
def get_all_complaints(
    status: str | None = None,
    category: str | None = None,
    priority: str | None = None,
    department_id: int | None = None,
    search: str | None = None,
    db: Session = Depends(get_db)
):

    return fetch_all_complaints(
        db=db,
        status=status,
        category=category,
        priority=priority,
        department_id=department_id,
        search=search
    )


# ========================================
# GET SINGLE COMPLAINT
# ========================================

@router.get(
    "/{complaint_id}",
    response_model=ComplaintResponse
)
def get_single_complaint(
    complaint_id: int,
    db: Session = Depends(get_db)
):

    return fetch_single_complaint(
        db,
        complaint_id
    )


# ========================================
# UPDATE COMPLAINT
# ========================================

@router.put(
    "/{complaint_id}",
    response_model=ComplaintResponse
)
def update_complaint(
    complaint_id: int,
    complaint: ComplaintUpdate,
    db: Session = Depends(get_db)
):

    return edit_complaint(
        db,
        complaint_id,
        complaint
    )


# ========================================
# DELETE COMPLAINT
# ========================================

@router.delete(
    "/{complaint_id}"
)
def delete_complaint(
    complaint_id: int,
    db: Session = Depends(get_db)
):

    return remove_complaint(
        db,
        complaint_id
    )


# ========================================
# ASSIGN STAFF
# ========================================

@router.put(
    "/{complaint_id}/assign"
)
def assign(
    complaint_id: int,
    staff_id: int,
    db: Session = Depends(get_db)
):

    return assign_complaint(
        db,
        complaint_id,
        staff_id
    )


# ========================================
# UPDATE STATUS
# ========================================

@router.put(
    "/{complaint_id}/status"
)
def status(
    complaint_id: int,
    status: str,
    db: Session = Depends(get_db)
):

    return change_status(
        db,
        complaint_id,
        status
    )


# ========================================
# ADD REMARKS
# ========================================

@router.put(
    "/{complaint_id}/remarks"
)
def remarks(
    complaint_id: int,
    remarks: str,
    db: Session = Depends(get_db)
):

    return update_remarks(
        db,
        complaint_id,
        remarks
    )