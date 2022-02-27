from typing import (
    Any,
    Mapping
)

from core.interfaces.extractor.ProductExtractor import ProductExtractor

__all__ = [
    "ProductExtractorFactoryStoreFactory",
]


class ProductExtractorFactoryStoreFactory:
    async def add_instance(self, instance: ProductExtractor) -> None:
        raise NotImplementedError

    async def get_instance(self, settings: Mapping[str, Any]) -> ProductExtractor:
        raise NotImplementedError
