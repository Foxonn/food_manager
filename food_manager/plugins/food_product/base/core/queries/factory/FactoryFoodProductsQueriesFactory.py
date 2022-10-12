from .FoodProductsQueriesFactory import FoodProductsQueriesFactory

__all__ = ['FactoryFoodProductsQueriesFactory']


class FactoryFoodProductsQueriesFactory:
    __slots__ = ()

    async def __call__(self) -> FoodProductsQueriesFactory:
        raise NotImplementedError
