from typing import Any
from typing import Mapping

from base.core.extractor import ExtractorProduct
from base.core.extractor import ExtractorProductFactory
from base.core.extractor import ExtractorProductFactoryStore
from base.core.extractor import ExtractorProductFactoryStoreFactory

__all__ = ['ExtractorProductFactoryStoreFactoryImpl']

_instances_factories = ExtractorProductFactoryStore()


class ExtractorProductFactoryStoreFactoryImpl(
    ExtractorProductFactoryStoreFactory
):
    __slots__ = (
        '__instances_factories',
    )

    async def add_instance(
        self,
        instance: ExtractorProductFactory
    ) -> None:
        _instances_factories[instance] = instance

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> ExtractorProduct:
        extractor_product_factory = _instances_factories[type]
        return await extractor_product_factory(
            settings=settings
        )
