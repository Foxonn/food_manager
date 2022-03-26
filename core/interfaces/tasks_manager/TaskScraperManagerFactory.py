from core.interfaces.tasks_manager.TaskScraperManager import TaskScraperManager

__all__ = [
    "TaskScraperManagerFactory",
]


class TaskScraperManagerFactory:
    async def __call__(self) -> TaskScraperManager:
        raise NotImplementedError
