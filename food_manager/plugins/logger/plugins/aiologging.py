from aiologger import Logger
from galo_ioc import add_factory

from ..core import LoggerFactory

__all__ = ['load']


async def load() -> None:
    class AiologgerLoggerFactory(LoggerFactory):
        __slots__ = ()

        async def __call__(self) -> Logger:
            return logger

    logger = Logger()

    add_factory(
        factory_type=LoggerFactory,
        factory=AiologgerLoggerFactory()
    )
