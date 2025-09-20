from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import settings
from .base import Base

_engine = None
SessionLocal = None

def init_db():
    global _engine, SessionLocal
    _engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
    Base.metadata.create_all(bind=_engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
