from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db

from services.admin_services import fetch_dashboard_stats

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db)
):

    return fetch_dashboard_stats(db)