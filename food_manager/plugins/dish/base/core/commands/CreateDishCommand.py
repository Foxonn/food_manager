from typing import List

from ...models import DishDbModel
from .....food_product.base.models import FoodProductDbModel

__all__ = ['CreateDishCommand']


class CreateDishCommand:
    __slots__ = ()

    async def __call__(
        self,
        name: str,
        ingredients: List[FoodProductDbModel]
    ) -> DishDbModel:
        raise NotImplementedError
