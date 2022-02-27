from typing import (
    Any,
    Dict
)

from core.interfaces.extractor.ProductExtractorFactoryStoreFactory import (
    ProductExtractorFactoryStoreFactory
)
from core.interfaces.request.ProductRequestFactoryStoreFactory import (
    ProductRequestFactoryStoreFactory
)
from core.interfaces.scraper.ProductScraperFactoryStoreFactory import (
    ProductScraperFactoryStoreFactory
)
from core.interfaces.tasks_manager.TaskScraperManagerFactoryStoreFactory import (
    TaskScraperManagerFactoryStoreFactory
)
from impl.extractor.ProductExtractorFactoryStoreFactoryImpl import (
    ProductExtractorFactoryStoreFactoryImpl
)
from impl.extractor.factories import ProductExtractorSbermarketFactory
from impl.request.ProductRequestFactoryStoreFactoryImpl import (
    ProductRequestFactoryStoreFactoryImpl
)
from impl.request.factories import ProductRequestPyppeteerFactory
from impl.scraper.ProductScraperFactoryStoreFactoryImpl import (
    ProductScraperFactoryStoreFactoryImpl
)
from impl.scraper.factories import ProductScraperSbermarketFactory
from impl.tasks_scraper_manager.TaskScraperManagerFactoryStoreFactoryImpl import (
    TaskScraperManagerFactoryStoreFactoryImpl
)

__all__ = ['build_app']

from impl.tasks_scraper_manager.factories import TaskScraperManagerBaseFactory


async def build_app(ioc: Dict[Any, Any]) -> None:
    # register TaskScraperManagerFactory
    task_scraper_manager_store = TaskScraperManagerFactoryStoreFactoryImpl()
    await task_scraper_manager_store.add_instance(
        TaskScraperManagerBaseFactory()
    )
    ioc[TaskScraperManagerFactoryStoreFactory] = task_scraper_manager_store

    # register ProductExtractorFactoryStoreFactory
    product_extractor_factory_store = ProductExtractorFactoryStoreFactoryImpl()
    await product_extractor_factory_store.add_instance(
        ProductExtractorSbermarketFactory()
    )
    ioc[ProductExtractorFactoryStoreFactory] = product_extractor_factory_store

    # register ProductRequestFactoryStoreFactory
    product_request_factory_store = ProductRequestFactoryStoreFactoryImpl()
    await product_request_factory_store.add_instance(
        ProductRequestPyppeteerFactory()
    )
    ioc[
        ProductRequestFactoryStoreFactory] = ProductRequestFactoryStoreFactoryImpl()

    # register ProductRequestFactoryStoreFactory
    product_scraper_factory_store = ProductScraperFactoryStoreFactoryImpl()
    await product_scraper_factory_store.add_instance(
        ProductScraperSbermarketFactory()
    )
    ioc[ProductScraperFactoryStoreFactory] = product_scraper_factory_store
