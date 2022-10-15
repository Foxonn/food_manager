from datetime import datetime
from uuid import UUID
from uuid import uuid4

from pydantic import BaseModel
from pydantic import Field

__all__ = ['DishBaseModel']


def _datetime_now() -> datetime:
    return datetime.now()


class DishBaseModel(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    updated_at: datetime = Field(default_factory=_datetime_now)
    created_at: datetime = Field(default_factory=_datetime_now)
    name: str
