from .DishQueriesFactory import DishQueriesFactory

__all__ = ['FactoryDishQueriesFactory']


class FactoryDishQueriesFactory:
    __slots__ = ()

    async def __call__(self) -> DishQueriesFactory:
        raise NotImplementedError
