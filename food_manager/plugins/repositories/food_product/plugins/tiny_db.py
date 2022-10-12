import os

from galo_ioc import add_factory
from galo_ioc import get_factory
from tinydb import TinyDB

from ..core import FoodProductRepository
from ..core import FoodProductRepositoryFactory
from ..impl.tiny_db import FoodProductRepositoryTinyDB
from food_manager.plugins.logger.core import LoggerFactory

__all__ = ['load']


async def load() -> None:
    factory_logger = get_factory(
        factory_type=LoggerFactory
    )
    logger = await factory_logger()
    db = TinyDB(os.getenv('TINY_DB_PATH'))

    class FoodProductRepositoryFactoryTinyDB(
        FoodProductRepositoryFactory
    ):
        async def __call__(self) -> FoodProductRepository:
            return repository

    repository = FoodProductRepositoryTinyDB(
        logger=logger,
        table=db.table('food_product')
    )

    add_factory(
        factory_type=FoodProductRepositoryFactory,
        factory=FoodProductRepositoryFactoryTinyDB()
    )
