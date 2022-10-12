from galo_ioc import add_factory
from galo_ioc import get_factory

from ...base.core.commands import FactoryFoodProductCommandsFactory
from ...base.core.commands import FoodProductCommandsFactory
from ...impl.commands.base import BaseFoodProductCommandsFactory
from ....logger.core import LoggerFactory
from ....repositories.food_product.core import FoodProductRepositoryFactory

__all__ = ['load']


async def load() -> None:
    logger_factory = get_factory(factory_type=LoggerFactory)
    repository_factory = get_factory(factory_type=FoodProductRepositoryFactory)
    logger = await logger_factory()
    repository = await repository_factory()

    class BaseFactoryFoodProductCommandsFactory(
        FactoryFoodProductCommandsFactory
    ):
        async def __call__(self) -> FoodProductCommandsFactory:
            return base_commands_factory

    base_commands_factory = BaseFoodProductCommandsFactory(
        logger=logger,
        repository=repository,
    )

    add_factory(
        factory_type=FactoryFoodProductCommandsFactory,
        factory=BaseFactoryFoodProductCommandsFactory()
    )
