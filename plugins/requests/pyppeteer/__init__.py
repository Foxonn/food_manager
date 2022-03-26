import asyncio
import pathlib

from galo_ioc import add_factory
from pyppeteer import launch
from yaml import safe_load

from core.interfaces.request.RequestProduct import RequestProduct
from core.interfaces.request.RequestProductFactory import RequestProductFactory
from impl.request.instances.RequestProductPyppeteer import RequestProductPyppeteer

__all__ = [
    "load",
]


async def load() -> None:
    class RequestPyppeteerProductFactory(RequestProductFactory):
        async def __call__(self) -> RequestProduct:
            return request_product_pyppeteer

    path_to_config = pathlib.Path(
        pathlib.Path(__file__).parent.resolve(),
        'config.yaml'
    )

    with open(path_to_config) as fp:
        settings = safe_load(fp)

    browser = await launch(options=settings)
    request_product_pyppeteer = RequestProductPyppeteer(browser)

    add_factory(
        RequestProductFactory,
        RequestPyppeteerProductFactory()
    )
