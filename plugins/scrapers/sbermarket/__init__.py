from galo_ioc import add_factory, get_factory

from core.interfaces.request.RequestProductFactory import RequestProductFactory
from core.interfaces.scraper.ProductScraper import ProductScraper
from core.interfaces.scraper.ProductScraperFactory import ProductScraperFactory
from impl.scraper.instances import ProductScraperSbermarket

__all__ = [
    "load",
]


async def load() -> None:
    class ProductScraperSbermarketFactory(ProductScraperFactory):
        async def __call__(self) -> ProductScraper:
            return product_scraper_sbermarket

    request_factory = get_factory(RequestProductFactory)
    request = await request_factory()
    product_scraper_sbermarket = ProductScraperSbermarket(request)

    add_factory(
        ProductScraperFactory,
        ProductScraperSbermarketFactory()
    )
