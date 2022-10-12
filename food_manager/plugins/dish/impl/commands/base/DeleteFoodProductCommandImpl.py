from uuid import UUID

from ....base.core.commands import DeleteDishCommand
from .....repositories.dish.core import DishRepository

__all__ = ['DeleteDishCommandImpl']


class DeleteDishCommandImpl(
    DeleteDishCommand
):
    __slots__ = (
        '__repository',
    )

    def __init__(
        self,
        repository: DishRepository,
    ) -> None:
        self.__repository = repository

    async def __call__(
        self,
        id: UUID
    ) -> None:
        await self.__repository.delete_dish(
            id=id
        )
