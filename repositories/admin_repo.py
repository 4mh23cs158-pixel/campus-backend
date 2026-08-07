from sqlalchemy.orm import Session
from sqlalchemy import func

from models import User, Complaint, Department


def get_dashboard_stats(db: Session):

    total_users = db.query(User).count()

    total_complaints = db.query(Complaint).count()

    pending = db.query(Complaint).filter(
        Complaint.status == "Pending"
    ).count()

    assigned = db.query(Complaint).filter(
        Complaint.status == "Assigned"
    ).count()

    resolved = db.query(Complaint).filter(
        Complaint.status == "Resolved"
    ).count()

    departments = db.query(Department).count()

    complaint_categories = (
        db.query(
            Complaint.category,
            func.count(Complaint.id)
        )
        .group_by(Complaint.category)
        .all()
    )

    return {

        "total_users": total_users,

        "total_complaints": total_complaints,

        "pending": pending,

        "assigned": assigned,

        "resolved": resolved,

        "departments": departments,

        "complaint_categories": complaint_categories
    }