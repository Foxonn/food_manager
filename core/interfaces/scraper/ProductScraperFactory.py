from core.interfaces.scraper import ScraperProduct

__all__ = ['ProductScraperFactory']


class ProductScraperFactory:
    async def __call__(self) -> ScraperProduct:
        raise NotImplementedError
