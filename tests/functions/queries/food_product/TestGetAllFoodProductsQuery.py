import asyncio
import os

import pytest
from dotenv import load_dotenv
from galo_ioc import FactoryContainerImpl
from galo_ioc import get_factory

from food_manager.plugins.food_product.base.core.queries import FactoryFoodProductsQueriesFactory
from food_manager.plugins.food_product.base.models import FoodProductDbModel
from food_manager.utils.initialization_plugins import initialization_plugins


@pytest.fixture(
    scope="session"
)
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


class TestGetFoodProductByIDQuery:
    async def test_call(self) -> None:
        with FactoryContainerImpl():
            await initialization_plugins(
                module_names_path=os.getenv('MODULE_NAMES_PATH')
            )
            factory = get_factory(
                factory_type=FactoryFoodProductsQueriesFactory
            )
            cmd = await factory()

        results = await cmd.get_all_products()

        assert results
        assert isinstance(results[0], FoodProductDbModel)
