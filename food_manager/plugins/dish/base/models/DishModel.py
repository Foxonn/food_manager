from typing import List

from .DishBaseModel import DishBaseModel
from ....food_product.base.models import FoodProductDbModel
from ....food_product.base.models import FoodProductModel

__all__ = ['DishModel']


class DishModel(DishBaseModel):
    ingredients: List[FoodProductDbModel | FoodProductModel]

    @property
    def total_sum(self) -> int:
        return sum([p.price for p in self.ingredients])

    @property
    def total_calories(self) -> int:
        return sum([p.macronutrients.calories for p in self.ingredients])

    @property
    def total_fats(self) -> int:
        return sum([p.macronutrients.fats for p in self.ingredients])

    @property
    def total_carbohydrates(self) -> int:
        return sum([p.macronutrients.carbohydrates for p in self.ingredients])

    @property
    def total_proteins(self) -> int:
        return sum([p.macronutrients.proteins for p in self.ingredients])
