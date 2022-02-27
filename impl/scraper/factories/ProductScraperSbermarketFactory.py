from typing import (
    Any,
    Mapping,
)

from core.interfaces.scraper.ProductScraper import ProductScraper
from core.interfaces.scraper.ProductScraperFactory import ProductScraperFactory
from impl.scraper.instances import ProductScraperSbermarket

__all__ = ['ProductScraperSbermarketFactory']


class ProductScraperSbermarketFactory(ProductScraperFactory):
    @property
    def type(self) -> str:
        return "sbermarket"

    async def get_instance(
        self,
        settings: Mapping[str, Any]
    ) -> ProductScraper:
        return ProductScraperSbermarket(
            **settings
        )
