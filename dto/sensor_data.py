import re
from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class SensorDataIn(BaseModel):
    device_id: str = Field(...)
    timestamp: datetime = Field(...)
    temperature: float = Field(..., ge=-100.0, le=100.0)
    humidity: int = Field(..., ge=0, le=100)

    @field_validator("timestamp", mode="before")
    def validate_timestamp(cls, value: str) -> str:
        iso8601_pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$"
        if not re.match(iso8601_pattern, value):
            raise ValueError("timestamp must be in full ISO 8601 format (e.g. 2024-05-01T12:00:00Z)")
        return value


class SensorDataOut(BaseModel):
    device_id: str
    timestamp: datetime
    temperature: float
    humidity: int