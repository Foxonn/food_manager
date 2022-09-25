from typing import Any
from typing import Mapping

from base.core.tasks_manager import TaskManagerScraper
from base.core.tasks_manager import TaskManagerScraperFactory

__all__ = ['TaskManagerScraperFactoryStoreFactory']


class TaskManagerScraperFactoryStoreFactory:
    __slots__ = ()

    async def add_instance(self, instance: TaskManagerScraperFactory) -> None:
        raise NotImplementedError

    async def get_instance(self, type: str, settings: Mapping[str, Any]) -> TaskManagerScraper:
        raise NotImplementedError
