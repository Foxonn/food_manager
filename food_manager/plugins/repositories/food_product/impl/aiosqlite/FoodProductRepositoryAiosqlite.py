from typing import Collection
from uuid import UUID

from aiologger import Logger
from aiosqlite import Connection

from ...core import FoodProductRepository
from .....food_product.base.models import FoodProductDbModel

__all__ = ['FoodProductRepositoryAiosqlite']


class FoodProductRepositoryAiosqlite(
    FoodProductRepository
):
    __slots__ = (
        '__logger',
        '__con',
    )

    def __init__(
        self,
        logger: Logger,
        con: Connection,
    ) -> None:
        self.__logger = logger
        self.__con = con

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
