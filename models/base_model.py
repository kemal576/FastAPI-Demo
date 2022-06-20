import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, func
from sqlalchemy.dialects.postgresql import UUID


class BaseModel:
    id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: datetime = Column(DateTime(timezone=True),
                                  server_default=func.now(), nullable=False)
    updated_at: datetime = Column(DateTime(timezone=True),
                                  server_default=func.now(), nullable=False, onupdate=func.now())
