from typing import (
    Any,
    Dict,
    Mapping
)

from core.interfaces.extractor.ProductExtractor import ProductExtractor
from core.interfaces.extractor.ProductExtractorFactory import (
    ProductExtractorFactory
)
from core.interfaces.extractor.ProductExtractorFactoryStoreFactory import (
    ProductExtractorFactoryStoreFactory
)

__all__ = ['ProductExtractorFactoryStoreFactoryImpl']


class ProductExtractorFactoryStoreFactoryImpl(
    ProductExtractorFactoryStoreFactory
):
    __slots__ = (
        "__instances"
    )

    def __init__(self):
        self.__instances: Dict[str, ProductExtractorFactory] = {}

    async def add_instance(self, instance: ProductExtractorFactory) -> None:
        if instance.type in self.__instances.keys():
            raise KeyError(f"{type(instance)} already register.")

        self.__instances[instance.type] = instance

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> ProductExtractor:
        try:
            instance = self.__instances[type]
        except KeyError:
            raise KeyError(f"{type} not registered.")
        else:
            return await instance.get_instance(**settings)
