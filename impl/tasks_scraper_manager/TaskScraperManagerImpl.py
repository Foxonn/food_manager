import asyncio
from asyncio import (
    Future,
    Task,
    sleep,
)
from functools import partial
from itertools import zip_longest
from typing import (
    Dict,
    List,
    Optional,
)
from uuid import uuid4

from core.interfaces.Scraper import Scraper
from core.interfaces.TaskScraperManager import TaskScraperManager

__all__ = [
    "TaskScraperManagerImpl",
]


class TaskScraperManagerImpl(TaskScraperManager):
    __slots__ = (
        "__background_task",
        "__futures",
        "__scraper",
        "__tasks",
    )

    def __init__(
        self,
        scraper: Scraper
    ) -> None:
        self.__scraper = scraper
        self.__futures: Optional[Dict[str, (str, Future)]] = {}
        self.__tasks: Optional[Dict[str, Task]] = {}
        self.__background_task: Optional[Task] = None

    async def add_tasks(self, urls: List[str]) -> None:
        batch_urls = self.grouper(3, urls)
        for urls in batch_urls:
            for url in urls:
                if not url:
                    continue
                id = str(uuid4())
                future = Future()
                self.__futures[id] = (url, future)
            await asyncio.wait(
                [item[1] for item in self.__futures.values()],
                timeout=60,
            )

    async def __request(self, url: str) -> None:
        await self.__scraper(url)

    async def __background_worker(self):
        while True:
            if self.__futures:
                for item in self.__futures.copy().items():
                    id, value = item
                    url, future = value
                    task = asyncio.create_task(self.__scraper(url))
                    task.add_done_callback(
                        partial(
                            self.__callback,
                            future=future,
                            task=task,
                            id=id,
                        )
                    )
                    self.__tasks[id] = task
                await asyncio.wait(self.__tasks.values())
                await sleep(3)
            await sleep(0.1)

    def __callback(self, *args, **kwargs) -> None:
        future: Future = kwargs['future']
        task: Task = kwargs['task']
        id: str = kwargs['id']
        future.set_result(task.result())

        del self.__futures[id]
        del self.__tasks[id]

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
