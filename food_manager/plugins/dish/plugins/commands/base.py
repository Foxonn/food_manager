from galo_ioc import add_factory
from galo_ioc import get_factory

from ...base.core.commands import DishCommandsFactory
from ...base.core.commands import FactoryDishCommandsFactory
from ...impl.commands.base import BaseDishCommandsFactory
from ....logger.core import LoggerFactory
from ....repositories.food_product.core import FoodProductRepositoryFactory

__all__ = ['load']


async def load() -> None:
    logger_factory = get_factory(factory_type=LoggerFactory)
    repository_factory = get_factory(factory_type=FoodProductRepositoryFactory)
    logger = await logger_factory()
    repository = await repository_factory()

    class BaseFactoryDishCommandsFactory(FactoryDishCommandsFactory):
        async def __call__(self) -> DishCommandsFactory:
            return base_commands_factory

    base_commands_factory = BaseDishCommandsFactory(
        logger=logger,
        repository=repository,
    )

    add_factory(
        factory_type=FactoryDishCommandsFactory,
        factory=BaseFactoryDishCommandsFactory()
    )
