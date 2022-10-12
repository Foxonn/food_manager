from uuid import UUID

from ....base.models import DishDbModel

__all__ = ['GetDishByIDQuery']


class GetDishByIDQuery:
    __slots__ = ()

    async def __call__(self, id: UUID) -> DishDbModel:
        raise NotImplementedError
