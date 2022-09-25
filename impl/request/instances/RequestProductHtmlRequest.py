from typing import Collection

from requests_html import AsyncHTMLSession

from base.core.request import RequestProduct

__all__ = ['RequestProductHtmlRequest']


class RequestProductHtmlRequest(RequestProduct):
    __slots__ = (
        "__session",
    )

    def __init__(
        self,
        session: AsyncHTMLSession
    ) -> None:
        self.__session = session

    @property
    def type(self) -> str:
        return "html_request"

    async def __call__(self, url: str) -> Collection:
        pass
