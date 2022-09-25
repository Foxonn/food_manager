from base.core.request import RequestProduct

__all__ = ['RequestProductFactory']


class RequestProductFactory:
    __slots__ = ()

    @property
    def type(self) -> str:
        raise NotImplementedError

    async def __call__(self) -> RequestProduct:
        raise NotImplementedError
