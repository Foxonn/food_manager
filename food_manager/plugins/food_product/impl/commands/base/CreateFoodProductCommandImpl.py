from datetime import datetime
from uuid import uuid4

from ....base.core.commands import CreateFoodProductCommand
from ....base.models import FoodProductDbModel
from ....base.models.MacronutrientsModel import MacronutrientsModel
from .....repositories.food_product.core import FoodProductRepository

__all__ = ['CreateFoodProductCommandImpl']


class CreateFoodProductCommandImpl(
    CreateFoodProductCommand
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
        name: str,
        price: int,
        unit_measurement: str,
        units: int,
        proteins: int,
        fats: int,
        carbohydrates: int,
    ) -> FoodProductDbModel:
        product = FoodProductDbModel(
            name=name,
            price=price,
            unit_measurement=unit_measurement,
            units=units,
            macronutrients=MacronutrientsModel(
                proteins=proteins,
                fats=fats,
                carbohydrates=carbohydrates,
            ),
        )
        await self.__repository.add_product(
            product=product
        )
        return product
