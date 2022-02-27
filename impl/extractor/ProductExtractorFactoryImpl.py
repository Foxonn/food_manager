from typing import Dict

from core.interfaces.extractor.ProductExtractor import ProductExtractor
from core.interfaces.extractor.ProductExtractorFactory import (
    ProductExtractorFactory
)

__all__ = ['ProductExtractorFactoryImpl']


class ProductExtractorFactoryImpl(ProductExtractorFactory):
    __slots__ = (
        "__instances"
    )

    def __init__(self):
        self.__instances: Dict[str, ProductExtractor] = {}

    async def add_instance(self, instance: ProductExtractor) -> None:
        if instance.type in self.__instances.keys():
            raise KeyError(f"{type(instance)} already register.")

        self.__instances[instance.type] = instance

    async def get_instance(self, type: str) -> ProductExtractor:
        try:
            instance = self.__instances[type]
        except KeyError:
            raise KeyError(f"{type} not registered.")
        else:
            return instance
