import requests

def test_welcome():
    response = requests.get("http://localhost:8000/api/welcome-message")
    print("Welcome message:", response.json())

def test_save_message():
    payload = {"message": "Quiero ver la carta completa"}
    response = requests.post("http://localhost:8000/api/save-user-message", json=payload)
    print("Save message:", response.json())

if __name__ == "__main__":
    test_welcome()
    test_save_message()