from typing import Collection

from core.interfaces.request.RequestProduct import RequestProduct
from core.interfaces.scraper.ProductScraper import ProductScraper

__all__ = [
    "ProductScraperSbermarket",
]


class ProductScraperSbermarket(ProductScraper):
    __slots__ = (
        "__request"
    )

    def __init__(self, request: RequestProduct):
        self.__request = request

    async def __call__(self, url: str) -> Collection:
        return await self.__request(url)
