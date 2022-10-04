from datetime import datetime
from uuid import UUID

from .FoodProductModel import FoodProductModel

__all__ = ['FoodProductDbModel']


class FoodProductDbModel(FoodProductModel):
    id: UUID
    update_at: datetime
    create_at: datetime
