from typing import Collection

from food_manager.plugins.base.models import DishDbModel

__all__ = ['GetAllFoodProductsQuery']


class GetAllFoodProductsQuery:
    __slots__ = ()

    async def __call__(self) -> Collection[DishDbModel]:
        raise NotImplementedError
