import os

from galo_ioc import add_factory
from galo_ioc import get_factory
from tinydb import TinyDB

from ..core import DishRepository
from ..core import DishRepositoryFactory
from ..impl.tiny_db import DishRepositoryTinyDB
from food_manager.plugins.logger.core import LoggerFactory

__all__ = ['load']


async def load() -> None:
    factory_logger = get_factory(
        factory_type=LoggerFactory
    )
    logger = await factory_logger()
    db = TinyDB(os.getenv('TINY_DB_PATH'))

    class DishRepositoryFactoryTinyDB(
        DishRepositoryFactory
    ):
        async def __call__(self) -> DishRepository:
            return repository

    repository = DishRepositoryTinyDB(
        logger=logger,
        table=db.table('dish')
    )

    add_factory(
        factory_type=DishRepositoryFactory,
        factory=DishRepositoryFactoryTinyDB()
    )
