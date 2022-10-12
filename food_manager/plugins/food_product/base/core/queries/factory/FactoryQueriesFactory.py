from .QueriesFactory import QueriesFactory

__all__ = ['FactoryQueriesFactory']


class FactoryQueriesFactory:
    __slots__ = ()

    async def __call__(self) -> QueriesFactory:
        raise NotImplementedError
