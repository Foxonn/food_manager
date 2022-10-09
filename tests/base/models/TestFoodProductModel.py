from food_manager.plugins.base.models import FoodProductModel
from food_manager.plugins.base.models import MacronutrientsModel


class TestFoodProductModel:
    def test_product_1(self) -> None:
        kkal = 34.5

        model = FoodProductModel(
            name='Молоко Parmalat ультрапастеризованное 0.5%',
            price=980,
            units=1000,
            unit_measurement='ml',
            macronutrients=MacronutrientsModel(
                carbohydrates=470,
                fats=50,
                proteins=280,
            )
        )

        assert kkal == model.macronutrients.calories / 100

    def test_product_2(self) -> None:
        kkal = 125

        model = FoodProductModel(
            name='Паэлья «4 Сезона» замороженная',
            price=52299,
            units=600,
            unit_measurement='g',
            macronutrients=MacronutrientsModel(
                carbohydrates=163,
                fats=30,
                proteins=82,
            )
        )

        assert kkal == model.macronutrients.calories / 100
