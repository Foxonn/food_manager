import pathlib

from galo_ioc import add_factory
from yaml import safe_load

from base.core.extractor.ExtractorProduct import ExtractorProduct
from base.core.extractor.ExtractorProductFactory import ExtractorProductFactory
from impl.extractor.sbermarket.default.ExtractorProductSbermarket import ExtractorProductSbermarket

__all__ = ['load']


async def load() -> None:
    class ExtractorSbermarketProductFactory(ExtractorProductFactory):
        async def __call__(self) -> ExtractorProduct:
            return product_extractor_sbermarket

    path_to_config = pathlib.Path(
        pathlib.Path(__file__).parent.resolve(),
        'config.yaml'
    )
    settings = safe_load(path_to_config.read_text())

    product_extractor_sbermarket = ExtractorProductSbermarket(settings)

    add_factory(
        ExtractorProductFactory,
        ExtractorSbermarketProductFactory()
    )
