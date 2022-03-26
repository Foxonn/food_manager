import pathlib

from galo_ioc import add_factory, get_factory
from yaml import safe_load

from core.interfaces.scraper.ProductScraperFactory import ProductScraperFactory
from core.interfaces.tasks_manager.TaskScraperManager import TaskScraperManager
from core.interfaces.tasks_manager.TaskScraperManagerFactory import TaskScraperManagerFactory
from impl.tasks_scraper_manager.instances import TaskScraperManagerBase

__all__ = [
    "load",
]


async def load() -> None:
    class TaskScraperManagerBaseFactory(TaskScraperManagerFactory):
        async def __call__(self) -> TaskScraperManager:
            return task_scraper_manager

    path_to_config = pathlib.Path(
        pathlib.Path(__file__).parent.resolve(),
        'config.yaml'
    )

    with open(path_to_config) as fp:
        settings = safe_load(fp)

    product_scraper_factory = get_factory(ProductScraperFactory)
    product_scraper = await product_scraper_factory()

    task_scraper_manager = TaskScraperManagerBase(
        settings=settings,
        scraper=product_scraper,
    )

    add_factory(
        TaskScraperManagerFactory,
        TaskScraperManagerBaseFactory()
    )
