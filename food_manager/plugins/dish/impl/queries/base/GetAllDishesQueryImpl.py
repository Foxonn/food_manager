from logging import Logger
from typing import Collection

from ....base.core.queries import GetAllDishesQuery
from ....base.models import DishDbModel
from .....repositories.dish.core import DishRepository

__all__ = ['GetAllDishesQueryImpl']


class GetAllDishesQueryImpl(
    GetAllDishesQuery
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

    async def __call__(self) -> Collection[DishDbModel]:
        return await self.__repository.get_all_dishes()
