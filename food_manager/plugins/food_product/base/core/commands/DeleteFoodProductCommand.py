from uuid import UUID

__all__ = ['DeleteFoodProductCommand']


class DeleteFoodProductCommand:
    __slots__ = ()

    async def __call__(self, id: UUID) -> None:
        raise NotImplementedError
