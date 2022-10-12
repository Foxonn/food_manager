from uuid import UUID

from aiologger import Logger

from .CreateDishCommandImpl import CreateDishCommandImpl
from .DeleteFoodProductCommandImpl import DeleteDishCommandImpl
from ....base.core.commands import CommandsFactory
from ....base.models import DishDbModel
from food_manager.plugins.repositories.food_product.core import FoodProductRepository

__all__ = ['BaseCommandsFactory']


class BaseCommandsFactory(
    CommandsFactory
):
    __slots__ = (
        '__logger',
        '__repository',
    )

    def __init__(
        self,
        logger: Logger,
        repository: FoodProductRepository
    ) -> None:
        self.__logger = logger
        self.__repository = repository

    async def create_dish_command(
        self,
        name: str,
        price: int,
        unit_measurement: str,
        units: int,
        proteins: int,
        fats: int,
        carbohydrates: int,
    ) -> DishDbModel:
        return await CreateDishCommandImpl(
            repository=self.__repository,
        )(
            name=name,
            price=price,
            unit_measurement=unit_measurement,
            units=units,
            proteins=proteins,
            fats=fats,
            carbohydrates=carbohydrates,
        )

    async def delete_product_command(
        self,
        id: UUID,
    ) -> None:
        await DeleteDishCommandImpl(
            repository=self.__repository,
        )(
            id=id,
        )
