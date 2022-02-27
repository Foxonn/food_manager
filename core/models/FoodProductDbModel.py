from datetime import datetime

from pydantic.types import UUID

from core.entities.FoodProduct import FoodProduct

__all__ = [
    "FoodProductDbModel",
]


class FoodProductDbModel(FoodProduct):
    id: UUID
    update_at: datetime
    create_at: datetime
