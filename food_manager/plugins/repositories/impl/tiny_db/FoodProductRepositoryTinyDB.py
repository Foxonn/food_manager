import json
from typing import List
from uuid import UUID

from aiologger import Logger
from tinydb import Query
from tinydb.table import Table

from food_manager.plugins.base.models import FoodProductDbModel
from food_manager.plugins.base.models import FoodProductModel
from food_manager.plugins.base.models.exceptions import NotFoundException
from food_manager.plugins.repositories.core import FoodProductRepository

__all__ = ['FoodProductRepositoryTinyDB']


class FoodProductRepositoryTinyDB(
    FoodProductRepository
):
    __slots__ = (
        '__logger',
        '__db_factory',
        '__table',
    )

    def __init__(
        self,
        logger: Logger,
        table: Table,
    ) -> None:
        self.__logger = logger
        self.__table = table

    async def get_product(self, id: UUID) -> FoodProductDbModel:
        food_product = Query()
        records = self.__table.search(food_product.id == str(id))

        if not records:
            raise NotFoundException(id)

        return FoodProductDbModel(**records[0])

    async def get_all_products(self) -> List[FoodProductDbModel]:
        records = [
            FoodProductDbModel(**record)
            for record in self.__table.all()
        ]
        return records

    async def add_product(self, product: FoodProductDbModel) -> None:
        self.__table.insert(
            json.loads(
                product.json(
                    models_as_dict=True
                )
            )
        )

    async def delete_product(self, id: UUID) -> None:
        pass

    async def update_product(self, product: FoodProductModel) -> None:
        pass
