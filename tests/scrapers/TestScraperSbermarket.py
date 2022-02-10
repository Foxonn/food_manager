import pytest
from pyppeteer import launch
from selenium import webdriver

from core.interfaces.ProductExtractor import ProductExtractor
from core.interfaces.ProductRequest import ProductRequest
from core.interfaces.Scraper import Scraper
from impl.extractors import ProductExtractorSbermarket
from impl.requests import (
    ProductRequestPyppeteer,
    ProductRequestSelenium,
)
from impl.scrapers import ScraperSbermarket


@pytest.fixture
@pytest.mark.asyncio
async def product_request_pyppeteer() -> ProductRequest:
    browser = await launch()
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
async def scraper(product_request_pyppeteer: ProductRequest) -> Scraper:
    scraper = ScraperSbermarket(product_request_pyppeteer)
    return scraper


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
        scraper: Scraper,
        extractor: ProductExtractor
    ):
        # url = "https://business.sbermarket.ru/auchan/tvorog-prostokvashino-rassypchatyy-5-320-g-1108399"
        url = "https://business.sbermarket.ru/auchan/golien-pietielinka-s-kozhiei"
        parse_page = await scraper.get_product(url)
        product = await extractor(parse_page)
        print('\n' + '*' * 30)
        print(*[product], sep='\n\r')
        print('*' * 30 + '\n')
