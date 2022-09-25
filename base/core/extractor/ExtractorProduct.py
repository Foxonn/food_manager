from typing import Collection

from base.models import FoodProductModel

__all__ = ['ExtractorProduct']


class ExtractorProduct:
    __slots__ = ()

    def __call__(self, data: Collection) -> FoodProductModel:
        raise NotImplementedError
