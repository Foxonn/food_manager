from uuid import UUID

__all__ = ['NotFoundException']


class NotFoundException(Exception):
    def __init__(self, id: UUID) -> None:
        msg = f"Record with id: {id} not found."
        super().__init__(msg)
