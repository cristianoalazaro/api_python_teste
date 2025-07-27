from typing import List, Dict
from repositories.inMemory.productRepository import products

database: Dict[str, List] = {
    "products": products
}