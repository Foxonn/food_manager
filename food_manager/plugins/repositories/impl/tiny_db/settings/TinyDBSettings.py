from pydantic import BaseModel

__all__ = ['TinyDBSettings']


class TinyDBSettings(BaseModel):
    storage: str
