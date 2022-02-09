from aiohttp import ClientSession

from core.interfaces.ProductRequest import ProductRequest

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

    async def get(self, url: str) -> str:
        async with self.__session.get(url) as response:
            response.raise_for_status()
            return await response.text()
