__all__ = ['CommandsFactory']


class CommandsFactory:
    __slots__ = ()

    async def create_product_command(
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
