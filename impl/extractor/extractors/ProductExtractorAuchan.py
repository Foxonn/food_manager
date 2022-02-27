from typing import (
    Any,
    Dict,
)

from bs4 import BeautifulSoup

from core.interfaces.extractor.ProductExtractor import ProductExtractor

__all__ = [

    "ProductExtractorAuchan",
]


class ProductExtractorAuchan(ProductExtractor):
    @property
    def type(self) -> str:
        return 'auchan'

    async def extract_product_info(self, data: str) -> Dict[str, Any]:
        print('*'*30)
        print(*[data], sep='\n\r')
        print('*'*30)
        soup = BeautifulSoup(data, "html.parser")
        product_name = soup.find(id="productName")
        print('*'*30)
        print(*[product_name], sep='\n\r')
        print('*'*30)
