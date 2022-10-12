from galo_ioc import add_factory
from galo_ioc import get_factory

from ...base.core.queries import FactoryFoodProductsQueriesFactory
from ...base.core.queries import FoodProductsQueriesFactory
from ...impl.queries.base import BaseFoodProductsQueriesFactory
from ....logger.core import LoggerFactory
from ....repositories.food_product.core import FoodProductRepositoryFactory

__all__ = ['load']


async def load() -> None:
    logger_factory = get_factory(factory_type=LoggerFactory)
    repository_factory = get_factory(factory_type=FoodProductRepositoryFactory)
    logger = await logger_factory()
    repository = await repository_factory()

    class BaseFactoryFoodProductsQueriesFactory(
        FactoryFoodProductsQueriesFactory
    ):
        async def __call__(self) -> FoodProductsQueriesFactory:
            return base_queries_factory

    base_queries_factory = BaseFoodProductsQueriesFactory(
        logger=logger,
        repository=repository,
    )

    add_factory(
        factory_type=FactoryFoodProductsQueriesFactory,
        factory=BaseFactoryFoodProductsQueriesFactory()
    )
