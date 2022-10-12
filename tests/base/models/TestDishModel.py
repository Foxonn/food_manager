from food_manager.plugins.dish.base.models.DishModel import DishModel
from food_manager.plugins.food_product.base.models import FoodProductModel
from food_manager.plugins.food_product.base.models.MacronutrientsModel import \
    MacronutrientsModel


class TestDishModel:
    def test_dish_1(self) -> None:
        food_product_1 = FoodProductModel(
            name='Крупа гречневая «Мистраль» ядрица',
            price=16999,
            units=900,
            unit_measurement='г',
            macronutrients=MacronutrientsModel(
                carbohydrates=720,
                fats=34,
                proteins=120,
            )
        )

        food_product_2 = FoodProductModel(
            name='Филе индейки «Индилайт» голени охлажденное',
            price=24000,
            units=600,
            unit_measurement='г',
            macronutrients=MacronutrientsModel(
                carbohydrates=0,
                fats=100,
                proteins=160,
            )
        )

        dish = DishModel(
            name='Блюдо',
            ingredients=[
                food_product_1,
                food_product_2
            ]
        )

        assert dish.total_sum == sum(
            [
                food_product_1.price,
                food_product_2.price,
            ]
        )
        assert dish.total_carbohydrates == sum(
            [
                food_product_1.macronutrients.carbohydrates,
                food_product_2.macronutrients.carbohydrates,
            ]
        )
        assert dish.total_fats == sum(
            [
                food_product_1.macronutrients.fats,
                food_product_2.macronutrients.fats,
            ]
        )
        assert dish.total_proteins == sum(
            [
                food_product_1.macronutrients.proteins,
                food_product_2.macronutrients.proteins,
            ]
        )
        assert dish.total_calories is not None
