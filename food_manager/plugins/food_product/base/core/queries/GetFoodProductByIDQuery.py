from uuid import UUID

from ...models import FoodProductDbModel

__all__ = ['GetFoodProductByIDQuery']


class GetFoodProductByIDQuery:
    __slots__ = ()

    async def __call__(self, id: UUID) -> FoodProductDbModel:
        raise NotImplementedError
