from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db

from services.analytics_services import (
    fetch_dashboard_statistics,
    fetch_complaint_status_statistics,
    fetch_complaint_category_statistics,
    fetch_department_statistics,
    fetch_priority_statistics,
    fetch_monthly_complaint_statistics
)


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


# ----------------------------------------
# Complete Dashboard Statistics
# ----------------------------------------

@router.get("/dashboard")
def dashboard_statistics(
    db: Session = Depends(get_db)
):

    return fetch_dashboard_statistics(db)


# ----------------------------------------
# Complaint Status Statistics
# ----------------------------------------

@router.get("/status")
def status_statistics(
    db: Session = Depends(get_db)
):

    return fetch_complaint_status_statistics(db)


# ----------------------------------------
# Complaint Category Statistics
# ----------------------------------------

@router.get("/category")
def category_statistics(
    db: Session = Depends(get_db)
):

    return fetch_complaint_category_statistics(db)


# ----------------------------------------
# Department Statistics
# ----------------------------------------

@router.get("/department")
def department_statistics(
    db: Session = Depends(get_db)
):

    return fetch_department_statistics(db)


# ----------------------------------------
# Priority Statistics
# ----------------------------------------

@router.get("/priority")
def priority_statistics(
    db: Session = Depends(get_db)
):

    return fetch_priority_statistics(db)
@router.get("/monthly")
def monthly_statistics(
    db: Session = Depends(get_db)
):

    return fetch_monthly_complaint_statistics(db)