from galo_ioc import add_factory
from galo_ioc import get_factory

from ..core import DishRepository
from ..core import DishRepositoryFactory
from ..impl.aiosqlite import DishRepositoryAiosqlite
from ....db_providers.providers.aiosqlite.base import AiosqliteFactory
from ....logger.core import LoggerFactory

__all__ = ['load']


async def load() -> None:
    aiosqlite = get_factory(
        factory_type=AiosqliteFactory
    )
    factory_logger = get_factory(
        factory_type=LoggerFactory
    )
    logger = await factory_logger()

    class DishRepositoryFactoryAiosqlite(
        DishRepositoryFactory
    ):
        async def __call__(self) -> DishRepository:
            return repository

    repository = DishRepositoryAiosqlite(
        logger=logger,
        aiosqlite_factory=aiosqlite,
    )

    add_factory(
        factory_type=DishRepositoryFactory,
        factory=DishRepositoryFactoryAiosqlite()
    )
