from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Async engine ensures telemetry writes never block request handling
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
    future=True
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    """
    Dependency-injected database session.

    This pattern allows request-scoped DB access and prevents long-lived
    connections, which is important for security isolation and resource control.
    """
    async with AsyncSessionLocal() as session:
        yield session
