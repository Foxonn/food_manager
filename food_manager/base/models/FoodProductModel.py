from pydantic import BaseModel

__all__ = ['FoodProductModel']


class MacronutrientsModel(BaseModel):
    proteins: float = 0.0
    fats: float = 0.0
    carbohydrates: float = 0.0

    @property
    def calories(self) -> float:
        proteins = 4
        carbohydrates = 4
        fats = 9

        return sum(
            [
                self.proteins * proteins,
                self.fats * fats,
                self.carbohydrates * carbohydrates,
            ]
        )


class FoodProductModel(BaseModel):
    name: str
    price: float
    unit_measurement: str
    units: float = 0.0
    macronutrients: MacronutrientsModel
