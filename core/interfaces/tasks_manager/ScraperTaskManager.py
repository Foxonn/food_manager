from typing import Callable
from typing import Collection

__all__ = ['ScraperTaskManager']


class ScraperTaskManager:
    __slots__ = ()

    @property
    def type(self) -> str:
        raise NotImplementedError

    def set_callable_command(self, callback: Callable[[str], None]) -> None:
        raise NotImplementedError

    async def parse_page(self, urls: Collection) -> None:
        raise NotImplementedError

    def initialize(self) -> None:
        raise NotImplementedError

    async def deinitialize(self) -> None:
        raise NotImplementedError
