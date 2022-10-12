from typing import List
from uuid import UUID

from pydantic import BaseModel

from .DishBaseModel import DishBaseModel

__all__ = ['DishPreviewModel']


class DishPreviewModel(BaseModel):
    ingredients_ids: List[UUID]
