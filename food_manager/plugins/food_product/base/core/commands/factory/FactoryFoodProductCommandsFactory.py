from .FoodProductCommandsFactory import FoodProductCommandsFactory

__all__ = ['FactoryFoodProductCommandsFactory']


class FactoryFoodProductCommandsFactory:
    __slots__ = ()

    async def __call__(self) -> FoodProductCommandsFactory:
        raise NotImplementedError
