import asyncio
from asyncio import (
    Future,
    Task,
    sleep,
)
from functools import partial
from itertools import zip_longest
from typing import (Any, Callable, Dict, List, Optional, Coroutine)
from uuid import UUID, uuid4

from core.interfaces.Scraper import Scraper
from core.interfaces.TaskScraperManager import TaskScraperManager
from core.settings import SettingsTaskScraperManager

__all__ = [
    "TaskScraperManagerImpl2",
]


class TaskScraperManagerImpl2(TaskScraperManager):
    __slots__ = (
        "__background_task",
        "__futures",
        "__scraper",
        "__settings",
        "__callback",
    )

    def __init__(
        self,
        settings: Dict[str, Any],
        scraper: Scraper,
    ) -> None:
        self.__settings = SettingsTaskScraperManager(**settings)
        self.__scraper = scraper
        self.__callback: Optional[Callable[[str], str]] = None
        self.__futures: Optional[Dict[str, (str, Future)]] = {}
        self.__background_task: Optional[Task] = None

    def set_callable_command(self, callback: Coroutine[Any, Any, None]) -> None:
        self.__callback = callback

    async def parse_page(self, urls: List[str]) -> None:
        if self.__callback is None:
            raise ValueError("Need set callable function!")

        for url in urls:
            future: Future = Future()
            id: UUID = uuid4()
            self.__futures[str(id)] = (url, future)

    async def __request(self, url: str) -> None:
        await self.__scraper(url)

    async def __background_worker(self):
        while True:
            if self.__futures:
                for group in self.__futures.copy():
                    tasks = []
                    for item in group.items():
                        id, value = item
                        url, future = value
                        task = asyncio.create_task(self.__scraper(url))
                        task.add_done_callback(
                            partial(
                                self.__callback_task,
                                future=future,
                                task=task,
                                id=id,
                            )
                        )
                        tasks.append(task)
                    await asyncio.wait(tasks)
                    await sleep(self.__settings.timeout_loop)
            await sleep(0.01)

    def __callback_task(self, *args, **kwargs) -> None:
        future: Future = kwargs['future']
        task: Task = kwargs['task']
        id: str = kwargs['id']
        future.set_result(task.result())

        for group in self.__futures:
            for item in group:
                del item[id]

        self.__callback(task.result())

    def initialize(self) -> None:
        if not self.__background_task:
            self.__background_task = asyncio.create_task(
                self.__background_worker()
            )

    async def deinitialize(self) -> None:
        if self.__background_task:
            while self.__futures:
                await sleep(1)

            self.__background_task.cancel()

    @staticmethod
    def grouper(n, iterable, fillvalue=None):
        """grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"""
        args = [iter(iterable)] * n
        return zip_longest(fillvalue=fillvalue, *args)
