import asyncio
from asyncio import (
    CancelledError, Future,
    Task, sleep,
)
from copy import deepcopy
from functools import partial
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
    )

    def __init__(
        self,
        scraper: Scraper
    ) -> None:
        self.__scraper = scraper
        self.__futures: Optional[Dict[str, (str, Future)]] = {}
        self.__background_task: Optional[Task] = None

    async def add_task(self, url: str) -> None:
        id = str(uuid4())
        future = Future()
        self.__futures[id] = (url, future)
        await future

        print('\n' + '*'*30)
        print(*[future.result()], sep='\n\r')
        print('*'*30 + '\n')

    async def __request(self, url: str) -> None:
        await self.__scraper(url)

    async def __background_worker(self):
        while True:
            if self.__futures:
                tasks: List[Task] = []
                for item in self.__futures.copy().items():
                    id, value = item
                    url, future = value
                    task = asyncio.create_task(self.__scraper(url))
                    task.add_done_callback(partial(
                        self.__callback,
                        future=future)
                    )
                    tasks.append(task)
                await asyncio.wait(tasks)
            await sleep(0.1)

    def __callback(self, *args, **kwargs) -> None:
        future: Future = kwargs['future']
        future.set_result(True)
        del future

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
