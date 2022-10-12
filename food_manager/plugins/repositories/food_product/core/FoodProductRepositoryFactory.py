from .FoodProductRepository import FoodProductRepository

__all__ = ['FoodProductRepositoryFactory']


class FoodProductRepositoryFactory:
    __slots__ = ()

    async def __call__(self) -> FoodProductRepository:
        raise NotImplementedError
