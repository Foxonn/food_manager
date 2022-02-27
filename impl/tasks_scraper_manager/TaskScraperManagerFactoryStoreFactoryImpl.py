from typing import (
    Any,
    Dict,
    Mapping
)

from core.interfaces.tasks_manager.TaskScraperManager import TaskScraperManager
from core.interfaces.tasks_manager.TaskScraperManagerFactory import (
    TaskScraperManagerFactory
)
from core.interfaces.tasks_manager.TaskScraperManagerFactoryStoreFactory import (
    TaskScraperManagerFactoryStoreFactory
)

__all__ = ['TaskScraperManagerFactoryStoreFactoryImpl']


class TaskScraperManagerFactoryStoreFactoryImpl(
    TaskScraperManagerFactoryStoreFactory
):
    __slots__ = (
        "__instances"
    )

    def __init__(self):
        self.__instances: Dict[str, TaskScraperManagerFactory] = {}

    async def add_instance(self, instance: TaskScraperManagerFactory) -> None:
        if instance.type in self.__instances.keys():
            raise KeyError(f"{type(instance)} already register.")

        self.__instances[instance.type] = instance

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> TaskScraperManager:
        try:
            instance = self.__instances[type]
        except KeyError:
            raise KeyError(f"{type} not registered.")
        else:
            return await instance.get_instance(**settings)
