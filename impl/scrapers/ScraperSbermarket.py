from typing import Collection

from core.interfaces.ProductRequest import ProductRequest
from core.interfaces.Scraper import Scraper

__all__ = [
    "ScraperSbermarket",
]


class ScraperSbermarket(Scraper):
    __slots__ = (
        "__request"
    )

    def __init__(self, request: ProductRequest):
        self.__request = request

    @property
    def type(self) -> str:
        return "sbermarket"

    async def __call__(self, url: str) -> Collection:
        return await self.__request(url)
