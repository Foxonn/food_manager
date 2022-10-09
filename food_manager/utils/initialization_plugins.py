from food_manager.utils.startup_utils import load_plugins
from food_manager.utils.startup_utils import read_module_names

__all__ = ['initialization_plugins']


async def initialization_plugins(module_names_path: str) -> None:
    module_names = read_module_names(module_names_path)
    await load_plugins(module_names)
