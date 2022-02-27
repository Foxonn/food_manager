from core.interfaces.scraper.ProductScraper import ProductScraper

__all__ = [
    "ProductScraperFactoryStoreFactory",
]


class ProductScraperFactoryStoreFactory:
    async def add_instance(self, instance: ProductScraper) -> None:
        raise NotImplementedError

    async def get_instance(self, type: str) -> ProductScraper:
        raise NotImplementedError
