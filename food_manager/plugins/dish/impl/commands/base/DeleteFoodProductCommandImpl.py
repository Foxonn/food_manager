from uuid import UUID

from food_manager.plugins.dish.base.core import DeleteDishCommand
from food_manager.plugins.repositories.food_product.core import FoodProductRepository

__all__ = ['DeleteDishCommandImpl']


class DeleteDishCommandImpl(
    DeleteDishCommand
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
