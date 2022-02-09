from core.interfaces.ProductRequest import ProductRequest

__all__ = [
    "ProductRequestFactory",
]


class ProductRequestFactory:
    async def add_instance(self, instance: ProductRequest) -> None:
        raise NotImplementedError

    async def get_instance(self) -> ProductRequest:
        raise NotImplementedError
