from typing import Collection

from core.entities.FoodProduct import FoodProduct

__all__ = [
    "ProductExtractor",
]


class ProductExtractor:
    def __call__(self, data: Collection) -> FoodProduct:
        raise NotImplementedError
