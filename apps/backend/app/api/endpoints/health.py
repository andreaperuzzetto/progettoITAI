from app.core.config import settings
from app.db.session import engine
from fastapi import APIRouter
from sqlalchemy import text

router = APIRouter()


@router.get("/health", tags=["system"])
def health_check():
    db_status = "unknown"

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception:
        db_status = "error"

    return {"status": "ok", "environment": settings.environment, "database": db_status}
