from typing import Collection
from uuid import UUID

from aiologger import Logger

from ...core import FoodProductRepository
from .....db_providers.providers.aiosqlite.base import AiosqliteFactory
from .....food_product.base.models import FoodProductDbModel

__all__ = ['FoodProductRepositoryAiosqlite']


class FoodProductRepositoryAiosqlite(
    FoodProductRepository
):
    __slots__ = (
        '__logger',
        '__aiosqlite_factory',
    )

    def __init__(
        self,
        logger: Logger,
        aiosqlite_factory: AiosqliteFactory,
    ) -> None:
        self.__logger = logger
        self.__aiosqlite_factory = aiosqlite_factory

    async def get_product(self, id: UUID) -> FoodProductDbModel:
        pass

    async def get_all_products(self) -> Collection[FoodProductDbModel]:
        pass

    async def add_product(self, product: FoodProductDbModel) -> None:
        pass

    async def delete_product(self, id: UUID) -> None:
        pass

    async def update_product(self, product: FoodProductDbModel) -> None:
        pass
