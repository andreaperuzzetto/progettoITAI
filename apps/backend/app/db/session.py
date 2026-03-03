from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from sqlalchemy.orm import Session

engine = create_engine(
    settings.database_url,
    echo=False,          # True solo in debug
    future=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()