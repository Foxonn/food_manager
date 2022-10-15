from datetime import datetime
from uuid import UUID
from uuid import uuid4

from pydantic import Field

from .FoodProductModel import FoodProductModel

__all__ = ['FoodProductDbModel']


def _datetime_now() -> datetime:
    return datetime.now()


class FoodProductDbModel(FoodProductModel):
    id: UUID = Field(default_factory=uuid4)
    updated_at: datetime = Field(default_factory=_datetime_now)
    created_at: datetime = Field(default_factory=_datetime_now)

    class Config:
        allow_mutation = False
