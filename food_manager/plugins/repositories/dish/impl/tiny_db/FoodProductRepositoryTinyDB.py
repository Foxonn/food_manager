import asyncio
import json
from typing import List
from uuid import UUID

from aiologger import Logger
from tinydb import Query
from tinydb.table import Table

from food_manager.plugins.base.exceptions import NotFoundException
from food_manager.plugins.base.exceptions import RecordAlreadyExist
from food_manager.plugins.dish.base.models import DishDbModel
from food_manager.plugins.dish.base.models import DishFromDbModel
from food_manager.plugins.food_product.base.core.queries import FoodProductsQueriesFactory
from ...core import DishRepository

__all__ = ['DishRepositoryTinyDB']


class DishRepositoryTinyDB(
    DishRepository
):
    __dish = Query()

    __slots__ = (
        '__logger',
        '__table',
    )

    def __init__(
        self,
        logger: Logger,
        table: Table,
    ) -> None:
        self.__logger = logger
        self.__table = table

    async def get_dish_by_id(self, id: UUID) -> DishDbModel:
        records = self.__table.search(
            self.__dish.id == str(id)
        )

        if not records:
            raise NotFoundException(id)

        record = records[0]

        record = DishFromDbModel(
            id=record['id'],
            name=record['name'],
            ingredients=[i['id'] for i in record['ingredients']],
            # TODO: невозможно без запроса получить связанные данные
            updated_at=record['updated_at'],
            created_at=record['created_at'],
        )

        return record

    async def get_all_dishes(self) -> List[DishDbModel]:
        raise NotImplementedError

    async def add_dish(self, dish: DishDbModel) -> None:
        records = self.__table.search(
            self.__dish.name == str(dish.name)
        )
        if records:
            raise RecordAlreadyExist()

        data = json.loads(dish.json(models_as_dict=True))
        self.__table.insert(data)

    async def delete_dish(self, id: UUID) -> None:
        self.__table.remove(
            self.__dish.id == str(id)
        )

    async def update_dish(self, dish: DishDbModel) -> None:
        pass
