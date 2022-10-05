from .FoodProductRepositoryStoreFactoryImpl import \
    FoodProductRepositoryStoreFactoryImpl
from .tiny_db.FoodProductRepositoryFactoryTinyDB import \
    FoodProductRepositoryFactoryTinyDB

__all__ = ['store_factory']

store_factory = FoodProductRepositoryStoreFactoryImpl()

store_factory.register(
    repository=FoodProductRepositoryFactoryTinyDB()
)
