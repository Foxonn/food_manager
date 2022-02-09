from typing import Collection

__all__ = [
    "ProductRequest",
]


class ProductRequest:
    @property
    def type(self) -> str:
        raise NotImplementedError

    async def get(self, url: str) -> Collection:
        raise NotImplementedError