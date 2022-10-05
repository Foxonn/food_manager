from pydantic import BaseModel

__all__ = ['MacronutrientsModel']


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
