from typing import Collection

from base.core.request import RequestProduct
from base.core.scraper import ScraperProduct

__all__ = ['ScraperProductSbermarket']


class ScraperProductSbermarket(ScraperProduct):
    __slots__ = (
        "__request"
    )

    def __init__(self, request: RequestProduct):
        self.__request = request

    async def __call__(self, url: str) -> Collection:
        return await self.__request(url)
