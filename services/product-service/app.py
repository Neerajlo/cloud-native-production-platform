from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Product Service", version="1.0.0")


class Product(BaseModel):
    id: int
    name: str
    price: float = Field(gt=0)
    category: str


PRODUCTS = {
    1: Product(id=1, name="Laptop", price=65000, category="Electronics"),
    2: Product(id=2, name="Keyboard", price=1500, category="Accessories"),
    3: Product(id=3, name="Headphones", price=2500, category="Audio"),
}


@app.get("/health")
def health():
    return {"status": "healthy", "service": "product-service"}


@app.get("/products")
def list_products():
    return list(PRODUCTS.values())


@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = PRODUCTS.get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product