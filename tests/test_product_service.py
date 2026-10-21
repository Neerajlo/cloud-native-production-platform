import sys
from pathlib import Path

SERVICE_DIR = (
    Path(__file__).resolve().parents[1]
    / "services"
    / "product-service"
)
sys.path.insert(0, str(SERVICE_DIR))

from app import app

from fastapi.testclient import TestClient

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) >= 1