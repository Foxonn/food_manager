from galo_ioc import add_factory
from galo_ioc import get_factory

from core.interfaces.request import RequestProductFactory
from core.interfaces.scraper import ScraperProduct
from core.interfaces.scraper import ProductScraperFactory
from impl.scraper.instances import ScraperProductSbermarket

__all__ = ["load", ]


async def load() -> None:
    class ProductScraperSbermarketFactory(ProductScraperFactory):
        async def __call__(self) -> ScraperProduct:
            return product_scraper_sbermarket

    request_factory = get_factory(RequestProductFactory)
    request = await request_factory()
    product_scraper_sbermarket = ScraperProductSbermarket(request)

    add_factory(
        ProductScraperFactory,
        ProductScraperSbermarketFactory()
    )
