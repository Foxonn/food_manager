from core.interfaces.tasks_manager import ScraperTaskManager

__all__ = ['ScraperTaskManagerFactory']


class ScraperTaskManagerFactory:
    async def __call__(self) -> ScraperTaskManager:
        raise NotImplementedError
