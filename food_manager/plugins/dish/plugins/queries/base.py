from galo_ioc import add_factory
from galo_ioc import get_factory

from ...base.core.queries import DishQueriesFactory
from ...base.core.queries import FactoryDishQueriesFactory
from ...impl.queries.base import BaseDishQueriesFactory
from ....logger.core import LoggerFactory
from ....repositories.dish.core import DishRepositoryFactory

__all__ = ['load']


async def load() -> None:
    logger_factory = get_factory(factory_type=LoggerFactory)
    repository_factory = get_factory(factory_type=DishRepositoryFactory)
    logger = await logger_factory()
    repository = await repository_factory()

    class BaseFactoryDishQueriesFactory(FactoryDishQueriesFactory):
        async def __call__(self) -> DishQueriesFactory:
            return base_queries_factory

    base_queries_factory = BaseDishQueriesFactory(
        logger=logger,
        repository=repository,
    )

    add_factory(
        factory_type=FactoryDishQueriesFactory,
        factory=BaseFactoryDishQueriesFactory()
    )
