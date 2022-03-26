from typing import Collection

from core.entities.FoodProduct import FoodProduct

__all__ = [
    "ExtractorProduct",
]


class ExtractorProduct:
    def __call__(self, data: Collection) -> FoodProduct:
        raise NotImplementedError
