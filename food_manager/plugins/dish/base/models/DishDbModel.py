from .DishBaseModel import DishBaseModel
from .DishPreviewModel import DishPreviewModel

__all__ = ['DishDbModel']


class DishDbModel(
    DishBaseModel,
    DishPreviewModel
):
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

    class Config:
        allow_mutation = False
        fields = {
            'ingredients': {'include': {'__all__': {'id'}}},
            'id': {'include': True},
            'name': {'include': True},
            'updated_at': {'include': True},
            'created_at': {'include': True},
        }
