from typing import Any
from typing import Mapping

from base.core.extractor import ExtractorProduct
from base.core.extractor import ExtractorProductFactory
from base.settings import SettingsSbermarket
from impl.extractor.sbermarket import ExtractorProductSbermarket

__all__ = ['ExtractorProductSbermarketFactory']


class ExtractorProductSbermarketFactory(
    ExtractorProductFactory
):
    __slots__ = ()

    @property
    def type(self) -> str:
        return 'default'

    async def __call__(
        self,
        settings: Mapping[str, Any]
    ) -> ExtractorProduct:
        settings = SettingsSbermarket(**settings)
        return ExtractorProductSbermarket(
            settings=settings
        )
