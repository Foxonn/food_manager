from core.interfaces import Scraper

__all__ = [
    "ScraperFactory",
]


class ScraperFactory:
    async def add_instance(self, instance: Scraper) -> None:
        raise NotImplementedError

    async def get_instance(self) -> Scraper:
        raise NotImplementedError
