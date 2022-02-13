__all__ = [
    "TaskScraperManager",
]


class TaskScraperManager:
    __slots__ = ()

    async def add_task(self, url: str) -> None:
        raise NotImplementedError

    def initialize(self) -> None:
        raise NotImplementedError

    async def deinitialize(self) -> None:
        raise NotImplementedError
