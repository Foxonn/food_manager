from typing import (
    Any,
    Dict,
    Mapping
)

from core.interfaces.request.ProductRequest import ProductRequest
from core.interfaces.request.ProductRequestFactory import ProductRequestFactory
from core.interfaces.request.ProductRequestFactoryStoreFactory import (
    ProductRequestFactoryStoreFactory
)

__all__ = ['ProductRequestFactoryStoreFactoryImpl']


class ProductRequestFactoryStoreFactoryImpl(
    ProductRequestFactoryStoreFactory
):
    __slots__ = (
        "__instances"
    )

    def __init__(self):
        self.__instances: Dict[str, ProductRequestFactory] = {}

    async def add_instance(self, instance: ProductRequestFactory) -> None:
        if instance.type in self.__instances.keys():
            raise KeyError(f"{type(instance)} already register.")

        self.__instances[instance.type] = instance

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> ProductRequest:
        try:
            instance = self.__instances[type]
        except KeyError:
            raise KeyError(f"{type} not registered.")
        else:
            return await instance.get_instance(**settings)
