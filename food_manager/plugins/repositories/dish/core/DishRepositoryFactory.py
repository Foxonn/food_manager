from .DishRepository import DishRepository

__all__ = ['DishRepositoryFactory']


class DishRepositoryFactory:
    __slots__ = ()

    async def __call__(self) -> DishRepository:
        raise NotImplementedError
