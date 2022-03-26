from typing import Collection

__all__ = [
    "RequestProduct",
]


class RequestProduct:
    async def __call__(self, url: str) -> Collection:
        raise NotImplementedError
