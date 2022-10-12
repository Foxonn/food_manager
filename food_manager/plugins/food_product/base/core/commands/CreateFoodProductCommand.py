from food_manager.plugins.base.models import FoodProductDbModel

__all__ = ['CreateFoodProductCommand']


class CreateFoodProductCommand:
    __slots__ = ()

    async def __call__(
        self,
        name: str,
        price: int,
        unit_measurement: str,
        units: int,
        proteins: int,
        fats: int,
        carbohydrates: int,
    ) -> FoodProductDbModel:
        raise NotImplementedError
