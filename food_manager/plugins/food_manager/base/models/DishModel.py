from typing import List

from pydantic import BaseModel

from .FoodProductDbModel import FoodProductDbModel

__all__ = ['DishModel']


class DishModel(BaseModel):
    ingredients: List[FoodProductDbModel]

    @property
    def total_sum(self) -> int:
        return sum([p.price for p in self.ingredients])

    @property
    def total_calories(self) -> int:
        return sum([i.macronutrients.calories for i in self.ingredients])

    @property
    def total_fats(self) -> int:
        return sum([i.macronutrients.fats for i in self.ingredients])

    @property
    def total_carbohydrates(self) -> int:
        return sum([i.macronutrients.carbohydrates for i in self.ingredients])

    @property
    def total_proteins(self) -> int:
        return sum([i.macronutrients.proteins for i in self.ingredients])
