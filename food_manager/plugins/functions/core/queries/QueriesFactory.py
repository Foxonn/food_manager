from uuid import UUID

from ....base.models import FoodProductDbModel

__all__ = ['QueriesFactory']


class QueriesFactory:
    __slots__ = ()

    async def get_food_product_by_id_query(
        self,
        id: UUID
    ) -> FoodProductDbModel:
        raise NotImplementedError
