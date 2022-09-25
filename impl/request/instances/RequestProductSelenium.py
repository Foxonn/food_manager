from typing import Collection

from selenium import webdriver

from core.interfaces.request import RequestProduct

__all__ = ['RequestProductSelenium']


class RequestProductSelenium(RequestProduct):
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
