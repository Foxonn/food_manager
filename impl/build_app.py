from galo_ioc import add_factory


from core.interfaces.scraper.ProductScraperFactory import ProductScraperFactory
from impl.scraper import product_scraper_factory
from impl.scraper.scrapers import (
    ProductScraperAuchan,
    ProductScraperSbermarket
)

from core.interfaces.request.ProductRequestFactory import ProductRequestFactory
from impl.request import product_request_factory
from impl.request.requests import (
    ProductRequestHtmlRequest,
    ProductRequestPyppeteer,
    ProductRequestSelenium,
    ProductRequestAiohttp
)

from core.interfaces.tasks_manager.TaskScraperManagerFactory import TaskScraperManagerFactory
from impl.tasks_scraper_manager import task_scraper_manager_factory
from impl.tasks_scraper_manager.tasks_managers import TaskScraperManagerImpl

from core.interfaces.extractor.ProductExtractorFactory import ProductExtractorFactory
from impl.extractor import product_extractor_factory
from impl.extractor.extractors import (
    ProductExtractorAuchan,
    ProductExtractorSbermarket
)

__all__ = ['build_app']


async def build_app() -> None:
    await product_request_factory.add_instance(ProductRequestHtmlRequest)
    await product_request_factory.add_instance(ProductRequestPyppeteer)
    await product_request_factory.add_instance(ProductRequestSelenium)
    await product_request_factory.add_instance(ProductRequestAiohttp)

    await product_scraper_factory.add_instance(ProductScraperAuchan)
    await product_scraper_factory.add_instance(ProductScraperSbermarket)

    await task_scraper_manager_factory.add_instance(TaskScraperManagerImpl)

    await product_extractor_factory.add_instance(ProductExtractorAuchan)
    await product_extractor_factory.add_instance(ProductExtractorSbermarket)

    add_factory(
        factory_type=ProductRequestFactory,
        factory=product_request_factory
    )

    add_factory(
        factory_type=ProductScraperFactory,
        factory=product_scraper_factory
    )

    add_factory(
        factory_type=TaskScraperManagerFactory,
        factory=task_scraper_manager_factory
    )

    add_factory(
        factory_type=ProductExtractorFactory,
        factory=product_extractor_factory
    )
