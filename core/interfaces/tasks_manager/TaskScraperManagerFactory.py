from typing import (
    Any,
    Mapping
)

from core.interfaces.tasks_manager.TaskScraperManager import TaskScraperManager

__all__ = [
    "TaskScraperManagerFactory",
]


class TaskScraperManagerFactory:
    @property
    def type(self) -> str:
        raise NotImplementedError

    async def get_instance(self, settings: Mapping[str, Any]) -> TaskScraperManager:
        raise NotImplementedError
