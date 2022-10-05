from typing import Any
from typing import Mapping

from .FoodProductRepository import FoodProductRepository

__all__ = ['FoodProductRepositoryFactory']


class FoodProductRepositoryFactory:
    __slots__ = ()

    @property
    def type(self) -> str:
        raise NotImplementedError

    async def get_instance(
        self,
        settings: Mapping[str, Any]
    ) -> FoodProductRepository:
        raise NotImplementedError
