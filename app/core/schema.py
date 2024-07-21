from datetime import datetime, timezone

from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        json_encoders = {datetime: lambda v: v.replace(tzinfo=timezone.utc).isoformat()}
        from_attributes = True
