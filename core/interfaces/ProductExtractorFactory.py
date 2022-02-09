from core.interfaces.ProductExtractor import ProductExtractor

__all__ = [
    "ProductExtractorFactory",
]


class ProductExtractorFactory:
    async def add_instance(self, instance: ProductExtractor) -> None:
        raise NotImplementedError

    async def get_instance(self) -> ProductExtractor:
        raise NotImplementedError
