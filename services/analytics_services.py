from sqlalchemy.orm import Session

from repositories.analytics_repo import (
    get_dashboard_statistics,
    complaint_status_statistics,
    complaint_category_statistics,
    department_statistics,
    priority_statistics,
    monthly_complaint_statistics
)


# ----------------------------------------
# Dashboard Statistics
# ----------------------------------------

def fetch_dashboard_statistics(db: Session):

    return get_dashboard_statistics(db)


# ----------------------------------------
# Complaint Status Statistics
# ----------------------------------------

def fetch_complaint_status_statistics(db: Session):

    return complaint_status_statistics(db)


# ----------------------------------------
# Complaint Category Statistics
# ----------------------------------------

def fetch_complaint_category_statistics(db: Session):

    return complaint_category_statistics(db)


# ----------------------------------------
# Department Statistics
# ----------------------------------------

def fetch_department_statistics(db: Session):

    return department_statistics(db)


# ----------------------------------------
# Priority Statistics
# ----------------------------------------

def fetch_priority_statistics(db: Session):

    return priority_statistics(db)

def fetch_monthly_complaint_statistics(
    db: Session
):

    return monthly_complaint_statistics(db)