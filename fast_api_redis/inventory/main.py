# python3 -m venv venv
# venv\Scripts\activate
#pip install fastapi
#pip install "uvicorn[standard]"
#pip install redis-om
# uvicorn main:app --reload --port 8000

from turtle import st
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection,HashModel 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

redis = get_redis_connection(
    host = "redis-19627.c244.us-east-1-2.ec2.cloud.redislabs.com",
    port = 19627,
    password = "hMOz4gdd0QfupmF4MXRVNMOgFqLNAlA5",
    decode_responses = True
)

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

@app.get("/products")
def all():
    return [format(x) for x in Product.all_pks()]

def format(pk:str):
    product = Product.get(pk)
    print(product)
    return {
        'id':product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity,
    }

@app.get("/products/{pk}")
def get(pk:str):
    return Product.get(pk)

@app.delete("/products/{pk}")
def delete(pk:str):
    return Product.delete(pk)

@app.post("/products")
def create(product:Product):
    return product.save()
