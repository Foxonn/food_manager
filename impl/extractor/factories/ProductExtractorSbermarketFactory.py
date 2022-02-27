from typing import (
    Any,
    Mapping
)

from core.settings import SettingsSbermarket
from core.interfaces.extractor.ProductExtractor import ProductExtractor
from impl.extractor.instances.ProductExtractorSbermarket import (
    ProductExtractorSbermarket
)
from core.interfaces.extractor.ProductExtractorFactory import (
    ProductExtractorFactory
)

__all__ = ['ProductExtractorSbermarketFactory']


class ProductExtractorSbermarketFactory(ProductExtractorFactory):
    @property
    def type(self) -> str:
        return "sbermarket"

    async def get_instance(
        self,
        settings: Mapping[str, Any]
    ) -> ProductExtractor:
        SettingsSbermarket(**settings)
        return ProductExtractorSbermarket(**settings)
