from typing import Collection

from core.interfaces.ProductRequest import ProductRequest
from core.interfaces.Scraper import Scraper

__all__ = [
    "ScraperAuchan",
]


class ScraperAuchan(Scraper):
    __slots__ = (
        "__request"
    )

    def __init__(self, request: ProductRequest):
        self.__request = request

    @property
    def type(self) -> str:
        return "auchan"

    async def get_product(self, url: str) -> Collection:
        return await self.__request.get(url)
