from typing import (
    Any,
    Mapping,
)

from core.interfaces.extractor.ProductExtractor import ProductExtractor
from core.interfaces.extractor.ProductExtractorFactory import (
    ProductExtractorFactory
)

__all__ = [
    "ProductExtractorFactoryStoreFactory",
]


class ProductExtractorFactoryStoreFactory:
    async def add_instance(self, instance: ProductExtractorFactory) -> None:
        raise NotImplementedError

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> ProductExtractor:
        raise NotImplementedError
