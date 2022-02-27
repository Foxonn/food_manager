from core.interfaces.tasks_manager.TaskScraperManager import TaskScraperManager

__all__ = [
    "TaskScraperManagerFactoryStoreFactory",
]


class TaskScraperManagerFactoryStoreFactory:
    async def add_instance(self, instance: TaskScraperManager) -> None:
        raise NotImplementedError

    async def get_instance(self, type: str) -> TaskScraperManager:
        raise NotImplementedError
