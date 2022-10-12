from .DishCommandsFactory import DishCommandsFactory

__all__ = ['FactoryDishCommandsFactory']


class FactoryDishCommandsFactory:
    __slots__ = ()

    async def __call__(self) -> DishCommandsFactory:
        raise NotImplementedError
