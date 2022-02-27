from typing import (
    Collection,
    Callable,
)

__all__ = [
    "TaskScraperManager",
]


class TaskScraperManager:
    __slots__ = ()

    def set_callable_command(self, callback: Callable[[str], None]) -> None:
        raise NotImplementedError

    async def parse_page(self, urls: Collection) -> None:
        raise NotImplementedError

    def initialize(self) -> None:
        raise NotImplementedError

    async def deinitialize(self) -> None:
        raise NotImplementedError
