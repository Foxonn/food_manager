from pyppeteer.browser import Browser

from core.interfaces.ProductRequest import ProductRequest

__all__ = [
    "ProductRequestPyppeteer",
]


class ProductRequestPyppeteer(ProductRequest):
    __slots__ = (
        "__browser",
    )

    def __init__(
        self,
        browser: Browser
    ) -> None:
        self.__browser = browser

    @property
    def type(self) -> str:
        return "pyppeteer"

    async def __call__(self, url: str) -> str:
        page = await self.__browser.newPage()
        await page.goto(url)
        content = await page.content()
        await page.close()
        return content
