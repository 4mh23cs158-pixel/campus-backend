from sqlalchemy.orm import Session
from fastapi import HTTPException

from models import Complaint
from schemas.complaint_schemas import (
    ComplaintCreate,
    ComplaintUpdate
)


# ---------------------------------
# Create Complaint
# ---------------------------------
def create_complaint(
    db: Session,
    complaint: ComplaintCreate,
    student_id: int,
    predicted_category: str
):

    new_complaint = Complaint(
        title=complaint.title,
        description=complaint.description,
        category=predicted_category,
        location=complaint.location,
        priority="Low",
        status="Pending",
        student_id=student_id
    )

    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)

    return new_complaint


# ---------------------------------
# Get All Complaints
# ---------------------------------
def get_all_complaints(
    db: Session,
    status: str | None = None,
    category: str | None = None,
    priority: str | None = None,
    department_id: int | None = None,
    search: str | None = None
):

    query = db.query(Complaint)

    # -----------------------------
    # Status Filter
    # -----------------------------

    if status:
        query = query.filter(
            Complaint.status == status
        )

    # -----------------------------
    # Category Filter
    # -----------------------------

    if category:
        query = query.filter(
            Complaint.category == category
        )

    # -----------------------------
    # Priority Filter
    # -----------------------------

    if priority:
        query = query.filter(
            Complaint.priority == priority
        )

    # -----------------------------
    # Department Filter
    # -----------------------------

    if department_id:
        query = query.filter(
            Complaint.department_id == department_id
        )

    # -----------------------------
    # Search
    # -----------------------------

    if search:

        search_text = f"%{search}%"

        query = query.filter(
            Complaint.title.ilike(search_text)
            |
            Complaint.description.ilike(search_text)
        )

    # -----------------------------
    # Latest Complaints First
    # -----------------------------

    query = query.order_by(
        Complaint.created_at.desc()
    )

    return query.all()


# ---------------------------------
# Get Complaint By ID
# ---------------------------------
def get_complaint_by_id(db: Session, complaint_id: int):

    complaint = (
        db.query(Complaint)
        .filter(Complaint.id == complaint_id)
        .first()
    )

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return complaint


# ---------------------------------
# Update Complaint
# ---------------------------------
def update_complaint(
    db: Session,
    complaint_id: int,
    complaint_data: ComplaintUpdate
):

    complaint = (
        db.query(Complaint)
        .filter(Complaint.id == complaint_id)
        .first()
    )

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    update_data = complaint_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(complaint, key, value)

    db.commit()
    db.refresh(complaint)

    return complaint


# ---------------------------------
# Delete Complaint
# ---------------------------------
def delete_complaint(db: Session, complaint_id: int):

    complaint = (
        db.query(Complaint)
        .filter(Complaint.id == complaint_id)
        .first()
    )

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    db.delete(complaint)
    db.commit()

    return {
        "message": "Complaint deleted successfully"
    }

def assign_staff(
    db: Session,
    complaint_id: int,
    staff_id: int
):

    complaint = db.query(Complaint).filter(
        Complaint.id == complaint_id
    ).first()

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    complaint.assigned_to = staff_id

    complaint.status = "Assigned"

    db.commit()

    db.refresh(complaint)

    return complaint

def update_status(
    db: Session,
    complaint_id: int,
    status: str
):

    complaint = db.query(Complaint).filter(
        Complaint.id == complaint_id
    ).first()

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    complaint.status = status

    db.commit()

    db.refresh(complaint)

    return complaint

def add_remarks(
    db: Session,
    complaint_id: int,
    remarks: str
):

    complaint = db.query(Complaint).filter(
        Complaint.id == complaint_id
    ).first()

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    complaint.remarks = remarks

    db.commit()

    db.refresh(complaint)

    return complaint

def get_student_complaints(db: Session, student_id: int):

    complaints = (
        db.query(Complaint)
        .filter(Complaint.student_id == student_id)
        .all()
    )

    return complaints
def get_staff_complaints(
    db: Session,
    staff_id: int
):

    complaints = (
        db.query(Complaint)
        .filter(
            Complaint.assigned_to == staff_id
        )
        .all()
    )

    return complaints