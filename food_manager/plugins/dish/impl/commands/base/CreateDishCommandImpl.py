from datetime import datetime
from typing import List
from uuid import uuid4

from ....base.core.commands import CreateDishCommand
from ....base.models import DishDbModel
from .....food_product.base.models import FoodProductDbModel
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
        ingredients: List[FoodProductDbModel]
    ) -> DishDbModel:
        dish = DishDbModel(
            name=name,
            ingredients=ingredients,
        )
        await self.__repository.add_dish(
            dish=dish
        )
        return dish
