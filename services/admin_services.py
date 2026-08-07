from sqlalchemy.orm import Session

from repositories.admin_repo import get_dashboard_stats


def fetch_dashboard_stats(db: Session):

    return get_dashboard_stats(db)