from datetime import datetime
from uuid import UUID

from .DishModel import DishModel

__all__ = ['DishDbModel']


class DishDbModel(DishModel):
    id: UUID
    updated_at: datetime
    created_at: datetime
