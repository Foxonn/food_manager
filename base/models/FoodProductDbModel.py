from datetime import datetime

from pydantic.types import UUID

from .FoodProductModel import FoodProductModel

__all__ = ['FoodProductDbModel']


class FoodProductDbModel(FoodProductModel):
    id: UUID
    update_at: datetime
    create_at: datetime
