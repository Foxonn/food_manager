import asyncio
import os

import pytest
from dotenv import load_dotenv
from galo_ioc import FactoryContainerImpl
from galo_ioc import get_factory

from food_manager.plugins.functions.core.commands import FactoryCommandsFactory
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


class TestCreateProductCommand:
    async def test_call(self) -> None:
        with FactoryContainerImpl():
            await initialization_plugins(
                module_names_path=os.getenv('MODULE_NAMES_PATH')
            )
            factory = get_factory(factory_type=FactoryCommandsFactory)
            cmd = await factory()

        await cmd.create_product_command(
            name='Смесь овощная Bonduelle Средиземноморская для жарки замороженная',
            price=39699,
            unit_measurement='г',
            units=700,
            proteins=18,
            fats=37,
            carbohydrates=83,
        )
