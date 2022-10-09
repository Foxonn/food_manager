import asyncio
import os

from dotenv import load_dotenv
from galo_ioc import FactoryContainerImpl

from food_manager.utils.initialization_plugins import initialization_plugins


async def main() -> None:
    load_dotenv()
    module_names_path = os.getenv('MODULE_NAMES_PATH')

    with FactoryContainerImpl():
        await initialization_plugins(module_names_path)


if __name__ == '__main__':
    asyncio.run(main())
