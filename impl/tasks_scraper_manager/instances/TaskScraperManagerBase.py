import asyncio
from asyncio import (
    Future,
    Task,
    sleep,
)
from functools import partial
from itertools import zip_longest
from uuid import uuid4
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Coroutine
)

from core.interfaces.scraper.ProductScraper import ProductScraper
from core.interfaces.tasks_manager.TaskScraperManager import TaskScraperManager
from core.settings import SettingsTaskScraperBaseManager

__all__ = [
    "TaskScraperManagerBase",
]


class TaskScraperManagerBase(TaskScraperManager):
    __slots__ = (
        "__background_task",
        "__futures",
        "__scraper",
        "__tasks",
        "__settings",
        "__callback",
    )

    def __init__(
        self,
        settings: Dict[str, Any],
        scraper: ProductScraper,
    ) -> None:
        self.__settings = SettingsTaskScraperBaseManager(**settings)
        self.__scraper = scraper
        self.__callback: Optional[Callable[[str], str]] = None
        self.__futures: Optional[Dict[str, (str, Future)]] = {}
        self.__tasks: Optional[Dict[str, Task]] = {}
        self.__background_task: Optional[Task] = None

    def set_callable_command(
        self,
        callback: Coroutine[Any, Any, None]
    ) -> None:
        self.__callback = callback

    async def parse_page(
        self,
        urls: List[str]
    ) -> None:
        if self.__callback is None:
            raise ValueError("Need set callable function!")

        batch_urls = self.grouper(
            self.__settings.batch_urls,
            urls
        )
        for urls in batch_urls:
            for url in urls:
                if not url:
                    continue
                id = str(uuid4())
                future = Future()
                self.__futures[id] = (url, future)
            await asyncio.wait(
                [item[1] for item in self.__futures.values()],
                timeout=self.__settings.timeout_execute_batch_tasks,
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
                            self.__callback_task,
                            future=future,
                            task=task,
                            id=id,
                        )
                    )
                    self.__tasks[id] = task
                await asyncio.wait(self.__tasks.values())
                await sleep(self.__settings.timeout_loop)
            await sleep(0.01)

    def __callback_task(self, *args, **kwargs) -> None:
        future: Future = kwargs['future']
        task: Task = kwargs['task']
        id: str = kwargs['id']

        future.set_result(task.result())

        del self.__futures[id]
        del self.__tasks[id]

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
    def grouper(
        n,
        iterable,
        fillvalue=None
    ):
        """grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"""
        args = [iter(iterable)] * n
        return zip_longest(fillvalue=fillvalue, *args)
