from typing import Collection

from aiohttp import ClientSession

from core.interfaces.request.ProductRequest import ProductRequest

__all__ = [
    "ProductRequestAiohttp",
]


class ProductRequestAiohttp(ProductRequest):
    __slots__ = (
        "__session",
    )

    def __init__(
        self,
        session: ClientSession
    ) -> None:
        self.__session = session

    @property
    def type(self) -> str:
        return "aiohttp"

    async def __call__(self, url: str) -> Collection:
        pass
