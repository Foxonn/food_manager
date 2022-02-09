from pydantic import BaseModel

__all__ = [
    "FoodProduct",
]


class FoodProduct(BaseModel):
    name: str
    price: float
    proteins: float = 0.0
    fats: float = 0.0
    carbohydrates: float = 0.0
    weight: float = 0.0
    callories: float = 0.0
