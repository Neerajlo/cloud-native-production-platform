from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI(title="Order Service", version="1.0.0")


class OrderItem(BaseModel):
    product_id: int
    quantity: int


class OrderRequest(BaseModel):
    customer_id: int
    items: List[OrderItem]


orders = []


@app.get("/health")
def health():
    return {"status": "healthy", "service": "order-service"}


@app.post("/orders")
def create_order(order: OrderRequest):
    new_order = {
        "order_id": str(uuid4()),
        "customer_id": order.customer_id,
        "items": [item.model_dump() for item in order.items],
        "status": "created"
    }
    orders.append(new_order)
    return new_order


@app.get("/orders")
def list_orders():
    return orders