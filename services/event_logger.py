from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Event

async def log_event(db: AsyncSession, event_data):
    """
    Centralized telemetry ingestion function.

    This abstraction allows:
    - Future log forwarding (SIEM, message queues)
    - Rate limiting
    - Anomaly detection hooks
    - Audit integrity controls

    Keeping telemetry logic isolated mirrors how security teams
    design observability pipelines.
    """
    event = Event(
        campaign_id=event_data.campaign_id,
        event_type=event_data.event_type,
        metadata=event_data.metadata
    )

    db.add(event)
    await db.commit()
