from uuid import UUID

from food_manager.plugins.food_product.base.core import DeleteFoodProductCommand
from food_manager.plugins.repositories.food_product.core import FoodProductRepository

__all__ = ['DeleteFoodProductCommandImpl']


class DeleteFoodProductCommandImpl(
    DeleteFoodProductCommand
):
    __slots__ = (
        '__repository',
    )

    def __init__(
        self,
        repository: FoodProductRepository,
    ) -> None:
        self.__repository = repository

    async def __call__(
        self,
        id: UUID
    ) -> None:
        await self.__repository.delete_product(
            id=id
        )
