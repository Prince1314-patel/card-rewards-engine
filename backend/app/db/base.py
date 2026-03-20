"""Database configuration and session setup."""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool
from app.core.config import settings

# Database URL from settings
DATABASE_URL = settings.database_url

# Create engine
engine = create_engine(
    DATABASE_URL,
    echo=settings.database_echo,
    # Use NullPool to avoid connection pooling issues in development
    poolclass=NullPool if settings.environment == "test" else None,
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base class for models
Base = declarative_base()


def get_db():
    """Dependency for getting database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
