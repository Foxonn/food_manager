import aiosqlite
from aiosqlite import Connection
from galo_ioc import add_factory

from ..providers.aiosqlite.base import AiosqliteFactory

__all__ = ['load']


async def load() -> None:
    class AiosqliteFactoryImpl(
        AiosqliteFactory
    ):
        async def __call__(self) -> Connection:
            return aiosqlite.connect('food_manager.db')

    add_factory(
        factory_type=AiosqliteFactory,
        factory=AiosqliteFactoryImpl()
    )
