from typing import Any
from typing import Mapping

from aiologger import Logger
from tinydb import TinyDB

from .FoodProductRepositoryTinyDB import FoodProductRepositoryTinyDB
from .TinyDBSettings import TinyDBSettings
from ...base.core.repository import FoodProductRepositoryFactory

__all__ = ['FoodProductRepositoryFactoryTinyDB']


class FoodProductRepositoryFactoryTinyDB(
    FoodProductRepositoryFactory
):
    __slots__ = (
        '__logger',
    )

    def __init__(
        self,
        logger: Logger,
    ) -> None:
        self.__logger = logger

    @property
    def type(self) -> str:
        raise 'tiny_db'

    async def get_instance(
        self,
        settings: Mapping[str, Any]
    ) -> FoodProductRepositoryTinyDB:
        settings = TinyDBSettings(**settings)
        return FoodProductRepositoryTinyDB(
            logger=self.__logger,
            tiny_db=TinyDB(
                storage=settings.storage
            )
        )
