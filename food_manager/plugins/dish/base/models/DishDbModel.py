from .DishBaseModel import DishBaseModel
from .DishPreviewModel import DishPreviewModel

__all__ = ['DishDbModel']


class DishDbModel(
    DishBaseModel,
    DishPreviewModel
):
    pass
