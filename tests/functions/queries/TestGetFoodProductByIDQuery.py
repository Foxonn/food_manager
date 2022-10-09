import asyncio
import os
from uuid import UUID

import pytest
from dotenv import load_dotenv
from galo_ioc import FactoryContainerImpl
from galo_ioc import get_factory

from food_manager.plugins.base.models.exceptions import NotFoundException
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

        await cmd.get_food_product_by_id_query(
            id=UUID('5918182e-4faf-4690-8746-c3cb492df1cc')
        )

    async def test_exception_record_not_found(self) -> None:
        with FactoryContainerImpl():
            await initialization_plugins(
                module_names_path=os.getenv('MODULE_NAMES_PATH')
            )
            factory = get_factory(factory_type=FactoryQueriesFactory)
            cmd = await factory()

        with pytest.raises(NotFoundException):
            await cmd.get_food_product_by_id_query(
                id=UUID('6118182e-4faf-4690-8746-c3cb492df1cc')
            )
