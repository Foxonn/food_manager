from typing import (
    Any,
    Mapping
)

from core.interfaces.extractor.ProductExtractor import ProductExtractor

__all__ = [
    "ProductExtractorFactory",
]


class ProductExtractorFactory:
    @property
    def type(self) -> str:
        raise NotImplementedError

    async def get_instance(
        self,
        settings: Mapping[str, Any]
    ) -> ProductExtractor:
        raise NotImplementedError
