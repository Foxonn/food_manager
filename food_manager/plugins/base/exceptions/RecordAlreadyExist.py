__all__ = ['RecordAlreadyExist']


class RecordAlreadyExist(Exception):
    def __init__(self) -> None:
        msg = f"Record already exist."
        super().__init__(msg)
