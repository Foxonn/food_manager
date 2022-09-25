from typing import Any
from typing import Mapping

from base.core.extractor import ExtractorProduct
from base.core.extractor import ExtractorProductFactory

__all__ = ['ExtractorProductFactoryStoreFactory']


class ExtractorProductFactoryStoreFactory:
    __slots__ = ()

    async def add_instance(self, instance: ExtractorProductFactory) -> None:
        raise NotImplementedError

    async def get_instance(self, type: str, settings: Mapping[str, Any]) -> ExtractorProduct:
        raise NotImplementedError
