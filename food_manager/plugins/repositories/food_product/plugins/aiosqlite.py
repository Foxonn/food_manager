import os

from galo_ioc import add_factory
from galo_ioc import get_factory
from tinydb import TinyDB

from food_manager.plugins.db_providers.providers.aiosqlite.base import \
    AiosqliteFactory
from ..core import FoodProductRepository
from ..core import FoodProductRepositoryFactory
from ..impl.aiosqlite import FoodProductRepositoryAiosqlite
from ..impl.tiny_db import FoodProductRepositoryTinyDB
from food_manager.plugins.logger.core import LoggerFactory

__all__ = ['load']


async def load() -> None:
    factory_logger = get_factory(
        factory_type=LoggerFactory
    )
    aiosqlite = get_factory(
        factory_type=AiosqliteFactory
    )
    logger = await factory_logger()
    con = await aiosqlite()

    class FoodProductRepositoryFactoryAiosqlite(
        FoodProductRepositoryFactory
    ):
        async def __call__(self) -> FoodProductRepository:
            return repository

    repository = FoodProductRepositoryAiosqlite(
        logger=logger,
        con=con,
    )

    add_factory(
        factory_type=FoodProductRepositoryFactory,
        factory=FoodProductRepositoryFactoryAiosqlite()
    )
