from galo_ioc import add_factory
from galo_ioc import get_factory

from food_manager.plugins.food_product.base.core import QueriesFactory
from food_manager.plugins.food_product.base.core import FactoryQueriesFactory
from ...impl.queries.base import BaseQueriesFactory
from ....logger.core import LoggerFactory
from food_manager.plugins.repositories.food_product.core import FoodProductRepositoryFactory

__all__ = ['load']


async def load() -> None:
    logger_factory = get_factory(factory_type=LoggerFactory)
    repository_factory = get_factory(factory_type=FoodProductRepositoryFactory)
    logger = await logger_factory()
    repository = await repository_factory()

    class BaseFactoryQueriesFactory(FactoryQueriesFactory):
        async def __call__(self) -> QueriesFactory:
            return base_queries_factory

    base_queries_factory = BaseQueriesFactory(
        logger=logger,
        repository=repository,
    )

    add_factory(
        factory_type=FactoryQueriesFactory,
        factory=BaseFactoryQueriesFactory()
    )
