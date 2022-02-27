from typing import (
    Any,
    Mapping
)

from core.interfaces.request.ProductRequest import ProductRequest

__all__ = [
    "ProductRequestFactory",
]


class ProductRequestFactory:
    @property
    def type(self) -> str:
        raise NotImplementedError

    async def get_instance(self, settings: Mapping[str, Any]) -> ProductRequest:
        raise NotImplementedError
