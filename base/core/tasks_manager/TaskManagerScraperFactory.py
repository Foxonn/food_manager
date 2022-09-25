from base.core.tasks_manager import TaskManagerScraper

__all__ = ['TaskManagerScraperFactory']


class TaskManagerScraperFactory:
    __slots__ = ()

    async def __call__(self) -> TaskManagerScraper:
        raise NotImplementedError
