from .CommandsFactory import CommandsFactory

__all__ = ['FactoryCommandsFactory']


class FactoryCommandsFactory:
    __slots__ = ()

    async def __call__(self) -> CommandsFactory:
        raise NotImplementedError
