from typing import List
from uuid import UUID

from aiologger import Logger

from .CreateDishCommandImpl import CreateDishCommandImpl
from .DeleteFoodProductCommandImpl import DeleteDishCommandImpl
from ....base.core.commands import DishCommandsFactory
from ....base.models import DishDbModel
from .....repositories.dish.core import DishRepository

__all__ = ['BaseDishCommandsFactory']


class BaseDishCommandsFactory(
    DishCommandsFactory
):
    __slots__ = (
        '__logger',
        '__repository',
    )

    def __init__(
        self,
        logger: Logger,
        repository: DishRepository
    ) -> None:
        self.__logger = logger
        self.__repository = repository

    async def create_dish_command(
        self,
        name: str,
        ingredients_ids: List[UUID],
    ) -> DishDbModel:
        return await CreateDishCommandImpl(
            repository=self.__repository,
        )(
            name=name,
            ingredients_ids=ingredients_ids,
        )

    async def delete_dish_command(
        self,
        id: UUID,
    ) -> None:
        await DeleteDishCommandImpl(
            repository=self.__repository,
        )(
            id=id,
        )
