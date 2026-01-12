from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Campaign(Base):
    """
    Represents a simulated phishing campaign.

    Campaigns act as containment boundaries: events are always attributed
    to a specific campaign to avoid cross-contamination of telemetry.
    """
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Event(Base):
    """
    Immutable security telemetry record.

    Events are append-only and intentionally generic. This mirrors real-world
    security logging systems where raw input is never stored.
    """
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    event_type = Column(String, nullable=False)
    metadata = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
