from core.interfaces.extractor import ExtractorProduct

__all__ = ['ExtractorProductFactory']


class ExtractorProductFactory:
    async def __call__(self) -> ExtractorProduct:
        raise NotImplementedError
