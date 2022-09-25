from typing import Any
from typing import Mapping

from core.interfaces.extractor import ExtractorProduct
from core.interfaces.extractor import ExtractorProductFactory

__all__ = ['ExtractorProductFactoryStoreFactory']


class ExtractorProductFactoryStoreFactory:
    async def add_instance(self, instance: ExtractorProductFactory) -> None:
        raise NotImplementedError

    async def get_instance(self, type: str, settings: Mapping[str, Any]) -> ExtractorProduct:
        raise NotImplementedError
