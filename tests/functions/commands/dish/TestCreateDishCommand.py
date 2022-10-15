import asyncio
import os
from typing import List

import pytest
from faker import Faker
from galo_ioc import FactoryContainerImpl
from galo_ioc import get_factory

from food_manager.plugins.dish.base.core.commands import \
    FactoryDishCommandsFactory
from food_manager.plugins.dish.base.core.queries import \
    FactoryDishQueriesFactory
from food_manager.plugins.food_product.base.core.commands import \
    FactoryFoodProductCommandsFactory
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
                factory_type=FactoryDishQueriesFactory
            )
            dish_query = await factory()

            factory = get_factory(
                factory_type=FactoryFoodProductCommandsFactory
            )
            food_product_cmd = await factory()

        ingredients: List[FoodProductDbModel] = []
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
            ingredients.append(prod)

        dish = await dish_cmd.create_dish_command(
            name=f'{fake.name()}_dish',
            ingredients=ingredients
        )

        dish = await dish_query.get_dish_by_id_query(
            id=dish.id
        )

        assert dish
        assert dish.total_sum != 0
        assert dish.total_fats != 0
        assert dish.total_calories != 0
        assert dish.total_proteins != 0
        assert dish.total_carbohydrates != 0

        # await dish_cmd.delete_dish_command(id=dish.id)
        #
        # for product in ingredients:
        #     await food_product_cmd.delete_product_command(product.id)
