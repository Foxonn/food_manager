from typing import List
from uuid import UUID

from .DishBaseModel import DishBaseModel
from ....food_product.base.models import FoodProductDbModel

__all__ = ['DishFromDbModel']


class DishFromDbModel(DishBaseModel):
    ingredients: List[UUID]
