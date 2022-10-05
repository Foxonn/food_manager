from pydantic import BaseModel

from .MacronutrientsModel import MacronutrientsModel

__all__ = ['FoodProductModel']


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
