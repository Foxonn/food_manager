from aiosqlite import Connection

__all__ = ['AiosqliteFactory']


class AiosqliteFactory:
    __slots__ = ()

    async def __call__(self) -> Connection:
        raise NotImplementedError
