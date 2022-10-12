from datetime import datetime
from typing import List
from uuid import uuid4

from ....base.core.commands import CreateDishCommand
from ....base.models import DishDbModel
from .....food_product.base.models import FoodProductDbModel
from food_manager.plugins.repositories.food_product.core import FoodProductRepository

__all__ = ['CreateDishCommandImpl']


class CreateDishCommandImpl(
    CreateDishCommand
):
    __slots__ = (
        '__repository',
    )

    def __init__(
        self,
        repository: FoodProductRepository,
    ) -> None:
        self.__repository = repository

    async def __call__(
        self,
        ingredients: List[FoodProductDbModel]
    ) -> DishDbModel:
        time = datetime.now()
        product = DishDbModel(
            id=uuid4(),
            ingredients=ingredients,
            created_at=time,
            updated_at=time,
        )
        await self.__repository.add_product(
            product=product
        )
        return product
