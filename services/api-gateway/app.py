import os
import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Cloud-Native API Gateway", version="1.0.0")

PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL",
    "http://localhost:8001"
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