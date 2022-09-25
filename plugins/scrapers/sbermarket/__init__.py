from galo_ioc import add_factory
from galo_ioc import get_factory

from base.core.request import RequestProductFactory
from base.core.scraper import ScraperProduct
from base.core.scraper import ScraperProductFactory
from impl.scraper.instances import ScraperProductSbermarket

__all__ = ["load", ]


async def load() -> None:
    class ProductScraperSbermarketFactory(ScraperProductFactory):
        async def __call__(self) -> ScraperProduct:
            return product_scraper_sbermarket

    request_factory = get_factory(RequestProductFactory)
    request = await request_factory()
    product_scraper_sbermarket = ScraperProductSbermarket(request)

    add_factory(
        ScraperProductFactory,
        ProductScraperSbermarketFactory()
    )
