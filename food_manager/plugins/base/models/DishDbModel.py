from datetime import datetime
from uuid import UUID

from .DishModel import DishModel

__all__ = ['DishDbModel']


class DishDbModel(DishModel):
    id: UUID
    update_at: datetime
    create_at: datetime
