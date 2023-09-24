from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection,HashModel
from starlette.requests import Request 
import requests, time
from fastapi.background import BackgroundTasks


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3001','http://localhost:8000'],
    allow_methods=['*'],
    allow_headers=['*']
)

redis = get_redis_connection(
    host = "redis-11931.c276.us-east-1-2.ec2.cloud.redislabs.com",
    port = 11931,
    password = "lRbkkruK6m2oE2rrsDoz63Mzr4O6Mb4i",
    decode_responses = True
)

class Order(HashModel):
    product_id: str
    price: float
    fee: int
    total: float
    quantity: int
    status: str # pending, completed, refunded

    class Meta:
        database = redis

@app.get("/orders/{pk}")
def get(pk:str):
    order = Order.get(pk)
    # redis.xadd('refund_order', order.dict(), '*') # si no esta en la cola de refund, lo agrega
    return order

@app.post("/orders")
async def create(request: Request, background_tasks: BackgroundTasks):
    body = await request.json()
    print(body)
    req = requests.get('http://localhost:8000/products/%s' % body['id'])
    product = req.json()
    order = Order(
        product_id = body['id'],
        price = product['price'],
        fee = 0.2 * product['price'],
        total = 1.2 * product['price'],
        quantity = 1,
        status = 'pending'
    )
    order.save()
    background_tasks.add_task(order_completed, order)
    return order

def order_completed(order: Order):
    time.sleep(5)
    order.status = 'completed'
    order.save()
    redis.xadd('order_completed', order.dict(),'*')