from typing import Collection

from ...models import DishDbModel

__all__ = ['GetAllDishesQuery']


class GetAllDishesQuery:
    __slots__ = ()

    async def __call__(self) -> Collection[DishDbModel]:
        raise NotImplementedError
