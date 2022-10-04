from typing import Collection
from uuid import UUID

from food_manager.plugins.food_manager.base.models import FoodProductDbModel
from food_manager.plugins.food_manager.base.models import FoodProductModel

__all__ = ['FoodProductRepository']


class FoodProductRepository:
    __slots__ = ()

    async def get_product(self, id: UUID) -> FoodProductDbModel:
        raise NotImplementedError

    async def get_all_products(self) -> Collection[FoodProductDbModel]:
        raise NotImplementedError

    async def add_product(self, product: FoodProductModel) -> None:
        raise NotImplementedError

    async def delete_product(self, id: UUID) -> None:
        raise NotImplementedError

    async def update_product(self, product: FoodProductModel) -> None:
        raise NotImplementedError
