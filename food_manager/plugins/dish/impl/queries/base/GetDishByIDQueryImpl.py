from logging import Logger
from uuid import UUID

from ....base.core.queries import GetDishByIDQuery
from ....base.models import DishDbModel
from .....repositories.dish.core import DishRepository

__all__ = ['GetDishByIDQueryImpl']


class GetDishByIDQueryImpl(
    GetDishByIDQuery
):
    __slots__ = (
        '__logger',
        '__repository',
    )

    def __init__(
        self,
        logger: Logger,
        repository: DishRepository
    ) -> None:
        self.__logger = logger
        self.__repository = repository

    async def __call__(
        self,
        id: UUID
    ) -> DishDbModel:
        return await self.__repository.get_dish(
            id=id
        )
