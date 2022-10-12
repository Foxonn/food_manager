from typing import List
from uuid import UUID

from .DishBaseModel import DishBaseModel

__all__ = ['DishDbModel']


class DishDbModel(DishBaseModel):
    ingredients_ids: List[UUID]
