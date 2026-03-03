from fastapi import APIRouter
from app.core.config import settings

router = APIRouter(prefix="/debug", tags=["debug"])

@router.get("/config")
def config_check():
    return {
        "app_name": settings.app_name,
        "environment": settings.environment,
        "has_db": bool(settings.database_url),
    }