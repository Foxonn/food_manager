from typing import Any
from typing import Mapping

from core.interfaces.scraper import ScraperProduct

__all__ = ['ProductScraperFactoryStoreFactory']


class ProductScraperFactoryStoreFactory:
    async def add_instance(self, instance: ScraperProduct) -> None:
        raise NotImplementedError

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> ScraperProduct:
        raise NotImplementedError
