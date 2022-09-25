from typing import Collection

from aiohttp import ClientSession

from base.core.request import RequestProduct

__all__ = ['RequestAiohttp']


class RequestAiohttp(RequestProduct):
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
