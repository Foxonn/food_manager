from typing import Any

from .FoodProductRepositoryFactory import FoodProductRepositoryFactory

__all__ = ['FoodProductRepositoryStoreFactory']


class FoodProductRepositoryStoreFactory:
    __slots__ = ()

    def register(self, repository: FoodProductRepositoryFactory) -> None:
        raise NotImplementedError

    async def get_instance(
        self,
        type: str,
        settings: Any
    ) -> FoodProductRepositoryFactory:
        raise NotImplementedError
