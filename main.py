from fastapi import FastAPI
from app.api import campaigns, events, analytics
from app.core.config import settings

app = FastAPI(
    title="Go Phish",
    description="""
    Go Phish is an educational phishing simulation platform focused on
    security telemetry, social engineering awareness, and backend systems design.

    This application intentionally prioritizes clarity, ethics, and defensive
    security thinking over feature completeness.
    """,
    version="0.1.0"
)

# Routers are registered explicitly to preserve clear API boundaries.
# This mirrors real-world security services where responsibility isolation
# is critical for auditing and access control.
app.include_router(campaigns.router, prefix="/api/campaigns", tags=["Campaigns"])
app.include_router(events.router, prefix="/api/events", tags=["Telemetry"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])
