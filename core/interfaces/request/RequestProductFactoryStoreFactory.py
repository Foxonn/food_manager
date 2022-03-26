from typing import (
    Any,
    Mapping
)

from core.interfaces.request.RequestProduct import RequestProduct

__all__ = [
    "RequestProductFactoryStoreFactory",
]


class RequestProductFactoryStoreFactory:
    async def add_instance(self, instance: RequestProduct) -> None:
        raise NotImplementedError

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> RequestProduct:
        raise NotImplementedError
