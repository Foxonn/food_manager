from typing import (
    Any,
    Dict,
    Mapping
)

from core.interfaces.scraper.ProductScraper import ProductScraper
from core.interfaces.scraper.ProductScraperFactory import ProductScraperFactory
from core.interfaces.scraper.ProductScraperFactoryStoreFactory import (
    ProductScraperFactoryStoreFactory
)

__all__ = ['ProductScraperFactoryStoreFactoryImpl']


class ProductScraperFactoryStoreFactoryImpl(
    ProductScraperFactoryStoreFactory
):
    __slots__ = (
        "__instances"
    )

    def __init__(self):
        self.__instances: Dict[str, ProductScraperFactory] = {}

    async def add_instance(self, instance: ProductScraperFactory) -> None:
        if instance.type in self.__instances.keys():
            raise KeyError(f"{type(instance)} already register.")

        self.__instances[instance.type] = instance

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> ProductScraper:
        try:
            instance = self.__instances[type]
        except KeyError:
            raise KeyError(f"{type} not registered.")
        else:
            return await instance.get_instance(**settings)
