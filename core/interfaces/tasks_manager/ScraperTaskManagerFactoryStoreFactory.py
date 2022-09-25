from typing import Any
from typing import Mapping

from core.interfaces.tasks_manager import ScraperTaskManager
from core.interfaces.tasks_manager import ScraperTaskManagerFactory

__all__ = ['ScraperTaskManagerFactoryStoreFactory']


class ScraperTaskManagerFactoryStoreFactory:
    async def add_instance(self, instance: ScraperTaskManagerFactory) -> None:
        raise NotImplementedError

    async def get_instance(self, type: str, settings: Mapping[str, Any]) -> ScraperTaskManager:
        raise NotImplementedError
