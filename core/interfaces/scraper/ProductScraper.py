from typing import Collection

__all__ = [
    "ProductScraper",
]


class ProductScraper:
    async def __call__(self, url: str) -> Collection:
        raise NotImplementedError
