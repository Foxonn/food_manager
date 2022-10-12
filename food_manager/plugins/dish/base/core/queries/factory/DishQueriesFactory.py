from typing import Collection
from uuid import UUID

from ....models import DishModel

__all__ = ['DishQueriesFactory']


class DishQueriesFactory:
    __slots__ = ()

    async def get_dish_by_id_query(self, id: UUID) -> DishModel:
        raise NotImplementedError

    async def get_all_dishes(self) -> Collection[DishModel]:
        raise NotImplementedError
