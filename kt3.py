import requests
import pytest

@pytest.fixture
def base_url():
    return "https://dummyjson.com"

def get_products(base_url):
    response = requests.get(f"{base_url}/products")
    return response.json()

def get_product(base_url, product_id):
    response = requests.get(f"{base_url}/products/{product_id}")
    return response.json()

def add_todo(base_url, todo_data):
    response = requests.post(f"{base_url}/todos/add", json=todo_data)
    return response.json()

def add_product(base_url, product_data):
    response = requests.post(f"{base_url}/products/add", json=product_data)
    return response.json()


class TestDummyJSONAPI:

    def test_get_products(self, base_url):
        data = get_products(base_url)
        assert "products" in data
        assert len(data["products"]) > 0

    def test_get_single_product(self, base_url):
        data = get_product(base_url, 1)
        assert data["id"] == 1

    def test_add_todo(self, base_url):
        payload = {
            "todo": "Новая задача",
            "completed": False,
            "userId": 5
        }
        data = add_todo(base_url, payload)
        assert data["todo"] == "Новая задача"
        assert data["completed"] is False

    def test_add_product(self, base_url):
        payload = {
            "title": "Новый телефон",
            "price": 100
        }
        data = add_product(base_url, payload)
        assert data["title"] == "Новый телефон"
        assert data["price"] == 100
