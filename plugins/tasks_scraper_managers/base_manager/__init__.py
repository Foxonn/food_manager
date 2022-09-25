import pathlib

from galo_ioc import add_factory
from galo_ioc import get_factory
from yaml import safe_load

from base.core.scraper import ScraperProductFactory
from base.core.tasks_manager import TaskManagerScraper
from base.core.tasks_manager import TaskManagerScraperFactory
from impl.tasks_scraper_manager.instances import TaskManagerScraperBase

__all__ = ['load']


async def load() -> None:
    class ScraperTaskManagerBaseFactory(TaskManagerScraperFactory):
        async def __call__(self) -> TaskManagerScraper:
            return task_scraper_manager

    path_to_config = pathlib.Path(
        pathlib.Path(__file__).parent.resolve(),
        'config.yaml'
    )
    settings = safe_load(path_to_config.read_text())

    product_scraper_factory = get_factory(ScraperProductFactory)
    product_scraper = await product_scraper_factory()

    task_scraper_manager = TaskManagerScraperBase(
        settings=settings,
        scraper=product_scraper,
    )

    add_factory(
        TaskManagerScraperFactory,
        ScraperTaskManagerBaseFactory()
    )
