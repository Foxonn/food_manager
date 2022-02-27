from typing import (
    Any,
    Mapping
)

from core.interfaces.scraper.ProductScraper import ProductScraper

__all__ = [
    "ProductScraperFactoryStoreFactory",
]


class ProductScraperFactoryStoreFactory:
    async def add_instance(self, instance: ProductScraper) -> None:
        raise NotImplementedError

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> ProductScraper:
        raise NotImplementedError
