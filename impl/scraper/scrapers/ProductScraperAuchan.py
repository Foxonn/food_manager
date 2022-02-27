from typing import Collection

from core.interfaces.request.ProductRequest import ProductRequest
from core.interfaces.scraper.ProductScraper import ProductScraper

__all__ = [
    "ProductScraperAuchan",
]


class ProductScraperAuchan(ProductScraper):
    __slots__ = (
        "__request"
    )

    def __init__(self, request: ProductRequest):
        self.__request = request

    @property
    def type(self) -> str:
        return "auchan"

    async def __call__(self, url: str) -> Collection:
        return await self.__request(url)
