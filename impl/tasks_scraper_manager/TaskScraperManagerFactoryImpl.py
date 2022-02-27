from typing import Dict

from core.interfaces.tasks_manager.TaskScraperManager import TaskScraperManager
from core.interfaces.tasks_manager.TaskScraperManagerFactory import (
    TaskScraperManagerFactory
)

__all__ = ['TaskScraperManagerFactoryImpl']


class TaskScraperManagerFactoryImpl(TaskScraperManagerFactory):
    __slots__ = (
        "__instances"
    )

    def __init__(self):
        self.__instances: Dict[str, TaskScraperManager] = {}

    async def add_instance(self, instance: TaskScraperManager) -> None:
        if instance.type in self.__instances.keys():
            raise KeyError(f"{type(instance)} already register.")

        self.__instances[instance.type] = instance

    async def get_instance(self, type: str) -> TaskScraperManager:
        try:
            instance = self.__instances[type]
        except KeyError:
            raise KeyError(f"{type} not registered.")
        else:
            return instance
