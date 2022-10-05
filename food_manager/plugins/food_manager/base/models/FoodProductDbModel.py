from datetime import datetime
from uuid import UUID

from .FoodProductModel import FoodProductModel

__all__ = ['FoodProductDbModel']


class FoodProductDbModel(FoodProductModel):
    id: UUID
    updated_at: datetime
    created_at: datetime
