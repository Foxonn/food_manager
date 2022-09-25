from typing import Collection

__all__ = ['RequestProduct']


class RequestProduct:
    __slots__ = ()

    async def __call__(self, url: str) -> Collection:
        raise NotImplementedError
