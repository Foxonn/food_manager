from typing import List
from uuid import UUID

from ....models import DishDbModel

__all__ = ['CommandsFactory']


class CommandsFactory:
    __slots__ = ()

    async def create_dish_command(
        self,
        ingredients: List[DishDbModel]
    ) -> DishDbModel:
        raise NotImplementedError

    async def delete_dish_command(
        self,
        id: UUID,
    ) -> None:
        raise NotImplementedError
