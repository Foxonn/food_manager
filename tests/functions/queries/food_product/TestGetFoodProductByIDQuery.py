import asyncio
import os
from uuid import UUID

import pytest
from dotenv import load_dotenv
from faker import Faker
from galo_ioc import FactoryContainerImpl
from galo_ioc import get_factory

from food_manager.plugins.base.exceptions import NotFoundException
from food_manager.plugins.food_product.base.core.commands import FactoryFoodProductCommandsFactory
from food_manager.plugins.food_product.base.core.queries import FactoryFoodProductsQueriesFactory
from food_manager.utils.initialization_plugins import initialization_plugins


@pytest.fixture(
    autouse=True,
    scope="session"
)
def init_env() -> None:
    load_dotenv(r'/.env')


@pytest.fixture(
    scope='session'
)
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(
    scope='session'
)
def fake() -> Faker:
    return Faker()


class TestGetFoodProductByIDQuery:
    async def test_call(
        self,
        fake: fake,
    ) -> None:
        with FactoryContainerImpl():
            await initialization_plugins(
                module_names_path=os.getenv('MODULE_NAMES_PATH')
            )
            factory = get_factory(
                factory_type=FactoryFoodProductCommandsFactory
            )
            cmd = await factory()
            factory = get_factory(
                factory_type=FactoryFoodProductsQueriesFactory
            )
            query = await factory()

        product = await cmd.create_product_command(
            name=fake.name(),
            price=fake.unique.random_int(),
            unit_measurement='г',
            units=fake.unique.random_int(),
            proteins=fake.unique.random_int(),
            fats=fake.unique.random_int(),
            carbohydrates=fake.unique.random_int(),
        )
        record = await query.get_food_product_by_id_query(
            id=product.id
        )
        assert record

    async def test_exception_record_not_found(self) -> None:
        with FactoryContainerImpl():
            await initialization_plugins(
                module_names_path=os.getenv('MODULE_NAMES_PATH')
            )
            factory = get_factory(
                factory_type=FactoryFoodProductsQueriesFactory
            )
            cmd = await factory()

        with pytest.raises(NotFoundException):
            await cmd.get_food_product_by_id_query(
                id=UUID('6118182e-4faf-4690-8746-c3cb492df1cc')
            )
