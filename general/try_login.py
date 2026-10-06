import requests

URL = "http://127.0.0.1:5100/auth/login"
response = requests.post(
    URL,
    json={"username": "student", "password": "Learn123!"},
    timeout=5,
)
print(response.status_code, response.json())
