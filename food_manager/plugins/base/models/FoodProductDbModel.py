from datetime import datetime
from uuid import uuid4

from pydantic import Field
from pydantic import UUID4

from .FoodProductModel import FoodProductModel

__all__ = ['FoodProductDbModel']


class FoodProductDbModel(FoodProductModel):
    id: UUID4 = Field(default_factory=uuid4)
    updated_at: datetime
    created_at: datetime
