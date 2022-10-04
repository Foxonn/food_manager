from typing import Collection
from uuid import UUID

from aiologger import Logger
from tinydb import TinyDB

from ...base.core.repository import FoodProductRepository
from ...base.models import FoodProductDbModel
from ...base.models import FoodProductModel

__all__ = ['FoodProductRepositoryTinyDB']


class FoodProductRepositoryTinyDB(
    FoodProductRepository
):
    __slots__ = (
        '__logger',
        '__tiny_db',
    )

    def __init__(
        self,
        logger: Logger,
        tiny_db: TinyDB,
    ) -> None:
        self.__logger = logger
        self.__tiny_db = tiny_db

    async def get_product(self, id: UUID) -> FoodProductDbModel:
        pass

    async def get_all_products(self) -> Collection[FoodProductDbModel]:
        pass

    async def add_product(self, product: FoodProductModel) -> None:
        pass

    async def delete_product(self, id: UUID) -> None:
        pass

    async def update_product(self, product: FoodProductModel) -> None:
        pass
