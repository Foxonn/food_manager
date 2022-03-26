from typing import (
    Any,
    Mapping,
)

from core.interfaces.extractor.ExtractorProduct import ExtractorProduct
from core.interfaces.extractor.ExtractorProductFactory import (
    ExtractorProductFactory
)

__all__ = [
    "ExtractorProductFactoryStoreFactory",
]


class ExtractorProductFactoryStoreFactory:
    async def add_instance(self, instance: ExtractorProductFactory) -> None:
        raise NotImplementedError

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> ExtractorProduct:
        raise NotImplementedError
