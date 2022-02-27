from typing import Collection

__all__ = [
    "ProductRequest",
]


class ProductRequest:
    async def __call__(self, url: str) -> Collection:
        raise NotImplementedError
