from typing import Collection
from uuid import UUID

from aiologger import Logger

from ...core import DishRepository
from .....db_providers.providers.aiosqlite.base import AiosqliteFactory
from .....dish.base.models import DishDbModel

__all__ = ['DishRepositoryAiosqlite']


class DishRepositoryAiosqlite(
    DishRepository
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

    async def get_dish(self, id: UUID) -> DishDbModel:
        pass

    async def get_all_dishes(self) -> Collection[DishDbModel]:
        pass

    async def add_dish(self, dish: DishDbModel) -> None:
        pass

    async def delete_dish(self, id: UUID) -> None:
        pass

    async def update_dish(self, dish: DishDbModel) -> None:
        pass
