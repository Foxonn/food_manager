from datetime import datetime
from uuid import uuid4

from ....core.commands import CreateProductCommand
from .....base.models import FoodProductDbModel
from .....base.models import MacronutrientsModel
from .....repositories.core import FoodProductRepository

__all__ = ['CreateProductCommandImpl']


class CreateProductCommandImpl(
    CreateProductCommand
):
    __slots__ = (
        '__repository',
    )

    def __init__(
        self,
        repository: FoodProductRepository,
    ) -> None:
        self.__repository = repository

    async def __call__(
        self,
        name: str,
        price: int,
        unit_measurement: str,
        units: int,
        proteins: int,
        fats: int,
        carbohydrates: int,
    ) -> None:
        time = datetime.now()
        product = FoodProductDbModel(
            id=uuid4(),
            name=name,
            price=price,
            unit_measurement=unit_measurement,
            units=units,
            macronutrients=MacronutrientsModel(
                proteins=proteins,
                fats=fats,
                carbohydrates=carbohydrates,
            ),
            created_at=time,
            updated_at=time,
        )
        await self.__repository.add_product(
            product=product
        )
