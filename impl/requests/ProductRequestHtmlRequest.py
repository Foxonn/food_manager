from requests_html import AsyncHTMLSession

from core.interfaces.ProductRequest import ProductRequest

__all__ = [
    "ProductRequestHtmlRequest",
]


class ProductRequestHtmlRequest(ProductRequest):
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

    async def get(self, url: str) -> str:
        _self = self

        async def _get():
            _self.__session.get(url)

        response = await self.__session.run(_get)
        response.raise_for_status()
        print('*' * 30)
        print(*[response.text], sep='\n\r')
        print('*' * 30)
