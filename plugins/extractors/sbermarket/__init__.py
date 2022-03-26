import pathlib

from galo_ioc import add_factory
from yaml import safe_load

from core.interfaces.extractor.ExtractorProduct import ExtractorProduct
from core.interfaces.extractor.ExtractorProductFactory import ExtractorProductFactory
from impl.extractor.sbermarket.ExtractorProductSbermarket import ExtractorProductSbermarket

__all__ = [
    "load",
]


async def load() -> None:
    class ExtractorSbermarketProductFactory(ExtractorProductFactory):
        async def __call__(self) -> ExtractorProduct:
            return product_extractor_sbermarket

    path_to_config = pathlib.Path(
        pathlib.Path(__file__).parent.resolve(),
        'config.yaml'
    )

    with open(path_to_config) as fp:
        settings = safe_load(fp)

    product_extractor_sbermarket = ExtractorProductSbermarket(settings)

    add_factory(
        ExtractorProductFactory,
        ExtractorSbermarketProductFactory()
    )
