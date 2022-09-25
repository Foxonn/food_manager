from typing import Any
from typing import Mapping

from base.core.extractor import ExtractorProduct

__all__ = ['ExtractorProductFactory']


class ExtractorProductFactory:
    __slots__ = ()

    @property
    def type(self) -> str:
        raise NotImplementedError

    async def __call__(self, settings: Mapping[str, Any]) -> ExtractorProduct:
        raise NotImplementedError
