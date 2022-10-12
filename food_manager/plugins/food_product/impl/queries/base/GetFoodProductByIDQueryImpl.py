from logging import Logger
from uuid import UUID

from food_manager.plugins.food_product.base.core import GetFoodProductByIDQuery
from .....base.models import FoodProductDbModel
from food_manager.plugins.repositories.food_product.core import FoodProductRepository

__all__ = ['GetFoodProductByIDQueryImpl']


class GetFoodProductByIDQueryImpl(
    GetFoodProductByIDQuery
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

    async def __call__(
        self,
        id: UUID
    ) -> FoodProductDbModel:
        return await self.__repository.get_product(
            id=id
        )
