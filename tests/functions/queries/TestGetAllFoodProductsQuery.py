import asyncio
import os

import pytest
from dotenv import load_dotenv
from galo_ioc import FactoryContainerImpl
from galo_ioc import get_factory

from food_manager.plugins.base.models import FoodProductDbModel
from food_manager.plugins.functions.core.queries import FactoryQueriesFactory
from food_manager.utils.initialization_plugins import initialization_plugins


@pytest.fixture(autouse=True, scope="session")
def init_env() -> None:
    load_dotenv(r'D:\Development\food_manager\.env')


@pytest.fixture(scope="session")
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
            factory = get_factory(factory_type=FactoryQueriesFactory)
            cmd = await factory()

        results = await cmd.get_all_products()

        assert results
        assert isinstance(results[0], FoodProductDbModel)
