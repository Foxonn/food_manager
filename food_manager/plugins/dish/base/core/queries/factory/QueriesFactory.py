from typing import Collection
from uuid import UUID

from food_manager.plugins.base.models import FoodProductDbModel

__all__ = ['QueriesFactory']


class QueriesFactory:
    __slots__ = ()

    async def get_dish_by_id_query(
        self,
        id: UUID
    ) -> FoodProductDbModel:
        raise NotImplementedError

    async def get_all_dishes(self) -> Collection[FoodProductDbModel]:
        raise NotImplementedError
