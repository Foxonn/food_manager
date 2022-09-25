import pathlib

from galo_ioc import add_factory
from galo_ioc import get_factory
from yaml import safe_load

from core.interfaces.scraper import ProductScraperFactory
from core.interfaces.tasks_manager import ScraperTaskManager
from core.interfaces.tasks_manager import ScraperTaskManagerFactory
from impl.tasks_scraper_manager.instances import ScraperTaskManagerBase

__all__ = ['load']


async def load() -> None:
    class ScraperTaskManagerBaseFactory(ScraperTaskManagerFactory):
        async def __call__(self) -> ScraperTaskManager:
            return task_scraper_manager

    path_to_config = pathlib.Path(
        pathlib.Path(__file__).parent.resolve(),
        'config.yaml'
    )
    settings = safe_load(path_to_config.read_text())

    product_scraper_factory = get_factory(ProductScraperFactory)
    product_scraper = await product_scraper_factory()

    task_scraper_manager = ScraperTaskManagerBase(
        settings=settings,
        scraper=product_scraper,
    )

    add_factory(
        ScraperTaskManagerFactory,
        ScraperTaskManagerBaseFactory()
    )
