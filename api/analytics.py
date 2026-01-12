from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.db.session import get_db
from app.db.models import Event

router = APIRouter()

@router.get("/campaigns/{campaign_id}")
async def campaign_metrics(
    campaign_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Aggregates security telemetry into meaningful metrics.

    This endpoint demonstrates how raw security signals
    are transformed into actionable insight.
    """
    query = (
        select(Event.event_type, func.count())
        .where(Event.campaign_id == campaign_id)
        .group_by(Event.event_type)
    )

    result = await db.execute(query)
    metrics = {row[0]: row[1] for row in result}

    return {
        "campaign_id": campaign_id,
        "metrics": metrics
    }
