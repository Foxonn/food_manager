from core.interfaces.request.RequestProduct import RequestProduct

__all__ = [
    "RequestProductFactory",
]


class RequestProductFactory:
    async def __call__(self) -> RequestProduct:
        raise NotImplementedError
