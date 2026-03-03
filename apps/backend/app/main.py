import logging

from app.api.router import api_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.db.session import engine
from fastapi import FastAPI
from sqlalchemy import text
from app.api.routes import debug

setup_logging()

app = FastAPI(title=settings.app_name, version="0.1.0")
app.include_router(debug.router)

app.include_router(api_router)

logger = logging.getLogger(__name__)


@app.on_event("startup")
def startup_event():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        logger.info("Database connection successful")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
