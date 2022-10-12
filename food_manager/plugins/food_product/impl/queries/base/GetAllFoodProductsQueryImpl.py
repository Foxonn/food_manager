from logging import Logger
from typing import Collection

from ....base.core.queries import GetAllFoodProductsQuery
from ....base.models import FoodProductDbModel
from .....repositories.food_product.core import FoodProductRepository

__all__ = ['GetAllFoodProductsQueryImpl']


class GetAllFoodProductsQueryImpl(
    GetAllFoodProductsQuery
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

    async def __call__(self) -> Collection[FoodProductDbModel]:
        return await self.__repository.get_all_products()
