from uuid import UUID

from aiologger import Logger

from .CreateFoodProductCommandImpl import CreateFoodProductCommandImpl
from .DeleteFoodProductCommandImpl import DeleteFoodProductCommandImpl
from ....core.commands import CommandsFactory
from .....base.models import FoodProductDbModel
from .....repositories.core import FoodProductRepository

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
    ) -> FoodProductDbModel:
        return await CreateFoodProductCommandImpl(
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
        await DeleteFoodProductCommandImpl(
            repository=self.__repository,
        )(
            id=id,
        )
