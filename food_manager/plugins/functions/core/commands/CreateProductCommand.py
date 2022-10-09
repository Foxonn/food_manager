__all__ = ['CreateProductCommand']


class CreateProductCommand:
    __slots__ = ()

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
        raise NotImplementedError
