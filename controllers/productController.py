from fastapi import APIRouter
from services.productsService import getProducts

productRouter = APIRouter()

# Teste
@productRouter.get('/api/products')
def getAll():
    return getProducts()