from typing import Collection

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from core.interfaces.request.ProductRequest import ProductRequest

__all__ = [
    "ProductRequestSelenium",
]


class ProductRequestSelenium(ProductRequest):
    __slots__ = (
        "__driver",
    )

    @property
    def type(self) -> str:
        return "selenium"

    def __init__(self, driver: webdriver.Chrome) -> None:
        self.__driver = driver

    async def __call__(self, url: str) -> Collection:
        pass
