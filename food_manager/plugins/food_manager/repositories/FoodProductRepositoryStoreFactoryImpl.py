from typing import Any

from ..base.core.repository import FoodProductRepositoryFactory
from ..base.core.repository import FoodProductRepositoryStoreFactory

__all__ = ['FoodProductRepositoryStoreFactoryImpl']


class StoreFactoriesRepositories(dict):
    def __setitem__(
        self,
        k: FoodProductRepositoryFactory,
        v: FoodProductRepositoryFactory
    ) -> None:
        k = k.type
        super().__setitem__(k, v)

    def __getitem__(
        self,
        k: str
    ) -> FoodProductRepositoryFactory:
        return super().__getitem__(k)


_store_factories_repositories = StoreFactoriesRepositories()


class FoodProductRepositoryStoreFactoryImpl(
    FoodProductRepositoryStoreFactory
):
    __slots__ = ()

    def register(self, repository: FoodProductRepositoryFactory) -> None:
        _store_factories_repositories[repository] = repository

    async def get_instance(
        self,
        type: str,
        settings: Any
    ) -> FoodProductRepositoryFactory:
        try:
            return _store_factories_repositories[type]
        except KeyError as err:
            raise KeyError(f'Type repository: {type} not found!.') from err
