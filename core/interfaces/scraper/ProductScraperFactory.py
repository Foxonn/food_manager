from core.interfaces.scraper.ProductScraper import ProductScraper

__all__ = [
    "ProductScraperFactory",
]


class ProductScraperFactory:
    async def __call__(self) -> ProductScraper:
        raise NotImplementedError
