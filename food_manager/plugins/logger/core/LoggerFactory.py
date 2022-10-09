from logging import Logger

__all__ = ['LoggerFactory']


class LoggerFactory:
    __slots__ = ()

    async def __call__(self) -> Logger:
        raise NotImplementedError
