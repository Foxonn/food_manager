from typing import Collection
from uuid import UUID

from aiologger import Logger

from ..GetDishByIDQueryImpl import GetDishByIDQueryImpl
from ..GetAllDishesQueryImpl import GetAllDishesQueryImpl
from .....base.core.queries import DishQueriesFactory
from .....base.models import DishDbModel
from ......repositories.dish.core import DishRepository

__all__ = ['BaseDishQueriesFactory']


class BaseDishQueriesFactory(
    DishQueriesFactory
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

    async def get_dish_by_id_query(
        self,
        id: UUID
    ) -> DishDbModel:
        return await GetDishByIDQueryImpl(
            logger=self.__logger,
            repository=self.__repository,
        )(
            id=id
        )

    async def get_all_dishes(self) -> Collection[DishDbModel]:
        return await GetAllDishesQueryImpl(
            logger=self.__logger,
            repository=self.__repository,
        )()
