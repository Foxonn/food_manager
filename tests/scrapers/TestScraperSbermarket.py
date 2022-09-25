import pytest
from pyppeteer import launch
from selenium import webdriver

from base.core.extractor import ExtractorProduct
from base.core.request import RequestProduct
from base.core.scraper import ScraperProduct
from base.core.tasks_manager import TaskManagerScraper
from impl.extractor.sbermarket import ExtractorProductSbermarket
from impl.request.instances import RequestProductPyppeteer
from impl.request.instances import RequestProductSelenium
from impl.scraper.instances import ScraperProductSbermarket
from impl.tasks_scraper_manager.instances import TaskManagerScraperBase


@pytest.fixture
@pytest.mark.asyncio
async def product_request_pyppeteer() -> RequestProduct:
    browser = await launch(
        options={
            'headless': False
        }
    )
    request = RequestProductPyppeteer(browser)
    yield request
    await browser.close()


@pytest.fixture
@pytest.mark.asyncio
async def product_request_selenium_chrome() -> RequestProduct:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(
        r'D:\Development\food_manager\source\chromedriver_98_0_4758_80.exe',
        options=chrome_options
    )

    try:
        request = RequestProductSelenium(browser)
    except Exception:
        raise
    else:
        yield request
    finally:
        browser.close()


@pytest.fixture
@pytest.mark.asyncio
async def scraper(
    product_request_pyppeteer: RequestProduct
) -> ScraperProduct:
    scraper = ScraperProductSbermarket(product_request_pyppeteer)
    return scraper


@pytest.fixture
@pytest.mark.asyncio
async def task_scraper_manager(
    scraper: ScraperProduct
) -> TaskManagerScraper:
    tasks_manager = TaskManagerScraperBase(
        scraper=scraper,
        settings={
            "batch_urls": 2,
            "waits_evaluate_batch_tasks": 60,
            "timeout_loop": 3,
        }
    )
    tasks_manager.initialize()
    return tasks_manager


@pytest.fixture
@pytest.mark.asyncio
async def extractor() -> ExtractorProduct:
    settings = {
        "selector_name": "h1[itemprop=name]",
        "selector_price": "meta[itemprop=price]",
        "selector_weight": "div[itemprop='offers'] p",
        "selector_nutrition_name": ".nutrition .product-properties .product-property__name",
        "selector_nutrition_value": ".nutrition .product-properties .product-property__value",
    }
    extractor = ExtractorProductSbermarket(settings)
    return extractor


class TestScraperSbermarket:
    @pytest.mark.asyncio
    async def test_get_product(
        self,
        extractor: ExtractorProduct,
        task_scraper_manager: TaskManagerScraper,
    ):
        def callback(html_page: str) -> None:
            product = extractor(html_page)

            print('\n' + '*' * 30)
            print(*[product], sep='\n\r')
            print('*' * 30 + '\n')

        task_scraper_manager.set_callable_command(callback)
        await task_scraper_manager.parse_page(
            [
                "https://sbermarket.ru/auchan/golien-pietielinka-s-kozhiei",
                "https://sbermarket.ru/auchan/ponchiki-auchan-s-varenoy-sguschenkoy-85-g-h-4-sht",
                "https://sbermarket.ru/auchan/moloko-luzhaykino-pasterizovannoe-2-5-900-ml",
                "https://sbermarket.ru/auchan/smetana-luzinskoe-moloko-termostatnaya-10-350-g"
            ]
        )
        await task_scraper_manager.deinitialize()

        # product = await extractor(parse_page)
        # print('\n' + '*' * 30)
        # print(*[product], sep='\n\r')
        # print('*' * 30 + '\n')
