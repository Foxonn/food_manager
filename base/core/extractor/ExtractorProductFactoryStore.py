from base.core.extractor import ExtractorProductFactory

__all__ = ['ExtractorProductFactoryStore']


class ExtractorProductFactoryStore(dict):
    def __setitem__(
        self,
        key: ExtractorProductFactory,
        value: ExtractorProductFactory
    ) -> None:
        key = key.type
        if key in super().keys():
            raise Exception(f'This type: {key}, already register.')

        super().__setitem__(key, value)
