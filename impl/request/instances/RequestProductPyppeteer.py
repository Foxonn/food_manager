from pyppeteer.browser import Browser

from core.interfaces.request import RequestProduct

__all__ = ['RequestProductPyppeteer']


class RequestProductPyppeteer(RequestProduct):
    __slots__ = (
        "__browser",
    )

    def __init__(
        self,
        browser: Browser
    ) -> None:
        self.__browser = browser

    async def __call__(self, url: str) -> str:
        page = await self.__browser.newPage()
        await page.goto(url)
        content = await page.content()
        await page.close()
        return content
