from typing import Collection

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from core.interfaces.ProductRequest import ProductRequest

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

    async def get(self, url: str) -> None:
        title = "Купить Творог рассыпчатый «Простоквашино» 5%, 320 г (773487) в интернет-магазине АШАН в Москве и России"
        self.__driver.get(url)
        WebDriverWait(self.__driver, 60).until(ec.title_is(title))
