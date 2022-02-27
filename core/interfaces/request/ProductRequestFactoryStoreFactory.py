from typing import (
    Any,
    Mapping
)

from core.interfaces.request.ProductRequest import ProductRequest

__all__ = [
    "ProductRequestFactoryStoreFactory",
]


class ProductRequestFactoryStoreFactory:
    async def add_instance(self, instance: ProductRequest) -> None:
        raise NotImplementedError

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> ProductRequest:
        raise NotImplementedError
