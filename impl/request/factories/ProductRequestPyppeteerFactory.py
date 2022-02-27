from typing import (
    Any,
    Mapping,
)

from core.interfaces.request.ProductRequest import ProductRequest
from core.interfaces.request.ProductRequestFactory import ProductRequestFactory
from impl.request.instances import ProductRequestPyppeteer

__all__ = ['ProductRequestPyppeteerFactory']


class ProductRequestPyppeteerFactory(ProductRequestFactory):
    @property
    def type(self) -> str:
        return "pyppeteer"

    async def get_instance(
        self,
        settings: Mapping[str, Any]
    ) -> ProductRequest:
        return ProductRequestPyppeteer(
            **settings
        )
