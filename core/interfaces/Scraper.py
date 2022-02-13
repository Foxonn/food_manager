from typing import Collection

__all__ = [
    "Scraper",
]


class Scraper:
    @property
    def type(self) -> str:
        raise NotImplementedError

    async def __call__(self, url: str) -> Collection:
        raise NotImplementedError
