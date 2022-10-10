__all__ = ['ChangeAttributeException']


class ChangeAttributeException(Exception):
    def __init__(self, *args: object) -> None:
        msg = "Attribute cannot change."
        super().__init__(msg, *args)
