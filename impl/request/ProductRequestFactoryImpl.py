from typing import Dict

from core.interfaces.request.ProductRequest import ProductRequest
from core.interfaces.request.ProductRequestFactory import (
    ProductRequestFactory
)

__all__ = ['ProductRequestFactoryImpl']


class ProductRequestFactoryImpl(ProductRequestFactory):
    __slots__ = (
        "__instances"
    )

    def __init__(self):
        self.__instances: Dict[str, ProductRequest] = {}

    async def add_instance(self, instance: ProductRequest) -> None:
        if instance.type in self.__instances.keys():
            raise KeyError(f"{type(instance)} already register.")

        self.__instances[instance.type] = instance

    async def get_instance(self, type: str) -> ProductRequest:
        try:
            instance = self.__instances[type]
        except KeyError:
            raise KeyError(f"{type} not registered.")
        else:
            return instance
