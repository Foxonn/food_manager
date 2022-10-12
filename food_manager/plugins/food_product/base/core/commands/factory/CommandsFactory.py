from uuid import UUID

from food_manager.plugins.base.models import FoodProductDbModel

__all__ = ['CommandsFactory']


class CommandsFactory:
    __slots__ = ()

    async def create_product_command(
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

    async def delete_product_command(
        self,
        id: UUID,
    ) -> None:
        raise NotImplementedError
