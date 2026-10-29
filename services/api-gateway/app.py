import os
import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Cloud-Native API Gateway", version="1.0.0")

PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL",
    "http://product-service:8000"
)

ORDER_SERVICE_URL = os.getenv(
    "ORDER_SERVICE_URL",
    "http://order-service:8002"
)

@app.get("/health")
def health():
    return {"status": "healthy", "service": "api-gateway"}


@app.get("/api/products")
async def list_products():
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(
                f"{PRODUCT_SERVICE_URL}/products"
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail="Product service unavailable"
        ) from exc


@app.get("/api/products/{product_id}")
async def get_product(product_id: int):
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(
                f"{PRODUCT_SERVICE_URL}/products/{product_id}"
            )
            if response.status_code == 404:
                raise HTTPException(
                    status_code=404,
                    detail="Product not found"
                )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail="Product service unavailable"
        ) from exc
    
    @app.post("/api/orders")
    async def create_order(order: dict):
     try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.post(
                f"{ORDER_SERVICE_URL}/orders",
                json=order
            )
            response.raise_for_status()
            return response.json()
     except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail="Order service unavailable"
        ) from exc


@app.get("/api/orders")
async def list_orders():
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(
                f"{ORDER_SERVICE_URL}/orders"
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail="Order service unavailable"
        ) from exc
    @app.post("/api/orders")
    async def create_order(order: dict):
     try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.post(
                f"{ORDER_SERVICE_URL}/orders",
                json=order
            )
            response.raise_for_status()
            return response.json()
     except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail="Order service unavailable"
        ) from exc