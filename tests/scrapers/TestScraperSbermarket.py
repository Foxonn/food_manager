import pytest
from pyppeteer import launch
from selenium import webdriver

from core.interfaces import (
    ProductExtractor,
    ProductRequest,
    Scraper,
    TaskScraperManager,
)
from impl.extractors import ProductExtractorSbermarket
from impl.requests import (
    ProductRequestPyppeteer,
    ProductRequestSelenium,
)
from impl.scrapers import ScraperSbermarket
from impl.tasks_scraper_manager import (
    TaskScraperManagerImpl,
    TaskScraperManagerImpl2
)


@pytest.fixture
@pytest.mark.asyncio
async def product_request_pyppeteer() -> ProductRequest:
    browser = await launch(
        options={'headless': False}
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
async def task_scraper_manager(scraper: Scraper) -> TaskScraperManager:
    tasks_manager = TaskScraperManagerImpl(
        scraper=scraper,
        settings={
            "batch_urls": 3,
            "waits_evaluate_batch_tasks": 60,
            "timeout_loop": 3,
        }
    )
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
        task_scraper_manager: TaskScraperManager,
    ):

        def callback(html_page: str) -> None:
            product = extractor(html_page)

            print('\n' + '*'*30)
            print(*[product], sep='\n\r')
            print('*'*30 + '\n')

        task_scraper_manager.set_callable_command(callback)
        await task_scraper_manager.parse_page([
            "https://sbermarket.ru/auchan/golien-pietielinka-s-kozhiei",
            "https://sbermarket.ru/auchan/ponchiki-auchan-s-varenoy-sguschenkoy-85-g-h-4-sht",
            "https://sbermarket.ru/auchan/moloko-luzhaykino-pasterizovannoe-2-5-900-ml",
            "https://sbermarket.ru/auchan/smetana-luzinskoe-moloko-termostatnaya-10-350-g"
        ])
        await task_scraper_manager.deinitialize()

        # product = await extractor(parse_page)
        # print('\n' + '*' * 30)
        # print(*[product], sep='\n\r')
        # print('*' * 30 + '\n')
