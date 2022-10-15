from typing import List

from pydantic import BaseModel

from ....food_product.base.models import FoodProductDbModel

__all__ = ['DishPreviewModel']


class DishPreviewModel(BaseModel):
    ingredients: List[FoodProductDbModel]
