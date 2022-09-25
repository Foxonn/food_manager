from typing import Any
from typing import Dict
from typing import Mapping

from core.interfaces.tasks_manager import ScraperTaskManager
from core.interfaces.tasks_manager import ScraperTaskManagerFactory
from core.interfaces.tasks_manager import ScraperTaskManagerFactoryStoreFactory

__all__ = ['ScraperTaskManagerFactoryStoreFactoryImpl']


class ScraperTaskManagerFactoryStoreFactoryImpl(
    ScraperTaskManagerFactoryStoreFactory
):
    __slots__ = (
        "__instances"
    )

    def __init__(self):
        self.__instances: Dict[str, ScraperTaskManagerFactory] = {}

    async def add_instance(self, instance: ScraperTaskManagerFactory) -> None:
        if instance.type in self.__instances.keys():
            raise KeyError(f"{type(instance)} already register.")

        self.__instances[instance.type] = instance

    async def get_instance(
        self,
        type: str,
        settings: Mapping[str, Any]
    ) -> ScraperTaskManager:
        try:
            instance = self.__instances[type]
        except KeyError:
            raise KeyError(f"{type} not registered.")
        else:
            return await instance.get_instance(**settings)
