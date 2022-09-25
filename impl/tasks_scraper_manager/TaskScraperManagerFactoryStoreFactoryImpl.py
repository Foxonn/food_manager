from typing import Any
from typing import Dict
from typing import Mapping

from base.core.tasks_manager import TaskManagerScraper
from base.core.tasks_manager import TaskManagerScraperFactory
from base.core.tasks_manager import TaskManagerScraperFactoryStoreFactory

__all__ = ['ScraperTaskManagerFactoryStoreFactoryImpl']


class ScraperTaskManagerFactoryStoreFactoryImpl(
    TaskManagerScraperFactoryStoreFactory
):
    __slots__ = (
        "__instances"
    )

    def __init__(self):
        self.__instances: Dict[str, TaskManagerScraperFactory] = {}

    async def add_instance(self, instance: TaskManagerScraperFactory) -> None:
        if instance.type in self.__instances.keys():
            raise KeyError(f"{type(instance)} already register.")

        self.__instances[instance.type] = instance

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> TaskManagerScraper:
        try:
            instance = self.__instances[type]
        except KeyError:
            raise KeyError(f"{type} not registered.")
        else:
            return await instance.get_instance(**settings)
