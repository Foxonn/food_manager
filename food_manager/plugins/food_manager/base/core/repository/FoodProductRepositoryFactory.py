from typing import Any

from .FoodProductRepository import FoodProductRepository

__all__ = ['FoodProductRepositoryFactory']


class FoodProductRepositoryFactory:
    __slots__ = ()

    @property
    def type(self) -> str:
        raise NotImplementedError

    async def get_instance(self, settings: Any) -> FoodProductRepository:
        raise NotImplementedError
