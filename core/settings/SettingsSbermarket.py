from pydantic import BaseModel

__all__ = [
    "SettingsSbermarket",
]


class SettingsSbermarket(BaseModel):
    selector_name: str
    selector_price: str
    selector_weight: str
    selector_nutrition_name: str
    selector_nutrition_value: str
