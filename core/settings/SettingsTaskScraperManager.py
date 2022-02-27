from pydantic import BaseModel

__all__ = [
    "SettingsTaskScraperManager",
]


class SettingsTaskScraperManager(BaseModel):
    """
    :param
        waits_evaluate_batch_tasks: 60 sec
    """
    batch_urls: int = 3
    timeout_execute_batch_tasks: int = 60
    timeout_loop: int = 3
