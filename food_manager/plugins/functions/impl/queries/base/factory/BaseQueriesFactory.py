from typing import Collection
from uuid import UUID

from aiologger import Logger

from food_manager.plugins.functions.impl.queries.base.GetAllFoodProductsQueryImpl import GetAllFoodProductsQueryImpl
from food_manager.plugins.functions.impl.queries.base.GetFoodProductByIDQueryImpl import GetFoodProductByIDQueryImpl
from food_manager.plugins.functions.core.queries import QueriesFactory
from food_manager.plugins.base.models import FoodProductDbModel
from food_manager.plugins.repositories.core import FoodProductRepository

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
