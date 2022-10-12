from typing import Collection
from uuid import UUID

from aiologger import Logger

from ..GetAllFoodProductsQueryImpl import GetAllFoodProductsQueryImpl
from ..GetFoodProductByIDQueryImpl import GetFoodProductByIDQueryImpl
from .....base.core.queries import FoodProductsQueriesFactory
from .....base.models import FoodProductDbModel
from ......repositories.food_product.core import FoodProductRepository

__all__ = ['BaseFoodProductsQueriesFactory']


class BaseFoodProductsQueriesFactory(
    FoodProductsQueriesFactory
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
