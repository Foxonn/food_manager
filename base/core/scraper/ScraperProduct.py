from typing import Collection

__all__ = ['ScraperProduct']


class ScraperProduct:
    __slots__ = ()

    async def __call__(self, url: str) -> Collection:
        raise NotImplementedError
