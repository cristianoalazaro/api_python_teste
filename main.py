from fastapi import FastAPI
from controllers.productController import productRouter

app = FastAPI()

# Teste
@app.get('/api')
def read_root():
    return {"status": "API running"}

app.include_router(productRouter, tags=['products'])