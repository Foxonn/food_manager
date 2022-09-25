from galo_ioc import FactoryContainerImpl
from galo_ioc import get_factory

from core.interfaces.extractor import ExtractorProductFactory
from core.interfaces.tasks_manager import ScraperTaskManagerFactory
from utils.startup_utils import get_module_names_path
from utils.startup_utils import load_plugins
from utils.startup_utils import read_module_names

__all__ = ['build_app']


async def build_app() -> None:
    module_names_path = get_module_names_path()
    module_names = read_module_names(module_names_path)

    with FactoryContainerImpl():
        await load_plugins(module_names)
        extractor_factory = get_factory(ExtractorProductFactory)
        task_scraper_manager_factory = get_factory(ScraperTaskManagerFactory)

        extractor = await extractor_factory()
        task_scraper_manager = await task_scraper_manager_factory()
