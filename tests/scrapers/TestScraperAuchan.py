import pytest
from pyppeteer import launch
from selenium import webdriver

from core.interfaces.ProductExtractor import ProductExtractor
from core.interfaces.ProductRequest import ProductRequest
from core.interfaces.Scraper import Scraper
from impl.extractors import ProductExtractorAuchan
from impl.requests import (
    ProductRequestPyppeteer,
    ProductRequestSelenium,
)
from impl.scrapers import ScraperAuchan


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
    request = ProductRequestSelenium(browser)
    yield request
    browser.close()


@pytest.fixture
@pytest.mark.asyncio
async def scraper(product_request_selenium_chrome: ProductRequest) -> Scraper:
    scraper = ScraperAuchan(product_request_selenium_chrome)
    return scraper


@pytest.fixture
@pytest.mark.asyncio
async def extractor() -> ProductExtractor:
    extractor = ProductExtractorAuchan()
    return extractor


class TestScraperAuchan:
    @pytest.mark.asyncio
    async def test_get_product(
        self,
        scraper: Scraper,
        extractor: ProductExtractor
    ):
        url = "https://business.sbermarket.ru/auchan/tvorog-prostokvashino-rassypchatyy-5-320-g-1108399"
        parse_page = await scraper.get_product(url)
        # data_product = await extractor.extract_product_info(parse_page)
        # print('*'*30)
        # print(*[data_product], sep='\n\r')
        # print('*'*30)
