from base.core.scraper import ScraperProduct

__all__ = ['ScraperProductFactory']


class ScraperProductFactory:
    __slots__ = ()

    @property
    def type(self) -> str:
        raise NotImplementedError

    async def __call__(self) -> ScraperProduct:
        raise NotImplementedError
