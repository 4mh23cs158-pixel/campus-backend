from sqlalchemy.orm import Session
from sqlalchemy import func

from models import (
    User,
    Complaint,
    Department
)
def get_dashboard_statistics(db: Session):

    total_users = db.query(User).count()

    total_students = (
        db.query(User)
        .filter(User.role == "Student")
        .count()
    )

    total_staff = (
        db.query(User)
        .filter(User.role == "Staff")
        .count()
    )

    total_admins = (
        db.query(User)
        .filter(User.role == "Admin")
        .count()
    )

    total_departments = db.query(Department).count()

    total_complaints = db.query(Complaint).count()

    return {

        "total_users": total_users,

        "total_students": total_students,

        "total_staff": total_staff,

        "total_admins": total_admins,

        "total_departments": total_departments,

        "total_complaints": total_complaints

    }
def complaint_status_statistics(db: Session):

    pending = (
        db.query(Complaint)
        .filter(Complaint.status == "Pending")
        .count()
    )

    assigned = (
        db.query(Complaint)
        .filter(Complaint.status == "Assigned")
        .count()
    )

    resolved = (
        db.query(Complaint)
        .filter(Complaint.status == "Resolved")
        .count()
    )

    rejected = (
        db.query(Complaint)
        .filter(Complaint.status == "Rejected")
        .count()
    )

    return {

        "pending": pending,

        "assigned": assigned,

        "resolved": resolved,

        "rejected": rejected

    }
def complaint_category_statistics(db: Session):

    categories = (

        db.query(

            Complaint.category,

            func.count(Complaint.id)

        )

        .group_by(Complaint.category)

        .all()

    )

    result = []

    for category, count in categories:

        result.append({

            "category": category,

            "count": count

        })

    return result
def department_statistics(db: Session):

    departments = (

        db.query(

            Complaint.department,

            func.count(Complaint.id)

        )

        .group_by(

            Complaint.department

        )

        .all()

    )

    result = []

    for department, count in departments:

        result.append({

            "department": department,

            "count": count

        })

    return result
def priority_statistics(db: Session):

    priorities = (

        db.query(

            Complaint.priority,

            func.count(Complaint.id)

        )

        .group_by(

            Complaint.priority

        )

        .all()

    )

    result = []

    for priority, count in priorities:

        result.append({

            "priority": priority,

            "count": count

        })

    return result
def monthly_complaint_statistics(db: Session):

    monthly_data = (
        db.query(
            func.extract(
                "month",
                Complaint.created_at
            ).label("month"),
            func.count(Complaint.id).label("count")
        )
        .group_by(
            func.extract(
                "month",
                Complaint.created_at
            )
        )
        .order_by(
            func.extract(
                "month",
                Complaint.created_at
            )
        )
        .all()
    )

    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    result = []

    for month, count in monthly_data:

        result.append({
            "month": month_names[int(month)],
            "count": count
        })

    return result