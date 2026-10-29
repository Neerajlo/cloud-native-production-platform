import os
import logging

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api-gateway")

# Application
app = FastAPI(
    title="Cloud-Native API Gateway",
    version="1.0.0",
    description="API Gateway for Product and Order microservices",
)

# Microservice URLs
PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL",
    "http://product-service:8000",
)

ORDER_SERVICE_URL = os.getenv(
    "ORDER_SERVICE_URL",
    "http://order-service:8002",
)

# Request models for order validation
class OrderItem(BaseModel):
    product_id: int = Field(gt=0, description="Product ID must be positive")
    quantity: int = Field(gt=0, description="Quantity must be positive")


class OrderRequest(BaseModel):
    customer_id: int = Field(gt=0, description="Customer ID must be positive")
    items: list[OrderItem] = Field(
        min_length=1,
        description="At least one order item is required",
    )


# Health endpoint
@app.get("/health", tags=["Health"])
async def health():
    return {
        "status": "healthy",
        "service": "api-gateway",
    }


# List all products
@app.get("/api/products", tags=["Products"])
async def list_products():
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(
                f"{PRODUCT_SERVICE_URL}/products"
            )
            response.raise_for_status()
            return response.json()

    except httpx.HTTPStatusError as exc:
        logger.error("Product service returned an HTTP error")
        raise HTTPException(
            status_code=502,
            detail="Product service returned an error",
        ) from exc

    except httpx.RequestError as exc:
        logger.error("Product service is unreachable")
        raise HTTPException(
            status_code=503,
            detail="Product service unavailable",
        ) from exc


# Get one product
@app.get("/api/products/{product_id}", tags=["Products"])
async def get_product(product_id: int):
    if product_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Product ID must be positive",
        )

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(
                f"{PRODUCT_SERVICE_URL}/products/{product_id}"
            )

            if response.status_code == 404:
                raise HTTPException(
                    status_code=404,
                    detail="Product not found",
                )

            response.raise_for_status()
            return response.json()

    except HTTPException:
        raise

    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=502,
            detail="Product service returned an error",
        ) from exc

    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail="Product service unavailable",
        ) from exc


# Create an order
@app.post("/api/orders", tags=["Orders"])
async def create_order(order: OrderRequest):
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.post(
                f"{ORDER_SERVICE_URL}/orders",
                json=order.model_dump(),
            )
            response.raise_for_status()
            return response.json()

    except httpx.HTTPStatusError as exc:
        logger.error("Order service returned an HTTP error")
        raise HTTPException(
            status_code=502,
            detail="Order service returned an error",
        ) from exc

    except httpx.RequestError as exc:
        logger.error("Order service is unreachable")
        raise HTTPException(
            status_code=503,
            detail="Order service unavailable",
        ) from exc


# List all orders
@app.get("/api/orders", tags=["Orders"])
async def list_orders():
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(
                f"{ORDER_SERVICE_URL}/orders"
            )
            response.raise_for_status()
            return response.json()

    except httpx.HTTPStatusError as exc:
        logger.error("Order service returned an HTTP error")
        raise HTTPException(
            status_code=502,
            detail="Order service returned an error",
        ) from exc

    except httpx.RequestError as exc:
        logger.error("Order service is unreachable")
        raise HTTPException(
            status_code=503,
            detail="Order service unavailable",
        ) from exc