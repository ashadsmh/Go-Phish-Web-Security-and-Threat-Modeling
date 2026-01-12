from pydantic import BaseModel, Field
from typing import Optional, Dict

class EventCreate(BaseModel):
    """
    Schema for incoming telemetry events.

    Notice how we never accept raw credentials — only metadata
    that describes behavior without exposing sensitive content.
    """
    campaign_id: int = Field(..., gt=0)
    event_type: str = Field(..., min_length=3, max_length=50)
    metadata: Optional[Dict] = Field(default_factory=dict)
