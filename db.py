from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
import settings

# Base class for models
Base = declarative_base()

# These will be initialized during app startup
engine = None
AsyncSessionLocal = None


def init_db():
    """Initialize the async SQLAlchemy engine and session maker."""
    global engine, AsyncSessionLocal

    if engine is None or AsyncSessionLocal is None:
        engine = create_async_engine(
            settings.DATABASE_URL,
            echo=settings.DEBUG_MODE,
            future=True,
        )
        AsyncSessionLocal = async_sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )


# Dependency for FastAPI routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
