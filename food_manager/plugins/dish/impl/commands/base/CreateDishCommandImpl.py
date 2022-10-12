from datetime import datetime
from typing import List
from uuid import UUID
from uuid import uuid4

from ....base.core.commands import CreateDishCommand
from ....base.models import DishDbModel
from .....repositories.dish.core import DishRepository

__all__ = ['CreateDishCommandImpl']


class CreateDishCommandImpl(
    CreateDishCommand
):
    __slots__ = (
        '__repository',
    )

    def __init__(
        self,
        repository: DishRepository,
    ) -> None:
        self.__repository = repository

    async def __call__(
        self,
        name: str,
        ingredients_ids: List[UUID]
    ) -> DishDbModel:
        time = datetime.now()
        dish = DishDbModel(
            id=uuid4(),
            name=name,
            ingredients_ids=ingredients_ids,
            created_at=time,
            updated_at=time,
        )
        await self.__repository.add_dish(
            dish=dish
        )
        return dish
