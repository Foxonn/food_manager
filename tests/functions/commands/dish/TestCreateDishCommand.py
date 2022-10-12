import asyncio
import os

import pytest
from dotenv import load_dotenv
from faker import Faker
from galo_ioc import FactoryContainerImpl
from galo_ioc import get_factory

from food_manager.plugins.dish.base.core.commands import FactoryDishCommandsFactory
from food_manager.plugins.food_product.base.core.commands import \
    FactoryFoodProductCommandsFactory
from food_manager.plugins.food_product.base.models import FoodProductModel
from food_manager.plugins.food_product.base.models.MacronutrientsModel import \
    MacronutrientsModel
from food_manager.utils.initialization_plugins import initialization_plugins


@pytest.fixture(
    autouse=True,
    scope="session"
)
def init_env() -> None:
    load_dotenv(r'/.env')


@pytest.fixture(
    scope="session"
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


class TestCreateDishCommand:
    async def test_call(
        self,
        fake: Faker,
    ) -> None:
        with FactoryContainerImpl():
            await initialization_plugins(
                module_names_path=os.getenv('MODULE_NAMES_PATH')
            )
            factory = get_factory(
                factory_type=FactoryDishCommandsFactory
            )
            dish_cmd = await factory()

            factory = get_factory(
                factory_type=FactoryFoodProductCommandsFactory
            )
            food_product_cmd = await factory()

        food_products = []
        for i in range(2):
            prod = await food_product_cmd.create_product_command(
                name=fake.name(),
                price=fake.unique.random_int(),
                unit_measurement='г',
                units=fake.unique.random_int(),
                proteins=fake.unique.random_int(),
                fats=fake.unique.random_int(),
                carbohydrates=fake.unique.random_int(),
            )
            food_products.append(prod)

        dish = await dish_cmd.create_dish_command(
            name='mock_dish',
            ingredients=food_products
        )

        print('\n' + '*'*30)
        print(*[dish], sep='\n\r')
        print('*'*30 + '\n')
