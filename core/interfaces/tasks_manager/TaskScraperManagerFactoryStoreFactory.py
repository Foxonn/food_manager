from typing import (
    Any,
    Mapping
)

from core.interfaces.tasks_manager.TaskScraperManager import TaskScraperManager
from core.interfaces.tasks_manager.TaskScraperManagerFactory import (
    TaskScraperManagerFactory
)

__all__ = [
    "TaskScraperManagerFactoryStoreFactory",
]


class TaskScraperManagerFactoryStoreFactory:
    async def add_instance(self, instance: TaskScraperManagerFactory) -> None:
        raise NotImplementedError

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> TaskScraperManager:
        raise NotImplementedError
