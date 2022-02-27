from core.interfaces.request.ProductRequest import ProductRequest

__all__ = [
    "ProductRequestFactoryStoreFactory",
]


class ProductRequestFactoryStoreFactory:
    async def add_instance(self, instance: ProductRequest) -> None:
        raise NotImplementedError

    async def get_instance(self, type_product_extractor: str) -> ProductRequest:
        raise NotImplementedError
