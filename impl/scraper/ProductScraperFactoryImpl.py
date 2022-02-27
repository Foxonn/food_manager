from typing import Dict

from core.interfaces.scraper.ProductScraperFactory import ProductScraperFactory
from core.interfaces.scraper.ProductScraper import ProductScraper

__all__ = ['ProductScraperFactoryImpl']


class ProductScraperFactoryImpl(ProductScraperFactory):
    __slots__ = (
        "__instances"
    )

    def __init__(self):
        self.__instances: Dict[str, ProductScraper] = {}

    async def add_instance(self, instance: ProductScraper) -> None:
        if instance.type in self.__instances.keys():
            raise KeyError(f"{type(instance)} already register.")

        self.__instances[instance.type] = instance

    async def get_instance(self, type: str) -> ProductScraper:
        try:
            instance = self.__instances[type]
        except KeyError:
            raise KeyError(f"{type} not registered.")
        else:
            return instance
