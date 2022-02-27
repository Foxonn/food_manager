from typing import Any, Mapping

from core.settings import SettingsTaskScraperBaseManager
from core.interfaces.tasks_manager.TaskScraperManager import TaskScraperManager
from core.interfaces.tasks_manager.TaskScraperManagerFactory import (
    TaskScraperManagerFactory
)
from impl.tasks_scraper_manager.instances import TaskScraperManagerBase

__all__ = ['TaskScraperManagerBaseFactory']


class TaskScraperManagerBaseFactory(TaskScraperManagerFactory):
    @property
    def type(self) -> str:
        return "base"

    async def get_instance(
        self,
        settings: Mapping[str, Any]
    ) -> TaskScraperManager:
        SettingsTaskScraperBaseManager(**settings)
        return TaskScraperManagerBase(**settings)
