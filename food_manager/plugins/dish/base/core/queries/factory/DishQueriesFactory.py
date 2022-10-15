from typing import Collection
from uuid import UUID

from ....models import DishDbModel

__all__ = ['DishQueriesFactory']


class DishQueriesFactory:
    __slots__ = ()

    async def get_dish_by_id_query(self, id: UUID) -> DishDbModel:
        raise NotImplementedError

    async def get_all_dishes(self) -> Collection[DishDbModel]:
        raise NotImplementedError
