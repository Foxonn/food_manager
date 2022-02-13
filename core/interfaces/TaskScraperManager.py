from typing import Collection

__all__ = [
    "TaskScraperManager",
]


class TaskScraperManager:
    __slots__ = ()

    async def add_tasks(self, urls: Collection) -> None:
        raise NotImplementedError

    def initialize(self) -> None:
        raise NotImplementedError

    async def deinitialize(self) -> None:
        raise NotImplementedError
