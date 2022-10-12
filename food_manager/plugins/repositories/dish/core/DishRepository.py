from typing import Collection
from uuid import UUID

from ....dish.base.models import DishDbModel
from ....dish.base.models import DishModel

__all__ = ['DishRepository']


class DishRepository:
    __slots__ = ()

    async def get_dish(self, id: UUID) -> DishModel:
        raise NotImplementedError

    async def get_all_dishes(self) -> Collection[DishModel]:
        raise NotImplementedError

    async def add_dish(self, dish: DishDbModel) -> None:
        raise NotImplementedError

    async def delete_dish(self, id: UUID) -> None:
        raise NotImplementedError

    async def update_dish(self, dish: DishModel) -> None:
        raise NotImplementedError
