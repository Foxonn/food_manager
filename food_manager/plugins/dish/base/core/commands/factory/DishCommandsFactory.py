from typing import List
from uuid import UUID

from ....models import DishDbModel

__all__ = ['DishCommandsFactory']


class DishCommandsFactory:
    __slots__ = ()

    async def create_dish_command(
        self,
        name: str,
        ingredients_ids: List[UUID],
    ) -> DishDbModel:
        raise NotImplementedError

    async def delete_dish_command(
        self,
        id: UUID,
    ) -> None:
        raise NotImplementedError
