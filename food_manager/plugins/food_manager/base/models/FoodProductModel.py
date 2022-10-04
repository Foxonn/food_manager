from pydantic import BaseModel

__all__ = ['FoodProductModel']


class MacronutrientsModel(BaseModel):
    """
    Макронутриенты указываются в миллиграммах (мг)

    proteins - белок\n
    fats - жиры\n
    carbohydrates - углеводы\n
    """
    proteins: int
    fats: int
    carbohydrates: int

    @property
    def calories(self) -> int:
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
    """
    name - наименование продукта\n
    price - стоимость товара в копейках\n
    unit_measurement - единицы измерения (л, мл, г, кг)\n
    units - кол-во продукта\n
    macronutrients - макронутриенты\n
    """
    name: str
    price: float
    unit_measurement: str
    units: float = 0.0
    macronutrients: MacronutrientsModel
