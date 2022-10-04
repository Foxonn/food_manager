from typing import Any

from .FoodProductRepositoryTinyDB import FoodProductRepositoryTinyDB
from ...base.core.repository import FoodProductRepositoryFactory

__all__ = ['FoodProductRepositoryFactoryTinyDB']


class FoodProductRepositoryFactoryTinyDB(
    FoodProductRepositoryFactory
):
    __slots__ = ()

    @property
    def type(self) -> str:
        raise 'tiny_db'

    async def get_instance(self, settings: Any) -> FoodProductRepositoryTinyDB:
        return FoodProductRepositoryTinyDB()
