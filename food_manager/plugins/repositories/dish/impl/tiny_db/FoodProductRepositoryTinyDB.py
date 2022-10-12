import json
from typing import List
from uuid import UUID

from aiologger import Logger
from tinydb import Query
from tinydb.table import Table

from food_manager.plugins.dish.base.models import DishDbModel
from ...core import DishRepository
from food_manager.plugins.base.exceptions import NotFoundException
from food_manager.plugins.base.exceptions import RecordAlreadyExist


__all__ = ['DishRepositoryTinyDB']


class DishRepositoryTinyDB(
    DishRepository
):
    __dish = Query()

    __slots__ = (
        '__logger',
        '__table',
        '__db_factory',
    )

    def __init__(
        self,
        logger: Logger,
        table: Table,
    ) -> None:
        self.__logger = logger
        self.__table = table

    async def get_dish(self, id: UUID) -> DishDbModel:
        records = self.__table.search(
            self.__dish.id == str(id)
        )

        if not records:
            raise NotFoundException(id)

        return DishDbModel(**records[0])

    async def get_all_dishes(self) -> List[DishDbModel]:
        records = [
            DishDbModel(**record)
            for record in self.__table.all()
        ]
        return records

    async def add_dish(self, dish: DishDbModel) -> None:
        records = self.__table.search(
            self.__dish.name == str(dish.name)
        )
        if records:
            raise RecordAlreadyExist()
        self.__table.insert(
            json.loads(
                dish.json(
                    models_as_dict=True
                )
            )
        )

    async def delete_dish(self, id: UUID) -> None:
        self.__table.remove(
            self.__dish.id == str(id)
        )

    async def update_dish(self, dish: DishDbModel) -> None:
        pass
