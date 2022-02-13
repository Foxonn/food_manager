from time import sleep
from uuid import uuid4

import pytest
from pyppeteer import launch
from selenium import webdriver

from core.interfaces.ProductExtractor import ProductExtractor
from core.interfaces.ProductRequest import ProductRequest
from core.interfaces.Scraper import Scraper
from core.interfaces.TaskScraperManager import TaskScraperManager
from impl.extractors import ProductExtractorSbermarket
from impl.requests import (
    ProductRequestPyppeteer,
    ProductRequestSelenium,
)
from impl.scrapers import ScraperSbermarket
from impl.tasks_scraper_manager import TaskScraperManagerImpl


@pytest.fixture
@pytest.mark.asyncio
async def product_request_pyppeteer() -> ProductRequest:
    browser = await launch(
        options={
            'headless': False
        }
    )
    request = ProductRequestPyppeteer(browser)
    yield request
    await browser.close()


@pytest.fixture
@pytest.mark.asyncio
async def product_request_selenium_chrome() -> ProductRequest:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(
        r'D:\Development\food_manager\source\chromedriver_98_0_4758_80.exe',
        options=chrome_options
    )

    try:
        request = ProductRequestSelenium(browser)
    except Exception:
        raise
    else:
        yield request
    finally:
        browser.close()


@pytest.fixture
@pytest.mark.asyncio
async def scraper(product_request_pyppeteer: ProductRequest) -> Scraper:
    scraper = ScraperSbermarket(product_request_pyppeteer)
    return scraper


@pytest.fixture
@pytest.mark.asyncio
async def tasks_manager(scraper: Scraper) -> TaskScraperManager:
    tasks_manager = TaskScraperManagerImpl(scraper)
    tasks_manager.initialize()
    return tasks_manager


@pytest.fixture
@pytest.mark.asyncio
async def extractor() -> ProductExtractor:
    settings = {
        "selector_name": "h1[itemprop=name]",
        "selector_price": "meta[itemprop=price]",
        "selector_weight": "div[itemprop='offers'] p",
        "selector_nutrition_name": ".nutrition .product-properties .product-property__name",
        "selector_nutrition_value": ".nutrition .product-properties .product-property__value",
    }
    extractor = ProductExtractorSbermarket(settings)
    return extractor


class TestScraperSbermarket:
    @pytest.mark.asyncio
    async def test_get_product(
        self,
        extractor: ProductExtractor,
        tasks_manager: TaskScraperManager,
    ):
        await tasks_manager.add_tasks(
            [
                "https://business.sbermarket.ru/auchan/golien-pietielinka-s-kozhiei",
                "https://business.sbermarket.ru/auchan/grudka-indeyki-file-pava-pava-premium-ohlazhdennaya-600-g",
                "https://business.sbermarket.ru/auchan/file-bedra-tsyplenka-rokoko-ohlazhdennoe-750-g",
                "https://business.sbermarket.ru/auchan/okorochok-tsyplenka-broylera-s-kozhey-kazhdyy-den-ohlazhdennyy-700-g"
            ]
        )
        await tasks_manager.deinitialize()

        # product = await extractor(parse_page)
        # print('\n' + '*' * 30)
        # print(*[product], sep='\n\r')
        # print('*' * 30 + '\n')
