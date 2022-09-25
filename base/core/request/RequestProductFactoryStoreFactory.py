from typing import Any
from typing import Mapping

from base.core.request import RequestProduct

__all__ = ['RequestProductFactoryStoreFactory']


class RequestProductFactoryStoreFactory:
    __slots__ = ()

    async def add_instance(self, instance: RequestProduct) -> None:
        raise NotImplementedError

    async def get_instance(self, type: str, settings: Mapping[str, Any]) -> RequestProduct:
        raise NotImplementedError
