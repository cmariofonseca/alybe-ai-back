import requests

def test_order_saving():
    """Test order saving functionality"""
    url = "http://localhost:8000/api/save-order"
    payload = {
        "table_id": "table-5",
        "items": [
            {"name": "Margherita Pizza", "quantity": 2, "price": 12.50},
            {"name": "Coca-Cola", "quantity": 1, "price": 3.00}
        ],
        "total": 28.00,
        "status": "pending"
    }
    
    response = requests.post(url, json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    test_order_saving()