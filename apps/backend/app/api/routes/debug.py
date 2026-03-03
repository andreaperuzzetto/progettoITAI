from fastapi import APIRouter
from app.core.config import settings
from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import Depends

from app.db.session import get_db

router = APIRouter(prefix="/debug", tags=["debug"])

@router.get("/config")
def config_check():
    return {
        "app_name": settings.app_name,
        "environment": settings.environment,
        "has_db": bool(settings.database_url),
        "has_openai": bool(settings.openai_api_key),
        "has_pinecone": bool(settings.pinecone_api_key),
    }

@router.get("/db-check")
def db_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "db connected"}