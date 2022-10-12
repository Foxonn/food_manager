from typing import List

from ...models import DishBaseModel
from ...models import DishModel
from .....food_product.base.models import FoodProductDbModel

__all__ = ['CreateDishCommand']


class CreateDishCommand:
    __slots__ = ()

    async def __call__(
        self,
        name: str,
        ingredients: List[FoodProductDbModel]
    ) -> DishModel:
        raise NotImplementedError
