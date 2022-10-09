from aiologger import Logger

from food_manager.plugins.functions.core.commands import CommandsFactory
from food_manager.plugins.repositories.core import FoodProductRepository
from .CreateProductCommandImpl import CreateProductCommandImpl

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

    async def create_product_command(
        self,
        name: str,
        price: int,
        unit_measurement: str,
        units: int,
        proteins: int,
        fats: int,
        carbohydrates: int,
    ) -> None:
        await CreateProductCommandImpl(
            repository=self.__repository
        )(
            name=name,
            price=price,
            unit_measurement=unit_measurement,
            units=units,
            proteins=proteins,
            fats=fats,
            carbohydrates=carbohydrates,
        )
