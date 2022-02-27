from typing import (
    Any,
    Mapping
)

from core.interfaces.scraper.ProductScraper import ProductScraper

__all__ = [
    "ProductScraperFactory",
]


class ProductScraperFactory:
    @property
    def type(self) -> str:
        raise NotImplementedError

    async def get_instance(self, settings: Mapping[str, Any]) -> ProductScraper:
        raise NotImplementedError
