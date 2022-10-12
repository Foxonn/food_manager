from galo_ioc import add_factory
from galo_ioc import get_factory

from food_manager.plugins.dish.base.core import CommandsFactory
from food_manager.plugins.dish.base.core import FactoryCommandsFactory
from ...impl.commands.base import BaseCommandsFactory
from ....logger.core import LoggerFactory
from food_manager.plugins.repositories.food_product.core import FoodProductRepositoryFactory

__all__ = ['load']


async def load() -> None:
    logger_factory = get_factory(factory_type=LoggerFactory)
    repository_factory = get_factory(factory_type=FoodProductRepositoryFactory)
    logger = await logger_factory()
    repository = await repository_factory()

    class BaseFactoryCommandsFactory(FactoryCommandsFactory):
        async def __call__(self) -> CommandsFactory:
            return base_commands_factory

    base_commands_factory = BaseCommandsFactory(
        logger=logger,
        repository=repository,
    )

    add_factory(
        factory_type=FactoryCommandsFactory,
        factory=BaseFactoryCommandsFactory()
    )
