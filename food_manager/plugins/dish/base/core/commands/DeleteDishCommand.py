from uuid import UUID

__all__ = ['DeleteDishCommand']


class DeleteDishCommand:
    __slots__ = ()

    async def __call__(self, id: UUID) -> None:
        raise NotImplementedError
