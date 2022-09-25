from typing import Any
from typing import Mapping

from base.core.scraper import ScraperProduct

__all__ = ['ScraperProductFactoryStoreFactory']


class ScraperProductFactoryStoreFactory:
    __slots__ = ()

    async def add_instance(self, instance: ScraperProduct) -> None:
        raise NotImplementedError

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> ScraperProduct:
        raise NotImplementedError
