from typing import Collection
from uuid import UUID

from aiologger import Logger

from .GetAllFoodProductsQueryImpl import GetAllFoodProductsQueryImpl
from .GetFoodProductByIDQueryImpl import GetFoodProductByIDQueryImpl
from ....core.queries import QueriesFactory
from .....base.models import FoodProductDbModel
from .....repositories.core import FoodProductRepository

__all__ = ['BaseQueriesFactory']


class BaseQueriesFactory(
    QueriesFactory
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

    async def get_food_product_by_id_query(
        self,
        id: UUID
    ) -> FoodProductDbModel:
        return await GetFoodProductByIDQueryImpl(
            logger=self.__logger,
            repository=self.__repository,
        )(
            id=id
        )

    async def get_all_products(self) -> Collection[FoodProductDbModel]:
        return await GetAllFoodProductsQueryImpl(
            logger=self.__logger,
            repository=self.__repository,
        )()
