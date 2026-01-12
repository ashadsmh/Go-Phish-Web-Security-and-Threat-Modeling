from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.schemas import EventCreate
from app.db.session import get_db
from app.services.event_logger import log_event

router = APIRouter()

@router.post("/", status_code=status.HTTP_202_ACCEPTED)
async def ingest_event(
    event: EventCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Ingests security-relevant events asynchronously.

    The 202 Accepted response is intentional: it communicates that
    telemetry ingestion is decoupled from user-facing behavior,
    which is a common security engineering pattern.
    """
    await log_event(db, event)
    return {"detail": "Event accepted for processing"}
