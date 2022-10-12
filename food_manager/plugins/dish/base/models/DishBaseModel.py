from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

__all__ = ['DishBaseModel']


class DishBaseModel(BaseModel):
    id: UUID
    name: str
    updated_at: datetime
    created_at: datetime
