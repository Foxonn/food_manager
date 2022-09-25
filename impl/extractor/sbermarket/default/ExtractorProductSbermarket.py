from bs4 import BeautifulSoup

from base.core.extractor import ExtractorProduct
from base.models import FoodProductModel
from base.settings import SettingsSbermarket

__all__ = ['ExtractorProductSbermarket']


class ExtractorProductSbermarket(ExtractorProduct):
    __slots__ = (
        "__settings",
        "__selector_name",
        "__selector_price",
        "__selector_weight",
        "__selector_nutrition_name",
        "__selector_nutrition_value",
    )

    def __init__(self, settings: SettingsSbermarket) -> None:
        self.__settings = settings
        self.__selector_name = self.__settings.selector_name
        self.__selector_price = self.__settings.selector_price
        self.__selector_weight = self.__settings.selector_weight
        self.__selector_nutrition_name = self.__settings.selector_nutrition_name
        self.__selector_nutrition_value = self.__settings.selector_nutrition_value

    def __call__(self, data: str) -> FoodProductModel:
        soup = BeautifulSoup(data, 'html.parser')
        name = soup.select_one(self.__selector_name).text.strip()
        price = float(
            soup.select_one(self.__selector_price).attrs['content'].strip()
        )
        weight, unit_measurement = soup.select_one(
            self.__selector_weight
        ).text.strip().split()

        nutrition = dict(
            zip(
                [
                    data.text.strip()
                    for data in soup.select(self.__selector_nutrition_name)
                ],
                [
                    float(data.text.strip().split()[0])
                    for data in soup.select(self.__selector_nutrition_value)
                ]
            )
        )

        return FoodProductModel(
            name=name,
            price=price,
            proteins=nutrition['Белки'],
            fats=nutrition['Жиры'],
            carbohydrates=nutrition['Углеводы'],
            callories=nutrition['Калорийность'],
            unit_measurement=unit_measurement,
            weight=weight,
        )
